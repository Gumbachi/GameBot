import random
import discord
from common.cfg import devguilds, Emoji
from discord.commands import slash_command


class flip(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="flipcoin", guild_ids=devguilds)
    async def flipCoin(self, ctx):
        side = random.randint(0, 1)
        if side == 0:
            await ctx.respond(Emoji.HEADS)
        else:
            await ctx.respond(Emoji.TAILS)
        return


def setup(bot):
    bot.add_cog(flip(bot))
