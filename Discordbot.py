
import asyncio
import time
import discord
from discord.ext import commands
import json
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")
client = commands.Bot(command_prefix="!")
ProgrammingHeroes = client.get_guild(658403310516174899)
profanity = ["fuck", "fick", "fck", "slut", "cunt", "bithc", "btch", "bch", "son of beach", "son of bitch",
             "sun of bitch", "sun of beach", "skrub", "pussy", "fucking", "fucker", "fcking", "fckr", "fcker"]


def available(guild):
    online = 0
    idle = 0
    offline = 0
    for i in guild.members:
        if str(i.status) == "online":
            online += 1
        if str(i.status) == "offline":
            offline += 1
        else:
            idle += 1
    return online, idle, offline


async def background_task():
    await client.wait_until_ready()
    global ProgrammingHeroes
    ProgrammingHeroes = client.get_guild(658403310516174899)
    while not client.is_closed():
        try:
            online, idle, offline = available(ProgrammingHeroes)
            with open("usermetrics.csv", 'a') as f:
                f.write(f"{int(time.time())},{online},{idle},{offline}\n")
            plt.clf()
            df = pd.read_csv("usermetrics.csv", names=[
                             "time", "online", "idle", "offline"])
            df["date"] = pd.to_datetime(df.time, unit='s')
            df["total"] = df["online"]+df["offline"]+df["idle"]
            df.drop("time", 1, inplace=True)
            df.set_index("date", inplace=True)
            print(df.head())
            df["online"].plot()
            plt.legend()
            plt.savefig("online.png")
            await asyncio.sleep(5)
        except Exception as e:
            print(str(e))
            await asyncio.sleep(5)


@client.event
async def on_ready():
    print(f"You have logged in as {client.user}")


@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    if "!hello" in message.content.lower():
        await message.channel.send('Hi!')
    elif "!membercount" == message.content.lower():
        await message.channel.send(f"```py\n{ProgrammingHeroes.member_count}```")
    elif "closebotlogoutghazib3t4" == message.content.lower():
        await discord.Message.delete(message)
        await client.close()

    elif "!available" == message.content.lower():
        online, idle, offline = available(ProgrammingHeroes)
        await message.channel.send(f"```Online: {online}.\nIdle/busy/dnd: {idle}.\nOffline: {offline}```")
        file = discord.File("online.png", filename="online.png")
        await message.channel.send("online.png", file=file)
    elif "!ispremium" == message.content:
        if(discord.user == discord.PremiumType):
            await message.channel.send("You are premium member of Discord ")
        else:
            await message.channel.send("You are NOT premium member of Discord ")
    elif any(i in message.content.lower() for i in profanity):
        await message.channel.send("NO BAD WORDS")
        await discord.Message.delete(message)

    await client.process_commands(message)


@client.event
# reference to discord.py which retrieve payload
async def on_raw_reaction_add(payload):
    print(payload.emoji.name)
    message_id = payload.message_id
    if message_id == 675438100306067488:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        if payload.emoji.name == "python":
            programmer = guild.get_role(673184041649832006)
            role = guild.get_role(673217657738362890)

        elif payload.emoji.name == "csharp":
            programmer = guild.get_role(673184041649832006)
            role = guild.get_role(673898023624900618)
        elif payload.emoji.name == "cpp":
            programmer = guild.get_role(673184041649832006)
            role = guild.get_role(673897660100378645)
        elif payload.emoji.name == "JS":
            programmer = guild.get_role(673184041649832006)
            role = guild.get_role(673897879370203186)
        elif payload.emoji.name == "clang":
            programmer = guild.get_role(673184041649832006)
            role = guild.get_role(673184344851873792)
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        if role is not None:
            member = discord.utils.find(
                lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                await member.add_roles(programmer)
                print("Done")
            else:
                print("Member not found")
        else:
            print("Role not found")
    elif message_id == 675635033997836289:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        if payload.emoji.name == "arts":
            role = guild.get_role(673184120834359316)
            print(payload.emoji.name)
        elif payload.emoji.name == "money":
            role = guild.get_role(673184177436491786)
            print(payload.emoji.name)
        elif payload.emoji.name == "game":
            role = guild.get_role(673184086323363844)
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        if role is not None:
            member = discord.utils.find(
                lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print("Done")
            else:
                print("member not found")
    else:
        print("Role is not found")


@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 675438100306067488:
        role = guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        if payload.emoji.name == "python":
            programmer = guild.get_role(673184041649832006)
            role = guild.get_role(673217657738362890)
        elif payload.emoji.name == "csharp":
            programmer = guild.get_role(673184041649832006)
            role = guild.get_role(673898023624900618)
        elif payload.emoji.name == "cpp":
            programmer = guild.get_role(673184041649832006)
            role = guild.get_role(673897660100378645)
        elif payload.emoji.name == "JS":
            programmer = guild.get_role(673184041649832006)
            role = guild.get_role(673897879370203186)
        elif payload.emoji.name == "clang":
            programmer = guild.get_role(673184041649832006)
            role = guild.get_role(673184344851873792)

        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        if role is not None:
            member = discord.utils.find(
                lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print("Done")
            else:
                print("Member not found")

        else:
            print("Role not found")
    elif message_id == 675635033997836289:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        if payload.emoji.name == "arts":
            role = guild.get_role(673184120834359316)
        elif payload.emoji.name == "money":
            role = guild.get_role(673184177436491786)
        elif payload.emoji.name == "game":
            role = guild.get_role(673184086323363844)
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        if role is not None:
            member = discord.utils.find(
                lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print("Done")
            else:
                print("member not found")
        else:
            print("Role is not found")


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
client.loop.create_task(background_task())
client.run("token")
