import discord
from common.cfg import devguilds
from discord.commands import slash_command
import random

class GuessMe(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="guess", guild_ids=devguilds)
    async def startgame(self, ctx, min: int, max: int):
        correct_number = random.randint(min, max)

        emb = discord.Embed(title=f'Pick a number Between {min} and {max}', color=discord.Color.blue())

        message = await ctx.send(embed=emb)

        response = await self.bot.wait_for('message')
        guess = int(response.content)

        if guess == correct_number:
            winEmbed = discord.Embed(title=f'You Picked The Correct Number!', color=discord.Color.green(), description=f'You picked {guess} and Won!')
            await message.edit(embed=winEmbed)
        
        else:
            loseEmbed = discord.Embed(title=f'Sorry, You Picked The Wrong Number', color=discord.Color.red(), description=f'You Picked {guess} and the Correct Number was {correct_number}')
            await message.edit(embed=loseEmbed)
                

def setup(bot):
    bot.add_cog(GuessMe(bot))