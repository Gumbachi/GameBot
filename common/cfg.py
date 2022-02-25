"""This file is for storing global vars"""
import discord
from discord import Activity, ActivityType
from discord.enums import Status

bot = discord.Bot(
    description="Multi-purpose chadbot",
    activity=Activity(name="Just Woke Up", type=ActivityType.playing),
    status=Status.dnd,
    owner_id=128595549975871488
)

# The ids of the dev testing servers
devguilds = [944304184335945759]

class EMOJI:
    ROCK = "\U0001faa8"
    PAPER = "\U0001f4c3"
    SCISSORS = "\u2702"
