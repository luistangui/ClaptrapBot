import datetime
#from urllib import request
import requests
import re
import conf

urlbtc = 'https://blockchain.info/es/q/'

frases = ["no tengo frases, que planeas que diga?"]
list = []

def cmdHola():
	return frases[0]
def cmdTime():
	return str(datetime.datetime.now())
def cmdSource():
	return conf.source

def cmdBtcPrice():
	r = requests.get(urlbtc + "24hrprice")
	return r.text

def init(botName):
	holaRegex   = re.compile('^(hola|\/(hola|hello))(@'+botName+')? *$')
	timeRegex   = re.compile('^\/(fecha|time)(@'+botName+')? *$')
	sourceRegex = re.compile('^\/(codigo|source)(@'+botName+')? *$')
	btcPriceRegex = re.compile('\/btc([Pp]rice)?(@'+botName+')? *$')
	
	list.extend(	[
			[holaRegex,cmdHola]
			,[timeRegex,cmdTime]
			,[sourceRegex,cmdSource]
			,[btcPriceRegex,cmdBtcPrice]
		])
