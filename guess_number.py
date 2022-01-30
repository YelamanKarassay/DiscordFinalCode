import math
import random

from discord.ext import commands

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command(name='play')
async def play(ctx):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.message.channel

    number = random.randint(1, 100)
    # await ctx.send(number)
    await ctx.send(':regional_indicator_i:'
                   '     :regional_indicator_h: :regional_indicator_a: :regional_indicator_v: :regional_indicator_e:'
                   '     :regional_indicator_a:     :regional_indicator_n: :regional_indicator_u: :regional_indicator_m: '
                   ':regional_indicator_b: :regional_indicator_e: :regional_indicator_r:'
                   '     :regional_indicator_i: :regional_indicator_n:'
                   '     :regional_indicator_m: :regional_indicator_i: :regional_indicator_n: :regional_indicator_d:'
                   '     :regional_indicator_b: :regional_indicator_e: :regional_indicator_t: :regional_indicator_w: '
                   ':regional_indicator_e: :regional_indicator_e: :regional_indicator_n:     :one:'
                   '     :regional_indicator_a: :regional_indicator_n: :regional_indicator_d:'
                   '     :one: :zero: :zero: ,     :regional_indicator_g: :regional_indicator_u: :regional_indicator_e:'
                   ' :regional_indicator_s: :regional_indicator_s:     ')

    for i in range(0, 7):
        guess = await client.wait_for('message', check=check)

        if guess.content == number:
            await ctx.send(':regional_indicator_y: :regional_indicator_o: :regional_indicator_u:'
                           '     :regional_indicator_g: :regional_indicator_o: :regional_indicator_t:'
                           '     :regional_indicator_i: :regional_indicator_t: :grey_exclamation:     ')

        elif guess.content < str(number):
            await ctx.send(':regional_indicator_h: :regional_indicator_i: :regional_indicator_g: :regional_indicator_h:'
                           ' :regional_indicator_e: :regional_indicator_r: :grey_exclamation:     ')

        elif guess.content > str(number):
            await ctx.send(':regional_indicator_l: :regional_indicator_o: :regional_indicator_w: :regional_indicator_e:'
                           ' :regional_indicator_r: :grey_exclamation:     ')


        else:
            return  # Or something else
        if math.isclose(int(guess.content), number, rel_tol=3, abs_tol=1):
            await ctx.send(
                ":regional_indicator_n: :regional_indicator_e: :regional_indicator_a: :regional_indicator_r: :grey_exclamation:     ")

    else:
        await ctx.send(":regional_indicator_y: :regional_indicator_o: :regional_indicator_u:"
                       "     :regional_indicator_l: :regional_indicator_o: :regional_indicator_s: :regional_indicator_t: ,"
                       "     :regional_indicator_t: :regional_indicator_y: :regional_indicator_p: :regional_indicator_e:"
                       "     :grey_exclamation: :regional_indicator_p: :regional_indicator_l: :regional_indicator_a: :regional_indicator_y:"
                       "     :regional_indicator_t: :regional_indicator_o:     :regional_indicator_p: :regional_indicator_l:"
                       " :regional_indicator_a: :regional_indicator_y::regional_indicator_a: :regional_indicator_g: "
                       ":regional_indicator_a: :regional_indicator_i: :regional_indicator_n: :record_button:         ")


client.run('OTI4MDQ5NjYzMjA5MjYzMTQ1.YdTHmg.smcyaU9DxGbhgkp6AlSX1WaM7Kk')
