from flask import Flask, request, render_template, redirect, flash, jsonify
import mysql.connector
from sightengine.client import SightengineClient

from fetch import get_feed
from block import block_user

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = 'my-secret-key'
app.config['SESSION_TYPE'] = 'filesystem'

conn = mysql.connector.connect(host="localhost", user="root", password="root", database="breakingbits")

client = SightengineClient('23433686', 'RbtybMJzE8iURkDvFcMV')

@app.route('/fetch', methods=['GET', 'POST'])
def fetch():

    if request.method == "POST":

        data = request.get_json()

        username = data['username']
        password = data['password']

        urls = get_feed(username, password ,"xxxxxx")

        im_urls = [url for url in urls.keys()]
        profile_urls = [url for url in urls.values()]

        predictions = [client.check('nudity').set_url(url)for url in urls.keys()]
        predictions = [round(prediction['nudity']['raw']) for prediction in predictions]

        mycursor = conn.cursor()

        mycursor.execute("SELECT * FROM facebook WHERE user='" + "xxxxx" + "'")
        myresults = mycursor.fetchall()

        imgs = [myresult[1] for myresult in myresults]

        for i in range(len(im_urls)):
            if im_urls[i] not in imgs:
                sql = "INSERT INTO facebook (img, user, url, bully, status) VALUES (%s, %s, %s, %s, %s)"
                val = (im_urls[i], "xxxxx", profile_urls[i], predictions[i], 0)
                print(val)
                mycursor.execute(sql, val)

                if predictions[i] == 1:
                    block_user(username, password, profile_urls[i])

            else:
                break

        conn.commit()

        sql = "SELECT * FROM facebook WHERE user='Vastu Kosh'"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()

        print(myresults)

        profiles = [myresult[3] for myresult in myresults if myresult[4] == 0 and myresult[5] == 0]
        profiles = set(profiles)

        print(profiles)

        return jsonify({"res": "Pushed"})

@app.route('/', methods=['GET'])
def index():

    return jsonify({"hello": "world"})
