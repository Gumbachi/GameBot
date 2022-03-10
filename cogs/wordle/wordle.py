import discord
import requests
import random
from common.cfg import devguilds, Emoji
from discord.commands import slash_command


class Wordle(discord.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.word_length = 5
        self.letters = "abcdefghijklmnopqrstuvwxyz"
        self.words = requests.get("https://random-word-api.herokuapp.com/all")
        self.filtered = list(filter(lambda word: len(word) == self.word_length, self.words.json()))
        self.word = random.choice(self.filtered)
        print(self.word)

    @slash_command(name="wordle", guild_ids=devguilds)
    async def wordle(self, ctx, input_word):
        output_str = ""
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

            await ctx.respond(embed=output)
        return


def setup(bot):
    bot.add_cog(Wordle(bot))


"""while len(word) != 5:
    word = requests.get("https://random-word-api.herokuapp.com/word?number=1")
    word = word.json()[0]
    print(word)"""
