import os
import threading

import discord
from discord.ext import commands , tasks
from discord.utils import get
from discord import file


try: # import the discum library from github (to click buttons)
  __import__("discum")
  import discum
  from discum.utils.button import Buttoner
except ImportError:
  os.system("python -m pip install --upgrade git+https://github.com/Merubokkusu/Discord-S.C.U.M.git#egg=discum")
  import discum
  from discum.utils.button import Buttoner


token = os.environ["token"]
bot = commands.Bot(command_prefix='')
disbot = discum.Client(token=token, log=False)
bot.remove_command("help")

dankmemerid = "270904126974590976"

def gtway():
  disbot.gateway.run(auto_reconnect=True)

def gtwaythread():
  x = threading.Thread(target=gtway)
  x.start()

@bot.event
async def on_ready():
  bot.load_extension("cogs.events")
  print(f"\n{bot.user}\n")

def tapbuttonrownolink(guildID,channelID,messageID,row,column):
  message = disbot.getMessage(channelID, messageID)
  data = message.json()[0]
  buts = Buttoner(data["components"])
  disbot.click(data["author"]["id"],channelID=data["channel_id"],guildID=guildID,messageID=data["id"],messageFlags=data["flags"],data=buts.getButton(row=row,column=column))


if __name__ == "__main__":
  bot.run(token)
  gtwaythread()
