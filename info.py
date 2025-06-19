import re
import os
from os import environ
from pyrogram import enums
from Script import script
import asyncio
import json
from collections import defaultdict
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '23361081'))
API_HASH = environ.get('API_HASH', '0605c5395b91ead763072251e20c3417')
BOT_TOKEN = environ.get('BOT_TOKEN', '8040135776:AAGXPSSYOoWd3nj_VZteK2TDhcfpcDq3Wfc')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5371238852 5102717153').split()]
USERNAME = environ.get('USERNAME', 'https://telegram.me/Rajesh1817')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002058942218'))
REQ_CHANNEL = environ.get('REQ_CHANNEL', '-1002232025730')
REQ_CHANNEL = int(REQ_CHANNEL) if REQ_CHANNEL and REQ_CHANNEL.lstrip('-').isdigit() else None
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002197398349').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Rajeah:Rajeah@rajesh2.2oma8nb.mongodb.net/?retryWrites=true&w=majority&appName=Rajesh2")
DATABASE_URI2 = environ.get('DATABASE_URI2', "mongodb+srv://Rajesh:Rajeah@rajesh.4m2jrxj.mongodb.net/?retryWrites=true&w=majority&appName=Rajesh")
DATABASE_NAME = environ.get('DATABASE_NAME', "Rajesh2")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Rajesh')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002058942218'))
QR_CODE = environ.get('QR_CODE', 'https://envs.sh/haY.jpg')
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]

#this vars is for when heroku or koyeb acc get banned, then change this vars as your file to link bot name
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1002232025730'))
URL = environ.get('URL', 'https://t.me/MTGxStreamBot')

# verify system vars
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002395713472'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/Tutorial01Ask")
TUTORIAL2 = environ.get("TUTORIAL2", "https://t.me/Tutorial01Ask")
TUTORIAL3 = environ.get("TUTORIAL3", "https://t.me/Tutorial01Ask")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/45a270fc6a0a1c183c614.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "5d9250c00801b067d7f83bfe54c4fba484505447")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEB5SITE", "krownlinks.com")
SHORTENER_API2 = environ.get("SHORTENER_API2", "5d9250c00801b067d7f83bfe54c4fba484505447")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "krownlinks.com")
SHORTENER_API3 = environ.get("SHORTENER_API3", "5d9250c00801b067d7f83bfe54c4fba484505447")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "krownlinks.co.")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "7200"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "21600"))

# languages search
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam"]

auth_channel = environ.get('AUTH_CHANNEL', '-1002139516496')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002633073907'))

# bot settings
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8080')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 600))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
PM_SEARCH = is_enabled('PM_SEARCH', False)
