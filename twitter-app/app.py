from flask import Flask, request, render_template, redirect, flash, jsonify
import mysql.connector

from tweet_fetch import get_tweets
from inference import predict

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

        start = len(myresult)
        end = len(tweets_mine) - len(myresult)

        mycursor.execute("SELECT * FROM tweet_mentions WHERE handle='" + handle + "'")
        myresult = mycursor.fetchall()

        start_one = len(myresult)
        end_one = len(tweets) - len(myresult)

        for i in range(start_one, end_one):
            bully = predict(tweets[i])
            sql = "INSERT INTO tweet_mentions (screenname, handle, tweet, bully) VALUES (%s, %s, %s, %s)"
            val = (tweets_screen_names[i], handle, tweets[i], bully)
            mycursor.execute(sql, val)

        for i in range(start, end):
            bully = predict(tweets_mine[i])
            sql = "INSERT INTO twitter (handle, tweet, bully) VALUES(%s, %s, %s)"
            val = (handle, tweets_mine[i], bully)
            mycursor.execute(sql, val)

        conn.commit()

        status = "Pushed"

        if start == 0 or start_one == 0:
            status = "No new data to push"

        return jsonify({"res": status})

    if request.method == "GET":
        tweets = get_tweets("@sdharchou")

        return jsonify({"tweets": tweets})
