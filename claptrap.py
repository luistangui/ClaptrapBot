import time
import telegram
import re
import conf
import commands
import json
import logging
import os
import sys

os.chdir(os.path.dirname(os.path.realpath(__file__)))

logging.basicConfig(filename='debug.log',level=logging.DEBUG)
bot = telegram.Bot(conf.botID)

commands.init(bot.getMe()['username'])


def handle(bot,msg):
	logging.debug(json.dumps(msg)+"\n")
	#if not msg.has_key("text") and not msg.has_key("chat"):
	if "text" not in msg and "chat" not in msg:
		return
	logging.debug("test\n")
	chat_id = msg['chat']['id']
	text	= msg['text']
	
	print("Mensaje recibido: "+ text)
	
	for comando in commands.list:
		if comando[0].match(text):
			bot.sendMessage(chat_id,comando[1]())
			return
	#bot.sendMessage(chat_id,"test")

#bot.notifyOnMessage(callback=handle, run_forever=True)
bot.startPolling(handle)

#while(1):
#	time.sleep(10)
