import discord
import random
from common.cfg import devguilds
from discord.commands import slash_command
from common.cfg import Emoji

class Magic8Ball(discord.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.responses = {
            1: "Most definitely.",
            2: "You can count on it.",
            3: "Without a doubt, yes.",
            4: "More than likely.",
            5: "Absolutely.",
            6: "I doubt it.",
            7: "I wouldn't count on it.",
            8: "Not in a million years.",
            9: "Concentrate and ask again.",
            10: "Not sure about that right now.",
            11: "I can't tell.",
            12: "Brian wills it.",
            13: "Could go either way.",
            14: "No, I don't think so.",
            15: "Perhaps.",
            16: "Please wait 5-7 business days and try again.",
            17: "Don't count on it.",
            18: "Survey says: no.",
            19: "Probably.",
            20: "As I see it, yes.",
            21: "Not a chance."
        }

    @slash_command(name="fortune", guild_ids=devguilds)
    async def fortune(self, ctx, question: str):
        result = random.randint(0, 21)
        await ctx.respond(f"{ctx.author.mention} asked: " + question + "\n" +Emoji.POOLBALL + ": " + self.responses[result])

def setup(bot):
    """Entry point for loading cogs. Required for all cogs"""
    bot.add_cog(Magic8Ball(bot))
