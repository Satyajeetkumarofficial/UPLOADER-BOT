#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | Modifieded By : @DC4_WARRIOR

import ntplib
from time import ctime, sleep
try:
    client = ntplib.NTPClient()
    response = client.request('pool.ntp.org')
    print("[INFO] System time synchronized: ", ctime(response.tx_time))
except Exception as e:
    print("[WARN] Failed to sync time: ", e)
sleep(1)

from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Running!"

def run():
    app.run(host="0.0.0.0", port=8080)

# Flask server अलग Thread में चलेगा
threading.Thread(target=run).start()

import os
import logging
from config import Config
from pyrogram import Client as Clinton
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="plugins")
    Warrior = Clinton("@BOT_X_BOT",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    plugins=plugins)
    Warrior.run()
