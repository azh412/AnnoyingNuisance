import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print(f'What a terrible name, {client.user}? What is wrong with you?')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  mes = message.content
  words = mes.split()
  if "i'm".lower() in words:
    index = words.index("i'm".lower())
    name = words[index+1:]
    realname = '"'
    for i in name:
      realname += i
      realname += " "
    realname2 = realname[:-1]
    realname2 += '"'
    await message.channel.send(f"Hello {realname2}, I'm {client.user}! :)")

client.run(os.getenv("token"))