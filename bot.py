import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6640601389:AAEQaqs79FcPTW5YMdwNZv_rhV7M7urWE1k")

API_ID = int(os.environ.get("API_ID", "23374527"))

API_HASH = os.environ.get("API_HASH", "5a48ec466dfa7df47e2a109ed40019bc")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
