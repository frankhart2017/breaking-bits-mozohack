from flask import Flask, request, render_template, redirect, flash, jsonify
import mysql.connector

from tweet_fetch import get_tweets

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
        end = len(tweets) - len(myresult)

        mycursor.execute("SELECT * FROM tweet_mentions WHERE handle='" + handle + "'")
        myresult = mycursor.fetchall()

        start_one = len(myresult)
        end_one = len(tweets_mine) - len(myresult)

        for i in range(start, end):
            mycursor.execute("INSERT INTO twitter('handle', 'tweet') VALUES('" + handle + "', '" + tweets_mine[i] + "')")

        return jsonify({"res": myresult})

    if request.method == "GET":
        tweets = get_tweets("@sdharchou")

        return jsonify({"tweets": tweets})
