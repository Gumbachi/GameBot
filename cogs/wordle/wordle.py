import discord
import requests
import random
import database
from datetime import date
from common.cfg import devguilds, Emoji
from discord.commands import slash_command


class Wordle(discord.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.word_length = 5
        self.date = date.today().strftime("%d/%m/%Y")
        self.wordle_db = database.HallBotDB("WordleDB")
        self.wordle_db.create_table("Players", ["Name", "DateGuessed"])
        self.letters = "abcdefghijklmnopqrstuvwxyz"
        self.words = requests.get("https://random-word-api.herokuapp.com/all")
        self.filtered = list(filter(lambda word: len(word) == self.word_length, self.words.json()))
        self.word = random.choice(self.filtered)
        print(self.word)

    @slash_command(name="wordle", guild_ids=devguilds, pass_context=True)
    async def wordle(self, ctx, input_word):
        self.date = date.today().strftime("%d/%m/%Y")
        output_str = ""
        for attb in self.wordle_db.get_table("Players").attributes:
            if str(ctx.author) in attb.values:
                if str(self.date) in attb.values:
                    output_str += "You have already tried to guess the word today."
                    output = discord.Embed(title=output_str, color=discord.Color.blue())
                    await ctx.respond(embed=output)
                    return

        if len(input_word) != self.word_length:
            output_str += "Input a " + str(self.word_length) + " letter long word."
            output = discord.Embed(title=output_str, color=discord.Color.blue())
            await ctx.respond(embed=output)
        else:
            for i in range(0, self.word_length):
                if self.word[i] == input_word[i]:
                    output_str += Emoji.GREEN_SQUARE
                elif input_word[i] in self.word:
                    output_str += Emoji.YELLOW_SQUARE
                else:
                    output_str += Emoji.WHITE_SQUARE
                    self.letters = self.letters.replace(input_word[i], "")
            str_input = str(input_word)
            format_input = ""
            for letter in str_input:
                format_input += " " + letter + "  "
            output_str += "\n" + format_input + "\nYour remaining letters are " + self.letters
            output = discord.Embed(title=output_str, color=discord.Color.blue())

            self.wordle_db.get_table("Players").add_attribute(database.Attribute([str(ctx.author), str(self.date)]))
            print(self.wordle_db)

            await ctx.respond(embed=output)
        self.wordle_db.dumpdb()
        return


def setup(bot):
    bot.add_cog(Wordle(bot))


"""while len(word) != 5:
    word = requests.get("https://random-word-api.herokuapp.com/word?number=1")
    word = word.json()[0]
    print(word)"""
