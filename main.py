# Copyright (c) 2021 Azhaan Salam
# Licensed under the MIT License

import discord
import os
import nltk
nltk.download('punkt')
client = discord.Client()

@client.event
async def on_ready():
  print(f'What a terrible name, {client.user}? What is wrong with you?')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  mes = message.content.lower()
  words = nltk.word_tokenize(mes)
  if "i'm".lower() in words :
    index = words.index("i'm".lower())
    name = words[index+1:]
    realname = '"'
    for i in name:
      realname += i
      realname += " "
    realname2 = realname[:-1]
    realname2 += '"'
    await message.channel.send(f"Hello {realname2}, I'm {client.user}! xD")
  if "lol" in words :
    await message.channel.send("LOLOLOLOLOLOL xD")

  if "stop" in words :
    await message.channel.send("NO U STOP LOLOLOL xD")

  if "bruh" in words :
    await message.channel.send("BRUHHHHHHHHH xD")

  if "annoying" in words :
    await message.channel.send("Someone call for me? xD")
  
  if "no" in words :
    noindex = words.index("no")
    if words[noindex + 1] == "u" or words[noindex + 1] == "you":
      await message.channel.send("https://tenor.com/view/roasted-oh-shookt-gif-8269968")
  if "uno" in words :
    unoindex = words.index("uno")
    if words[unoindex + 1] == 'reverse':
      await message.channel.send("https://tenor.com/view/uno-reverse-allcolor-reverse-card-gif-13843660")

  if "shut" in words :
    await message.channel.send("https://tenor.com/view/shut-up-shush-shh-ok-bird-gif-17679708")
  if "got" in words :
    gotindex = words.index("got")
    if words[gotindex + 1] == 'em' or words[gotindex + 1] == 'them':
      await message.channel.send("https://tenor.com/view/gotword-deeznuts-gottem-deez-nuts-gif-4394929")
  elif "gottem" in words :
    await message.channel.send("https://tenor.com/view/gotword-deeznuts-gottem-deez-nuts-gif-4394929")
  elif "gotem" in words :
    await message.channel.send("https://tenor.com/view/gotword-deeznuts-gottem-deez-nuts-gif-4394929")
  if "noob" in words:
    await message.channel.send("NOOOOOOOOOBBBBBBBB LOLOLOL xD")
  if "hate" in words:
    await message.channel.send("i hate u")
    await message.channel.send("https://tenor.com/view/roasted-oh-shookt-gif-8269968")
  if "look" in words:
    await message.channel.send("no u")
    await message.channel.send("https://tenor.com/view/roasted-oh-shookt-gif-8269968")
  if f"816855127486234644" in words:
    for i in range(20):
      await message.channel.send(message.author.mention)
  if "-_-" in words:
    await message.channel.send("-_____________- xD")
  if "yay" in words:
    await message.channel.send("YAYAYAYAYAYAYAYAYAYAYAYAY xD")
  if "yes" in words:
    await message.channel.send("no")
  if "no" in words:
    await message.channel.send("yes")
client.run(os.getenv("token"))
