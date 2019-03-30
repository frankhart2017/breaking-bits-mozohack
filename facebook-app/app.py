from flask import Flask, request, render_template, redirect, flash, jsonify
import mysql.connector

from fetch import get_feed

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = 'my-secret-key'
app.config['SESSION_TYPE'] = 'filesystem'

conn = mysql.connector.connect(host="localhost", user="root", password="root", database="breakingbits")

@app.route('/fetch', methods=['GET', 'POST'])
def fetch():

    if request.method == "POST":

        data = request.get_json()

        username = data['username']
        password = data['password']

        get_feed(username, password)

        return jsonify({"res": "Pushed"})

@app.route('/', methods=['GET'])
def index():

    return jsonify({"hello": "world"})
