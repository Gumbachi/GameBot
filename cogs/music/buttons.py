"""Module holds classes for the buttons of the music player."""

import discord
from discord.enums import ButtonStyle
from common.cfg import EMOJI
from discord.ui import View, Button


class PlayButton(Button):
    def __init__(self):
        """The play button.
        """
        super().__init__(emoji=EMOJI.PLAY, style=ButtonStyle.gray)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("Song Paused")


class PauseButton(Button):
    def __init__(self):
        """The play button.
        """
        super().__init__(emoji=EMOJI.PAUSE, style=ButtonStyle.gray)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("Song Paused")


class SkipButton(Button):
    def __init__(self):
        """The play button.
        """
        super().__init__(emoji=EMOJI.SKIP, style=ButtonStyle.gray)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("Song Paused")


class RepeatOffButton(Button):
    def __init__(self):
        """The play button.
        """
        super().__init__(emoji=EMOJI.REPEAT, style=ButtonStyle.gray)

    async def callback(self, interaction: discord.Interaction):
        await interaction.message.edit(view=view)
        await interaction.response.send_message("Song Paused")


class RepeatButton(Button):
    def __init__(self):
        """The play button.
        """
        super().__init__(emoji=EMOJI.REPEAT, style=ButtonStyle.green)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("Song Paused")


class RepeatOneButton(Button):
    def __init__(self):
        """The play button.
        """
        super().__init__(emoji=EMOJI.REPEATONE, style=ButtonStyle.green)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("Song Paused")


def create_view(view: discord.ui.View = None):
    """Create the media player view."""

    # Create default view
    if not view:
        return View(PlayButton(), RepeatOffButton(), SkipButton(), timeout=None)
