from flask import Flask, request, render_template, redirect, flash, jsonify
import mysql.connector

from tweet_fetch import get_tweets
from inference import predict
from warning import warn_user

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = 'my-secret-key'
app.config['SESSION_TYPE'] = 'filesystem'

conn = mysql.connector.connect(host="localhost", user="root", password="root", database="breakingbits")

@app.route('/fetch', methods=['GET', 'POST'])
def fetch():

    if request.method == "POST":

        data = request.get_json()
        handle = data['handle']

        tweets, tweets_screen_names, tweets_mine = get_tweets(handle)

        mycursor = conn.cursor()

        mycursor.execute("SELECT * FROM twitter WHERE handle='" + handle + "'")
        myresult = mycursor.fetchall()

        mycursor.execute("SELECT * FROM tweet_mentions WHERE handle='" + handle + "'")
        myresult_one = mycursor.fetchall()

        print(tweets)

        existing_tweets = [myresult_ones[3] for myresult_ones in myresult_one]
        existing_tweets_mine = [myresults[2] for myresults in myresult]

        print(existing_tweets)

        for i in range(len(tweets)):
            if(tweets[i] not in existing_tweets):
                bully = predict(tweets[i])
                sql = "INSERT INTO tweet_mentions (screenname, handle, tweet, bully, status) VALUES (%s, %s, %s, %s, %s)"
                val = (tweets_screen_names[i], handle, tweets[i], bully, 0)
                mycursor.execute(sql, val)

            else:
                break

        conn.commit()

        mycursor.execute("SELECT * FROM tweet_mentions WHERE handle='" + handle + "'")
        myresult_one = mycursor.fetchall()

        users = [myresult_ones[1] for myresult_ones in myresult_one if myresult_ones[4] == 0 and myresult_ones[5] == 0]
        users = set(users)

        print(users)

        for user in users:
            sql = "UPDATE tweet_mentions SET status = 1 WHERE screenname = '" + user + "'"
            mycursor.execute(sql)

        for i in range(len(tweets_mine)):
            if(tweets_mine[i] not in existing_tweets_mine):
                bully = predict(tweets_mine[i])
                sql = "INSERT INTO twitter (handle, tweet, bully) VALUES(%s, %s, %s)"
                val = (handle, tweets_mine[i], bully)
                mycursor.execute(sql, val)
            else:
                break

        conn.commit()

        if len(users) > 0:
            warn_user("xxxxx", "xxxxx", users)

        status = "Pushed"

        return jsonify({"res": status})

    if request.method == "GET":
        tweets = get_tweets("xxxxxx")

        return jsonify({"tweets": tweets})
