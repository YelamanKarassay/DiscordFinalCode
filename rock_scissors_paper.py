import discord,random
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def game(ctx,message):
    answer = message.lower()
    choices = ["rock","paper","scissors"]
    computers_answer =random.choice(choices)
    if answer not in choices:
        await ctx.send("Invalid option!")
    else:
        if computers_answer == answer:
            await ctx.send(f":regional_indicator_t: :regional_indicator_i: :regional_indicator_e: :grey_exclamation:     "
                           f"\n We picked {computers_answer} and you picked {answer}!")
            if answer == "rock":
                await ctx.send("https://facts.net/wp-content/uploads/2020/11/fight-4121142_1280.jpg")
            elif answer == "paper":
                await ctx.send("https://thumbs.dreamstime.com/b/two-teenager-slapping-hands-together-greeting-player-touching-hands-replace-sport-game-two-persons-clapping-hands-149222488.jpg")
            elif answer == "scissors":
                await ctx.send("https://live.staticflickr.com/2561/3829864148_98bbc822ff_b.jpg")



        if computers_answer == "rock":
            if answer == "paper":
               await ctx.send(f":regional_indicator_y: :regional_indicator_o: :regional_indicator_u:     "
                              f":regional_indicator_w: :regional_indicator_i: :regional_indicator_n: :grey_exclamation:      "
                              f"\nWe have {computers_answer} and your pick is {answer}!")
               await ctx.send("https://ichip.ru/blobimgs/uploads/2018/11/s55-beer-013_1-e1542283064790.jpg")

        if computers_answer == "paper":
            if answer == "rock":
                await ctx.send(f":regional_indicator_y: :regional_indicator_o: :regional_indicator_u:     "
                               f":regional_indicator_l: :regional_indicator_o: :regional_indicator_s: "
                               f":regional_indicator_e: :grey_exclamation:      "
                               f"\nWe have {computers_answer} and your pick is {answer}!")
                await ctx.send("https://ichip.ru/blobimgs/uploads/2018/11/s55-beer-013_1-e1542283064790.jpg")

        if computers_answer == "scissors":
            if answer == "rock":
                await ctx.send(f":regional_indicator_y: :regional_indicator_o: :regional_indicator_u:     :regional_indicator_w: "
                               f":regional_indicator_i: :regional_indicator_n: :grey_exclamation:      "
                               f"\nWe have {computers_answer} and your pick is {answer}!")
                await ctx.send("https://2i.by/wp-content/uploads/2021/12/af87e70f6d07932294add66a754435a0.jpg")

        if computers_answer == "rock" :
            if answer == "scissors":
                await ctx.send(f":regional_indicator_y: :regional_indicator_o: :regional_indicator_u:     "
                               f":regional_indicator_l: :regional_indicator_o: :regional_indicator_s: :regional_indicator_e: :grey_exclamation:      "
                               f"\nWe have {computers_answer} and your pick is {answer}!")
                await ctx.send("https://2i.by/wp-content/uploads/2021/12/af87e70f6d07932294add66a754435a0.jpg")

        if computers_answer == "paper":
            if answer == "scissors":
                await ctx.send(f":regional_indicator_y: :regional_indicator_o: :regional_indicator_u:     :regional_indicator_w: "
                               f":regional_indicator_i: :regional_indicator_n: :grey_exclamation:      "
                               f"\nWe have {computers_answer} and your pick is {answer}!")
                await ctx.send("https://ichip.ru/blobimgs/uploads/2018/11/s55-beer-012_1.jpg")

        if computers_answer == "scissors":
            if answer == "paper":
                await ctx.send(f":regional_indicator_y: :regional_indicator_o: :regional_indicator_u:     "
                               f":regional_indicator_l: :regional_indicator_o: :regional_indicator_s: :regional_indicator_e: :grey_exclamation:      "
                               f"\nWe have {computers_answer} and your pick is {answer}!")
                await ctx.send("https://ichip.ru/blobimgs/uploads/2018/11/s55-beer-012_1.jpg")

@game.error
async def _play_error(ctx, error):
    if isinstance(error,commands.MissingRequiredArgument):
        print("We Have An Error, Missing Bad Arguments")
        await ctx.send("Please Compelete Required Argument")
    elif isinstance(error,commands.BadArgument):
        print("We Have An Error, Bad Argument")
        await ctx.send("Bad Arguments")


client.run('OTI4MDQ5NjYzMjA5MjYzMTQ1.YdTHmg.smcyaU9DxGbhgkp6AlSX1WaM7Kk')