#!/bin/python3

# This file will contain the functions which include :
# 1. Extracting message from discord and returning their strings
# 2. Mapping unicode characters with certain commonly used commands like starting a listening port, executing a brute force attack
# 3. Returning the Output with the original command
# 4. Downloading images and gifs and calculating their md5sum followed by mapping them to specific commands like (2)
# 5. More
#
# Note :
# Call all Functions using threads (Use Low Level Threading Like : start_new_thread)
# Store all downloaded media in /tmp       
# Use Asyncio ?


import discord
import requests
import json
import random
from discord.ext import commands
import subprocess
#from decouple import config
import os
#import youtube_dl
import time

'''
#try add this 
intents=discord.Intents.all()
#if the above don't work, try with this
#intents = discord.Intents.default()
#intents.members=True

client=discord.Client(intents=intents)
'''

ID=int(824362867657801779)

bot=commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
     print("You have logged in as {0}".format(bot.user))
     channel=bot.get_channel(ID)
     await channel.send("Welcome back Mr.Anderson!")

    #We cannot trigger the bot.command instructions wihout writing this line in case of bot.event
     await bot.process_commands()

@bot.event
async def on_message(message):
    if message.author==bot.user:
        return
    else:
        if message.content.startswith("!hello"):
            await message.channel.send("Welcome to the matrix")

    #We cannot trigger the bot commands wihout writing this line in case of bot.event
    await bot.process_commands(message)

bot.run("ODI0MzU3NjM4Mzc5Nzk4NTI4.YFuM4A.XP1SZn2A9Qu1CuP2RPSD0wbbfVI")

