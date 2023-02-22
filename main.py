import sys
from discord.ext import commands
import discord
import io
import os
import asyncio
import requests

bot = commands.Bot(command_prefix="!")
elevenLabsAPIKey = os.getenv("ELEVENTOKEN")
#elevenLabsAPIKey = "enter api key when testing"

@bot.event
async def on_ready():
    print("connected")
    return

@bot.command()
async def rob(ctx, *args):
    if len(args) < 3:
        stab = 0.35
        boost = 0.6
    else:
        stab = args[1]
        boost = args[2]
    await synthesize_voice_clip(ctx, args[0], "jo1ygh26P6QtQ7bLPIJ3", "Rob",  args[1], args[2])
"""
    # Sets up event to allow the bot to wait until the clip has been played before leaving
    stop_event = asyncio.Event()
    loop = asyncio.get_event_loop()

    def wait_for_audio(error):
        if error:
            print(error)

        def clear():
            stop_event.set()
        loop.call_soon_threadsafe(clear)

    # Joins the calling users channel
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()
    # Attempt to play audio
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.play(discord.FFmpegPCMAudio(
        audio, executable='/usr/bin/ffmpeg'), after=wait_for_audio)

    # Leave the voice voice channel
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        # waits for the audio to stop
        await stop_event.wait()
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")
"""
@bot.command()
async def mattda(ctx, *args):
    if len(args) < 3:
        stab = 0.35
        boost = 0.6
    else:
        stab = args[1]
        boost = args[2]
    await synthesize_voice_clip(ctx, args[0], "PUooyE0VjiwElqBZHbWd", "Mattda", args[1], args[2])


@bot.command()
async def reid(ctx, *args):
    if len(args) < 3:
        stab = 0.35
        boost = 0.6
    else:
        stab = args[1]
        boost = args[2]
    await synthesize_voice_clip(ctx, args[0], "DuDfDhpoomHeT2o3HYiT", "Reid", args[1], args[2])

async def synthesize_voice_clip(ctx, msg, voiceID, voice_owner, stability=0.35, similarity_boost=0.6):
    try:
        stability = float(stability)
    except:
        stability = 0.35

    try:
        similarity_boost = float(similarity_boost)
    except:
        similarity_boost = 0.6

    if float(stability) < 0.0 or float(stability) > 1.0:
        await ctx.send("Stability Must be a float from 0.0 to 1.0")

    if float(similarity_boost) < 0.0 or float(similarity_boost) > 1.0:
        await ctx.send("similarity_boost Must be a float from 0.0 to 1.0")

    if len(msg) > 200:
        await ctx.send("Text must be less than 200 characters")
        await ctx.send(f"Current message is {len(msg)} characters")
        return
        
    url = "https://api.elevenlabs.io/v1/text-to-speech/" + voiceID
    headers = {'xi-api-key': elevenLabsAPIKey}

    r = requests.post(url, headers=headers, json=
    {
        "text": msg,
        "voice_settings": {
            "stability": float(stability),
            "similarity_boost": float(similarity_boost)
        }
    })

    r.raise_for_status()
    assert r.headers["Content-Type"] == "audio/mpeg"

    speach = r.content

    audio = io.BytesIO(speach)

    file = discord.File(audio, filename=voice_owner + ".mp3")

    await ctx.send(file=file)

token = os.getenv("TOKEN")
bot.run(token)
#bot.run("Enter token when testing")
sys.stdout.flush()