import os
import discord
from discord.ext import commands , tasks
from main import disbot,dankmemerid,ownerid,tapbuttonnolink
from discum.utils.button import Buttoner
import asyncio
import datetime
import random
try:
  __import__("termcolor")
  from termcolor import colored
except ImportError:
  os.system("pip install termcolor")

def tapbuttoncolumn(guildID,channelID,messageID,row,column):
  message = disbot.getMessage(channelID, messageID)
  data = message.json()[0]
  buts = Buttoner(data["components"])
  disbot.click(data["author"]["id"],channelID=data["channel_id"],guildID=guildID,messageID=data["id"],messageFlags=data["flags"],data=buts.getButton(row=row,column=column),)


class Events(commands.Cog):
    def __init__(self,bot):
      self.bot = bot


    @commands.Cog.listener()
    async def on_message(self,message):
      if message.author.id == dankmemerid:
        msg = disbot.getMessage(str(message.channel.id), str(message.id))
        data = msg.json()[0]
        if "referenced_message" in str(data):
          return
        timestamp = data["timestamp"]
        datetimestamp = datetime.datetime.fromisoformat(timestamp).replace(tzinfo=None)
        if "Attack the boss by clicking" in data["content"]:
          guildID = str(message.guild.id)
          channelID = str(message.channel.id)
          messageID = str(message.id)
          column = 0
          row = 0
          tapbuttoncolumn(guildID,channelID,messageID,row,column)
          nowdatetimestamp = datetime.datetime.fromisoformat(datetime.datetime.now().isoformat())
          uptime = nowdatetimestamp - datetimestamp
          channeln = await self.bot.fetch_channel(channelID)
          guildn = await self.bot.fetch_guild(guildID)
          discordlink = f'https://discord.com/channels/{guildID}/{channelID}/{messageID}'
          print(f"Clicked BOSS button [ {colored(discordlink, 'blue')} ] (SERVER: {colored(guildn.name, 'green')} / CHANNEL: {colored(channeln.name, 'green')}) DELAY: {colored(uptime, 'green')}")
          return
        elif data["content"] == "F":
          guildID = str(message.guild.id)
          channelID = str(message.channel.id)
          messageID = str(message.id)
          column = 0
          row = 0
          tapbuttoncolumn(guildID,channelID,messageID,row,column)
          nowdatetimestamp = datetime.datetime.fromisoformat(datetime.datetime.now().isoformat())
          uptime = nowdatetimestamp - datetimestamp
          channeln = await self.bot.fetch_channel(channelID)
          guildn = await self.bot.fetch_guild(guildID)
          discordlink = f'https://discord.com/channels/{guildID}/{channelID}/{messageID}'
          print(f"Clicked BOSS button [ {colored(discordlink, 'blue')} ] (SERVER: {colored(guildn.name, 'green')} / CHANNEL: {colored(channeln.name, 'green')}) DELAY: {colored(uptime, 'green')}")
          return
        elif "I just chose a secret number between 1 and 100" in str(data["embeds"]) and "icon_url" not in str(data["embeds"]):
          choices = ["Lower","Higher"]
          choice = random.choice(choices)
          guildID = str(message.guild.id)
          channelID = str(message.channel.id)
          messageID = str(message.id)
          tapbuttonnolink(guildID,channelID,messageID,choice)
          nowdatetimestamp = datetime.datetime.fromisoformat(datetime.datetime.now().isoformat())
          uptime = nowdatetimestamp - datetimestamp
          channeln = await self.bot.fetch_channel(channelID)
          guildn = await self.bot.fetch_guild(guildID)
          discordlink = f'https://discord.com/channels/{guildID}/{channelID}/{messageID}'
          print(f"Clicked BOSS button [ {colored(discordlink, 'blue')} ] (SERVER: {colored(guildn.name, 'green')} / CHANNEL: {colored(channeln.name, 'green')}) DELAY: {colored(uptime, 'green')}")
          return
      else:
        return


def setup(bot):
    bot.add_cog(Events(bot))
