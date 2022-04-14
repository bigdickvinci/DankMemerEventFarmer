import os
import sys
import threading

import discord
from discord.ext import commands , tasks
from discord.utils import get
from discord import file


try:
  __import__("discum")
  import discum
  from discum.utils.button import Buttoner
except ImportError:
  os.system("python -m pip install --upgrade git+https://github.com/Merubokkusu/Discord-S.C.U.M.git#egg=discum")
  import discum
  from discum.utils.button import Buttoner


token = os.environ["token"]
bot = commands.Bot(command_prefix='1dankmemereventfarmer1',self_bot=True)
disbot = discum.Client(token=token, log={"console": False,"file":"log.txt"})
bot.remove_command("help")

extensions = ["events"]

ownerid = "902195286544384070"
dankmemerid = "270904126974590976"

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

def setupcogs():
  print("\nLoading cogs...")
  for extension in extensions:
    try:
      bot.load_extension(f"cogs.{extension}")
      print(f"Loaded [ {extension} ]")
    except Exception as error:
      print(f"Error loading [ {extension} ] // [ {error} ]")
      restart_bot()






def gtway():
  disbot.gateway.run()
  disbot.gateway.log = {"console":False, "file":"log.txt"}

def gtwaythread():
  x = threading.Thread(target=gtway)
  x.start()

@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.offline)
  print(f"\n{bot.user}\n")

def tapbuttonnolink(strguildid,strchannelid,strmsgid,choice):
  message = disbot.getMessage(strchannelid, strmsgid)
  data = message.json()[0]
  buts = Buttoner(data["components"])
  disbot.click(data["author"]["id"],channelID=data["channel_id"],guildID=strguildid,messageID=data["id"],messageFlags=data["flags"],data=buts.getButton(choice))



if __name__ == "__main__":
  setupcogs()
  gtwaythread()
  bot.run(token,bot=False)
