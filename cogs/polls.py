from time import time
from typing import Optional
import discord
from common.cfg import devguilds
from discord.commands import slash_command
from discord import ButtonStyle, Embed
from common.cfg import Emoji


class YesButton(discord.ui.Button):
    def __init__(self, poll):
        super().__init__(style=ButtonStyle.green, emoji=Emoji.CHECKMARK)
        self.poll = poll

    async def callback(self, interaction: discord.Interaction):

        if interaction.user in self.poll.yes:
            return

        if interaction.user in self.poll.no:
            self.poll.no.remove(interaction.user)

        self.poll.yes.add(interaction.user)
        await interaction.response.edit_message(embed=self.poll.embed)


class NoButton(discord.ui.Button):
    def __init__(self, poll):
        super().__init__(style=ButtonStyle.red, emoji=Emoji.CROSS)
        self.poll = poll

    async def callback(self, interaction: discord.Interaction):

        if interaction.user in self.poll.no:
            return

        if interaction.user in self.poll.yes:
            self.poll.yes.remove(interaction.user)

        self.poll.no.add(interaction.user)
        await interaction.response.edit_message(embed=self.poll.embed)


class Poll:
    def __init__(self, question, timeout) -> None:
        self.question = question
        self.timeout = timeout
        self.yes = set()
        self.no = set()

    @property
    def embed(self):
        return discord.Embed(
            title=self.question,
            description=f"YES: {len(self.yes)}\nNO: {len(self.no)}\nTOTAL VOTES: {len(self.voters)}",
            color=discord.Color.blue()
        )

    @property
    def controller(self):
        return discord.ui.View(YesButton(self), NoButton(self), timeout=self.timeout)

    @property
    def voters(self):
        return self.yes.union(self.no)


class Polls(discord.Cog):
    """Handles polls"""

    def __init__(self, bot):
        self.bot = bot
        self.polls = {}

    def get_poll(self, message):
        return self.polls.get(message.id)

    @slash_command(name="poll", guild_ids=devguilds)
    async def poll(self, ctx, question: str, timeout: Optional[int] = 0):
        """Command to check if bot is alive or if you need a friend."""

        poll = Poll(question, timeout)
        message = await ctx.respond(embed=poll.embed, view=poll.controller)
        self.polls[message.id] = poll


def setup(bot):
    """Entry point for loading cogs. Required for all cogs"""
    bot.add_cog(Polls(bot))
