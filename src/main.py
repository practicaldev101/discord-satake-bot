import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import os
from dotenv import load_dotenv
from libs.api_controller import APIController
from cogs import usersCog

#asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

load_dotenv()

TOKEN = os.getenv("TOKEN")
API_URL = os.getenv("API_URL")



class Bot(commands.Bot):
    
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        super().__init__(command_prefix="?", intents=intents)
    
    async def setup_hook(self):
        await usersCog.setup(self)
        await self.tree.sync(guild=discord.Object(id=1023696007168540772))
        print("Synchronized")

bot = Bot()

@bot.event
async def on_ready():
    
    print("Bot activo")


@commands.has_permissions(administrator=True)
@bot.command("dmAll")
async def sendDMUsers(ctx, *, message):
    print(ctx.guild)
    embed_message = discord.Embed()
    embed_message.title = "Verificación"
    embed_message.description = message
    embed_message.color = discord.Colour.green()
    embed_message.add_field(name="Nota", value="*Ve al canal verificación y lee las instrucciones.*")
    embed_message.add_field(name="Servidor", value="https://discord.gg/M8s5eRY9Jv")
    embed_message.set_thumbnail(url="https://i.imgur.com/QyNXhw8.png")
    for member in ctx.guild.members:
        isVerified = False
        try:
            
            for rol in member.roles:
                if rol.id == 1021909078739533857 or rol.id == 1021573601645830224:
                    isVerified = True
            if isVerified == False:     
                dm_channel = await member.create_dm()
                await dm_channel.send("https://discord.gg/M8s5eRY9Jv", embed=embed_message)
                await ctx.channel.send('Enviado a ' + '<@' + str(member.id) + '>')
        except Exception as exc:
            pass
        


@bot.command()
async def test(ctx):

    await ctx.message.channel.typing()
    await asyncio.sleep(10)
    embed_message = discord.Embed()
    embed_message.title = "TU MADRE CARE VERGA"
    embed_message.description = "JAJA COME PITO"
    embed_message.color = discord.Colour.green()
    await ctx.message.channel.send(embed=embed_message)


bot.run(TOKEN)
