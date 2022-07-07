import os
import discord
from discord.ext import commands , tasks
from main import disbot,dankmemerid,tapbuttonnolink
from discum.utils.button import Buttoner
import asyncio
import datetime
import random


def tapbuttoncolumn(guildID,channelID,messageID,row,column):
  message = disbot.getMessage(channelID, messageID)
  data = message.json()[0]
  buts = Buttoner(data["components"])
  disbot.click(data["author"]["id"],channelID=data["channel_id"],guildID=guildID,messageID=data["id"],messageFlags=data["flags"],data=buts.getButton(row=row,column=column),)


countr = 0

class Events(commands.Cog):
    def __init__(self,bot):
      self.bot = bot

  
    @commands.Cog.listener()
    async def on_message(self,message):
      if message.author.id == dankmemerid:
        data = {}
        msg = disbot.getMessage(str(message.channel.id), str(message.id))
        try:
          data = msg.json()[0]
        except:
          return
        if "referenced_message" in str(data):
          return
        timestamp = data["timestamp"]
        datetimestamp = datetime.datetime.fromisoformat(timestamp).replace(tzinfo=None)
        if "Attack the boss by clicking" in data["content"]:
          global countr
          while True:
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
            msg0 = disbot.getMessage(channelID, messageID)
            data0 = msg0.json()[0]
            if str(data0["components"][0]["components"][0]["disabled"]) == "True":
              print(f"Clicked BOSS button {countr} times [ {discordlink} ] (SERVER: {guildn.name} / CHANNEL: {channeln.name}) DELAY(Last Click): {uptime}")
              return
            else:
              countr =+ 1
              continue
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
          print(f"Clicked F button [ {discordlink} ] (SERVER: {guildn.name} / CHANNEL: {channeln.name}) DELAY: {uptime}")
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
          print(f"Clicked {choice} button [ {discordlink} ] (SERVER: {guildn.name} / CHANNEL: {channeln.name}) DELAY: {uptime}")
          return
      else:
        return


def setup(bot):
    bot.add_cog(Events(bot))
