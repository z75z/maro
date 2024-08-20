import json
import os
import time
from os import getenv
from typing import List
import requests
from utils import get_restarted
from pyrogram import Client, enums
from pytgcalls import PyTgCalls
super_sudoers: List[int] = [5964879906, 5964879906]
from dotenv import load_dotenv

load_dotenv()

####################################################################################




# start
wr = get_restarted()
if wr is None:
    if os.path.exists('info.json'):
        fileSize = os.path.getsize("info.json")
        if fileSize == 0:
            print("Please Input Your Token:\n")
            tokenBot = input()
            print("Please Input Your Session:\n")
            sessionAss = input()
            print("Please Input id sudo:\n")
            idSudo = input()

            aDict = {"Token": tokenBot, "Session": sessionAss, "idSudo": int(idSudo)}
            jsonString = json.dumps(aDict)
            jsonFile = open("info.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()
    
        aDict = {"Token": tokenBot, "Session": sessionAss, "idSudo": int(idSudo)}
        jsonString = json.dumps(aDict)
        jsonFile = open("info.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()


####################################################################################

# Token bot
TOKEN = getenv("TOKEN")
SESSION = getenv("SESSION")
# Your API ID and Hash from https://my.telegram.org/apps
API_ID = 7634570
API_HASH = "49265e23e8cb8218ac89d60777f280a6"

# Chat used for logs
log_chat = 6367618993
# Sudoers and super sudoers
sudoers = list(map(int, getenv("sudoers").split()))
sudoers += super_sudoers
developer = []
developer += sudoers
bot_start_time = time.time()

####################################################################################

def get_bot_information():
    bot_inf = requests.get(
        "https://api.telegram.org/bot" + TOKEN + "/getme")
    bot_info = bot_inf.json()
    result = bot_info["result"]
    bot_id = result["id"]
    bot_username = result["username"]
    bot_name = result["first_name"]
    return bot_id, bot_username, bot_name

app = Client(
    "Dream",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN,
    parse_mode=enums.ParseMode.HTML,
    plugins=dict(root="plugins"),
    in_memory=True, 
)

app2 = Client(
    "Dream2",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=str(SESSION),
)
pytgcalls = PyTgCalls(app2)

#####################################################################################


# Prefixes for commands, e.g: /command and !command
prefix: List[str] = ["/", "!", "."]

# List of disabled plugins
disabled_plugins: List[str] = []

# API keys
TENOR_API_KEY = "2MAL8NKBOO01"

# Bot version, do not touch this
with open("version.txt") as f:
    version = f.read().strip()
