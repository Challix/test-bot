# Docs: https://discordpy.readthedocs.io/en/latest/index.html
# Apps: https://discord.com/developers/applications

import discord
from discord.ext import commands
import random
import os

# bot = discord.Client()
bot = commands.Bot(command_prefix=".")


@bot.event
async def on_ready():
    print('{} is Online!'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))
    print('------')


@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency) * 1000} ms")


@bot.command(description='rolls a dice')
async def roll(ctx, dice):
    try:
        # 1d8
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Use #d# !!!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command()
async def react(ctx, emoji):
    # emoji = '\N{}'
    try:
        await ctx.message.add_reaction(emoji)
    except discord.HTTPException:
        pass


@bot.command()
async def test(ctx, *, arg):
    await ctx.send('argument: {}'.format(arg))


@bot.command()
async def embed(ctx):
    message = discord.Embed(title="Example", description='example text', color=discord.Colour.red())
    await ctx.send(embed=message)


@bot.command()
async def user(ctx):
    await ctx.send('user ID: <@!{}>'.format(ctx.message.author.id))
    await ctx.send('user ID: @everyone')


bot.run(os.environ.get('BOT_TOKEN'))
