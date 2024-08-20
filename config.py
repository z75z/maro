import json
import os
import time
from os import getenv
from typing import List
import requests
from utils import get_restarted
from pyrogram import Client, enums
from pytgcalls import PyTgCalls
super_sudoers: List[int] = [833360381, 1818734394]


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
TOKEN = getenv("TOKEN", "7155835267:AAHz2NyrX1O4dyRgjNxMaJVcoWEMGg9EY_w")
SESSION = getenv("SESSION", "AgDFycsAeVHkKExrE_xJEUMTwyg9z1CzpoZG73D4IsbkwZAfVOtqlwU_8Q8cULOYVuqxfZso4k6k-f3ANnlNBKdlf5UtOP6sp9W3Nxae_S8RJQ7dK0t5K6eDALv-EsYnuxepv2Vjc6K_gJL-XYu7loX5me2x9GNfgl9zXl7B_M66JLZLYecfoeo8SLMPYE8gNXBXobXqU1no0mrfVUV0jbK2o-6U6ZIOpcfmlww5lrKdibyuvV-LTGft3BGXmxCmB3Pubd9Nwz9jebooer5ZT83u3qrIMpKEvO6Iy1gs5XeFs5FeYOc1gLkoxr4l6EyHgyhht1Vk3fL0fnuYUuLfom0LTpdtfwAAAABsZ686AA")
# Your API ID and Hash from https://my.telegram.org/apps
API_ID = 12962251
API_HASH = "b51499523800add51e4530c6f552dbc8"

# Chat used for logs
log_chat = 6367618993
# Sudoers and super sudoers
sudoers = list(map(int, getenv("sudoers", "833360381").split()))
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
