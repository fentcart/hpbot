import os
import discord
import asyncio
from config import TOKEN

hp = discord.Bot(intents=discord.Intents.all())

footer = "Made By Osf0 :)"

@hp.event
async def on_ready():
    print(f"{hp.user} Is Now Online")
    activities = [
        discord.Activity(type=discord.ActivityType.watching, name="#1 ANIME REALM"),
        discord.Activity(type=discord.ActivityType.watching, name=f"{len(hp.users)} Members!"),
        discord.Activity(type=discord.ActivityType.watching, name="Join The Server!"),
        discord.Activity(type=discord.ActivityType.playing, name="Anime Brawlers!"),
        discord.Activity(type=discord.ActivityType.watching, name="Heroic Productions On YT")
    ]

    while True:
        for activity in activities:
            await hp.change_presence(activity=activity)
            await asyncio.sleep(5)


@hp.event
async def on_message(message: discord.Message):
    channel = message.channel

    if message.content == "<@788214943269912606>":
        embed = discord.Embed(
            title="ANTI PING",
            description=f"**<@{message.author.id}> PLEASE Do Not @ The Owner Heroic! He Is Very Busy And Doesn't Wanna Be Bothered.**",
            color=discord.Colour.red()
        )
        await channel.send(embed=embed)
        await message.delete()

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        hp.load_extension(f'commands.{filename[:-3]}')

hp.run(TOKEN)