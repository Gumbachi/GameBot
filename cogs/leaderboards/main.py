import discord
from common.cfg import devguilds
from discord.commands import slash_command
from database import HallBotDB, Attribute

rpswins = HallBotDB("rpswins")
rpswins.__init__("wins")
# print(rpswins)

class stats():
    def __init__(self, player: discord.Member):
        self.player = player
        # self.rpswin = HallBotDB("rpswins")

    @property
    def embed(self):
        return discord.Embed(
            title=f"{self.player.name}'s Stats",
            description=self.getdata,
            color=discord.Color.orange()
        )

    @property
    def getdata(self):
        wins = [0, 100, 200]
        mmr = 1000
         
        # for win in self.rpswin.get_table("wins"):
        #     test = wins.append(self.rpswin.get_table("wins"))
        #     print(test)
        #     return len(wins)
        finalwins = len(wins)
        print(wins)
        print(len(wins))
        print(rpswins)

        return f"RPS Wins: {finalwins}\nRPS MMR: {mmr}"

class leaderboard(discord.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self.rpswins = HallBotDB("rpswins")

    @slash_command(name="stats", guild_ids=devguilds)
    async def startgame(self, ctx, player: discord.Member):
        """Check your stats"""
        # Loads data from the database.
        # self.rpswins.__loaddb()

        view = stats(player)
        await ctx.respond(embed=view.embed)

        # Saves data
        # self.rpswins.dumpdb()
                

def setup(bot):
    bot.add_cog(leaderboard(bot))

