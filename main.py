import discord
from discord.ext import commands
import models as mdl

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

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

            await attachment.save(f"./{file_name}")

            await ctx.send(f"Saved the image to ./{file_name}")

    else:
        await ctx.send("You forgot to upload the image :(")

@bot.command()
async def detect(ctx):
    if ctx.message.attachments:

        for attachment in ctx.message.attachments:

            file_name = attachment.filename

            file_url = attachment.url

            await attachment.save(f"./{attachment.filename}")

            # Load the image
            img = mdl.Image.open(f"./{attachment.filename}")
            
            # Resize the image
            img = img.resize((224, 224))
            
            # Convert the image to a numpy array
            img_array = mdl.np.array(img)
            
            # Normalize the image array
            img_array = img_array / 255.0
            
            # Get the class with the highest probability
            class_id = mdl.np.argmax(mdl.prediction)
            class_names = ["0 Küresel Isınma", "1 Yangınlar", "2 Fabrika Atıkları"]
            file_type = class_names[class_id]

            if file_type == "0 Küresel Isınma":

                await ctx.send(f"{file_name}, this picture contains global warming, if this is in your area please call the authorities!")

            elif file_type == "1 Yangınlar":
                await ctx.send(f"{file_name}, this picture contains fire, if this is in your area immediately call the authorities!!")
            
            elif file_type == "2 Fabrika Atıkları":
                await ctx.send(f"{file_name}, this picture contains factory wastes, if this is in your area immedşately call the authorities!")

            else:
                await ctx.send(f"I couldn't detect {file_name} please try again")

    else:
        await ctx.send("You forgot to upload the image :(")

@bot.command(name = "custom_help")
async def custom_help(ctx):
    await ctx.send("Hello, If you need help, here are the commands:")
    await ctx.send("--> hello")
    await ctx.send("--> heh")
    await ctx.send("--> save")
    await ctx.send("--> detect")

bot.run("TOKEN")
