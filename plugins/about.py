import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','6640601389:AAEQaqs79FcPTW5YMdwNZv_rhV7M7urWE1k')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"Total User:- {total_user()}\nBot :- @dlx_renamerbot\nBuy Subscription :- @dlx_smith\nSubscribe :- https://t.me/animes_in_30mb\n\nTotal Renamed File :-{total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))} ",quote=True)
