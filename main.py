import os
import discord
from discord.ext import commands, tasks
from discord.utils import get
from discord import file
from discord.ext.commands import cooldown, BucketType



intents = discord.Intents().all()
activity=discord.Activity(type=discord.ActivityType.watching, name="vincicord")
bot = commands.Bot(command_prefix="*",activity=activity, intents=intents)
token = os.environ['token']
bot.remove_command("help")
guildID = os.environ["guild_id"]
channelID = os.environ["channel_id"]


@bot.event
async def on_ready():
  print(f"\n{bot.user}\n")
  loop.start()


@tasks.loop(seconds=305)
async def loop():
  users = {}
  guild = bot.get_guild(int(guildID))
  updatingchannel = bot.get_channel(int(channelID))
  for channel in guild.channels:
    chnl = discord.utils.get(bot.get_all_channels(), name=channel.name)
    if str(chnl.type) == "text" or str(chnl.type) == "news":
      async for message in chnl.history(limit=9999999):
        if not message.author.bot:
          if message.author.id in users:
            users.update({message.author.id:users.get(message.author.id)+1})
          else:
            users.update({message.author.id:1})
  sort = sorted(users.values())[::-1]
  keys = list(users.keys())
  vals = list(users.values())
  topuser = keys[vals.index(sort[0])]
  topusermessages = sort[0]
  print(f"{topuser} // {topusermessages}")
  tpusr = bot.get_user(int(topuser))
  await updatingchannel.edit(name=f"#1 msgs: {tpusr.name} / {topusermessages}")



bot.run(token)
