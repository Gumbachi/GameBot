import discord
from common.cfg import devguilds
from discord.commands import slash_command
from .game import PVPGame


class RPSpvp(discord.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.instances = {}

    @slash_command(name="rps", guild_ids=devguilds)
    async def startgame(self, ctx, opponent: discord.Member):
        game_instance = PVPGame(ctx.author, opponent)
        self.instances[ctx.guild.id] = game_instance
        await ctx.respond(embed=game_instance.embed, view=game_instance.controller)

def setup(bot):
    bot.add_cog(RPSpvp(bot))