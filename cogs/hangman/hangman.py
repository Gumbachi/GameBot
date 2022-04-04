import discord
import random
from common.cfg import devguilds
from discord.commands import slash_command
from .game import Game


class hangman_game(discord.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.instances = {}

    @slash_command(name="hangman", guild_ids=devguilds)
    async def start_game(self, ctx):
        game = Game()
        self.instances[ctx.guild.id] = game
        await ctx.respond(f"Hangman game: {game.progress}")

    @discord.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        game = self.instances.get(message.guild.id)
        if not game:
            return
        if game.tries <= 0:
            return
        if len(message.content.lower()) == 1:
            if game.guess_letter(message.content.lower()):
                await message.reply(f"Correct! Current progress: {game.progress}\nRemaining tries: {game.tries}")
            else:
                await message.reply(f"Wrong. Current progress: {game.progress}\nRemaining tries: {game.tries}")

        if game.check_win():
            game.tries = 0
            await message.reply(f"You win!")


def setup(bot):
    bot.add_cog(hangman_game(bot))
