import discord
import random
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hi!")

@bot.command()
async def bye(ctx):
    await ctx.send("\\U0001f642")

@bot.command()
async def passgen(ctx, length: int = 10):
    password = gen_pass(length)
    await ctx.send(password)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)  
    await message.channel.send(message.content)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))
    
bot.run("Aqui va tu codigo")
