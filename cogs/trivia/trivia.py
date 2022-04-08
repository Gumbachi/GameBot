import discord
from common.cfg import devguilds
from discord.commands import slash_command
from .game import Game

class Trivia(discord.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.instances = {}

    @slash_command(name="trivia", guild_ids=devguilds)
    async def start_game(self, ctx):
        game = Game()
        self.instances[ctx.guild.id] = game
        await ctx.respond(f"{game.question[0]}", view=game.view)


def setup(bot):
    bot.add_cog(Trivia(bot))
