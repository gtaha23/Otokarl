import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def save(ctx):
    if ctx.message.attachments:

        for attachment in ctx.message.attachments:

            file_name = attachment.filename

            file_url = attachment.url

            await attachment.save(f"./{attachment.filename}")

            await ctx.send(f"Saved the image to ./{attachment.filename}")

    else:
        await ctx.send("You forgot to upload the image :(")

bot.run("Token")