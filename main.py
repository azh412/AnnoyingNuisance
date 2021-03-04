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
  if "lol" in words:
    await message.channel.send("LOLOLOLOLOLOL xD")

  if "stop" in words:
    await message.channel.send("NO U STOP LOLOLOL xD")

  if "bruh" in words:
    await message.channel.send("BRUHHHHHHHHH xD")

  if "annoying" in words:
    await message.channel.send("Someone call for me? xD")
  
  if "no" in words:
    noindex = words.index("no")
    if words[noindex + 1] == "u" or words[noindex + 1] == "you":
      await message.channel.send("https://tenor.com/view/roasted-oh-shookt-gif-8269968")
  if "uno" in words:
    unoindex = words.index("uno")
    if words[unoindex + 1] == 'reverse':
      await message.channel.send("https://tenor.com/view/uno-reverse-allcolor-reverse-card-gif-13843660")
client.run(os.getenv("token"))