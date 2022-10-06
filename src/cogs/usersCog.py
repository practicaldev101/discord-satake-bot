from pydoc import describe
import discord
from discord.ext import commands
from discord import app_commands
from libs.api_controller import APIController
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")


class Users(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
        
    
    @commands.has_permissions(administrator=True)   
    @commands.hybrid_group(name="user", with_app_command=True)
    async def users(self, ctx: commands.Context):
        if ctx.invoked_subcommand is None:
            print(ctx.guild.id)
            await ctx.send("> Comando inválido de users")
        print(API_URL)

    @users.command(name="all")
    async def all(self, ctx: commands.Context):
        api = APIController(API_URL)
        response = await api.authUser({
            "username": "PracticalProgrammer", 
            "password":"test123"
            })

        print(response)
        
        api.token = response["token"]
        users = await api.getUsers()
        
        for user in users["result"]:
            embed_message = discord.Embed(title=user["robloxNickname"])
            embed_message.color = discord.Colour.green()
            embed_message.add_field(name="Nombre", value=user["username"])
            embed_message.add_field(name="Edad", value=str(user["yearsOld"]))
            embed_message.add_field(name="Género", value=str(user["gender"]))
            await ctx.channel.send(embed=embed_message)
            
            
    @users.command()
    #@app_commands.choices(values=["rand_c"])
    async def search(self, ctx: commands.Context, keyword: str):
        await ctx.send(keyword)
        
async def setup(bot):
        await bot.add_cog(Users(bot), guilds=[discord.Object(id=1023696007168540772)])
        await bot.tree.sync()
