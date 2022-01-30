import os
import discord
import PasswordGame
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = 'OTI4MDQ5NjYzMjA5MjYzMTQ1.YdTHmg.smcyaU9DxGbhgkp6AlSX1WaM7Kk'

bot = commands.Bot(command_prefix='!')

openGames = {}

rulesMessage = f"\
The game :joystick:: \n\
\n\
    The Password has digits from 0 to 9, no repeated digits.\n\
    Each :green_circle: means that the atempt has a right number in the right position.\n\
    Each :yellow_circle: means that the attempt has a right number in a wrong position.\n\
    Each :red_circle: mean that there is a wrong number in the attempt.\n\
\n\
Commands:\n\
To use any command use the prefix \"{bot.command_prefix}\".\n\
\n\
    - play: starts a new game.\n\
    - stop: close your game.\n\
    - next: proceed to next level.\n\
    - ans 'password': send an attempt to the game.\n\
        Example: \"{bot.command_prefix}ans 063\", try to answer with the password 063.\n\
"


@bot.event
async def on_ready():
    print("My Bot(y) is ready.")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("p:rules"))


@bot.command()
async def rules(ctx):
    user = ctx.message.author

    await ctx.send(rulesMessage)


@bot.command()
async def play(ctx):
    user = ctx.message.author

    openGames[user] = PasswordGame.Game()

    await ctx.send(f"<@{user.id}>:\n" + str(openGames[user]))


@bot.command()
async def stop(ctx):
    user = ctx.message.author

    if user in openGames:
        del openGames[user]


@bot.command()
async def next(ctx):
    user = ctx.message.author

    if user in openGames:
        if openGames[user].status == PasswordGame.Game.WON:
            openGames[user].startNextLevel()
        else:
            await ctx.send(f"<@{user.id}>, you haven't beat this level yet!")

        await ctx.send(f"<@{user.id}>:\n" + str(openGames[user]))


@bot.command()
async def ans(ctx, *, arg):
    user = ctx.message.author

    if user in openGames:
        if openGames[user].status == PasswordGame.Game.PLAYING:
            try:
                openGames[user].attempt(arg)
            except PasswordGame.InvalidInput as exc:
                await ctx.send(f"{user}, {exc.args[0]}")

            await ctx.send(f"<@{user.id}>:\n" + str(openGames[user]))
        else:
            await ctx.send(f"<@{user.id}>, you are not playing, go to the next level or start a new game.")


bot.run(TOKEN)