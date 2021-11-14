from flask import Flask, request,render_template, jsonify
from replit import db
from PIL import Image, ImageDraw
from threading import Thread
import datetime as dt
from config import time_war, colors

app = Flask('')
con = 23.5

def update():
    pass

@app.route('/')
def main():
    update()
    return render_template('index.html',
                           map=db["map"],
                           enumerate=enumerate,
                           colors=colors,
                           type=type,
                           str=str)

def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    server = Thread(target=run)
    server.start()