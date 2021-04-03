#!/bin/python3

import discord
import requests
from discord.ext import commands
import subprocess
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()  #Makes the .env file accessible to my script as the source of the environment variables

ID=int(os.getenv("ID"))
bot=commands.Bot(command_prefix="!")

def download(url,path):  #To download a sent image

    r=requests.get(url)  #We get a response object from the URL. This object further has attributes which help us navigate the different functionalities of the page.
    with open(path,'wb') as f:  #r.content contains the bytes of the image, so when we write that into a file, it is interpreted as an image ('wb' mode stands for write-bytes)
        f.write(r.content)

def md5sum(a):  #To calculate the md5sum of a sent image

    args=f"md5sum {a}"
    process= subprocess.Popen(args,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)  #Shell=True means the args command is executed by using a shell. The stdout(output) and stderr(error) pipes are combined as per subprocess documentation
    output= process.stdout.read().decode()
    s=output.split(" ")
    return s[0]
    
@bot.event  #Bot activation message while logging in
async def on_ready():
     print("You have logged in as {0}".format(bot.user))
     channel=bot.get_channel(ID)
     await channel.send("Welcome back Mr.Anderson!")
     await bot.process_commands()  #We cannot trigger the bot.command instructions wihout writing this line in case of bot.event

@bot.event  #For commands
async def on_message(message):
    if message.author==bot.user:
        return
    else:
        if message.content.startswith("!hello"):
            await message.channel.send("Welcome to the matrix.")

        if message.content.startswith("!attach"):  #Calculating the md5sum of any image sent to the server
            attachments=message.attachments
            attach=attachments[0].url
            await message.channel.send(attach)

            your_path='/home/vader/Downloads/'
            name='fileee'
            url=attach.split('%')[0]  #The message.attachment object url has some some special characters at the end which the browser can't seem to parse (like %27%). So we remove that portion
            path=str(your_path+name)
            download(url,path)
        
            output2=md5sum(path)
            await message.channel.send(output2)

            os.remove(path)

    await bot.process_commands(message)  #We cannot trigger the bot commands wihout writing this line in case of bot.event

@bot.command()  #Taking any number of words as arguements and printing them
async def print(ctx, *args):
    output=""
    for arg in args:
        output=output + " " + arg
    await ctx.channel.send(output)
    

bot.run(os.getenv("TOKEN"))
