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
  curtailment = None
  words = mes.split()
  if "i'm".lower() in words and curtailment = False:
    index = words.index("i'm".lower())
    name = words[index+1:]
    realname = '"'
    for i in name:
      realname += i
      realname += " "
    realname2 = realname[:-1]
    realname2 += '"'
    await message.channel.send(f"Hello {realname2}, I'm {client.user}! xD")
  if "lol" in words and curtailment = False:
    await message.channel.send("LOLOLOLOLOLOL xD")

  if "stop" in words and curtailment = False:
    await message.channel.send("NO U STOP LOLOLOL xD")

  if "bruh" in words and curtailment = False:
    await message.channel.send("BRUHHHHHHHHH xD")

  if "annoying" in words and curtailment = False:
    await message.channel.send("Someone call for me? xD")
  
  if "no" in words and curtailment = False:
    noindex = words.index("no")
    if words[noindex + 1] == "u" or words[noindex + 1] == "you":
      await message.channel.send("https://tenor.com/view/roasted-oh-shookt-gif-8269968")
  if "uno" in words and curtailment = False:
    unoindex = words.index("uno")
    if words[unoindex + 1] == 'reverse':
      await message.channel.send("https://tenor.com/view/uno-reverse-allcolor-reverse-card-gif-13843660")

  if "shut" in words and curtailment = False:
    await message.channel.send("https://tenor.com/view/shut-up-shush-shh-ok-bird-gif-17679708")
  if "got" in words and curtailment = False:
    gotindex = words.index("got")
    if words[gotindex + 1] == 'em' or words[gotindex + 1] == 'them':
      await message.channel.send("https://tenor.com/view/gotword-deeznuts-gottem-deez-nuts-gif-4394929")
  elif "gottem" in words and curtailment = False:
    await message.channel.send("https://tenor.com/view/gotword-deeznuts-gottem-deez-nuts-gif-4394929")
  elif "gotem" in words and curtailment = False:
    await message.channel.send("https://tenor.com/view/gotword-deeznuts-gottem-deez-nuts-gif-4394929")

  if "iaFGHJBADFGUAGYEDHJKGUYSFDJHAV" in words:
    if curtailment == False:
      curtailment = True
    else:
      curtailment = False
    
client.run(os.getenv("token"))