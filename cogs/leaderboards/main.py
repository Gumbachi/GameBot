import discord
from common.cfg import devguilds
from discord.commands import slash_command

class leaderboard(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="leaderboard", guild_ids=devguilds)
    async def startgame(self, ctx, player: discord.Member):
        await ctx.send("Test")
                

def setup(bot):
    bot.add_cog(leaderboard(bot))

