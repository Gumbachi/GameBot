import discord
from common.cfg import devguilds
from discord.commands import slash_command


class GeneralCommands(discord.Cog):
    """Handles simple commands and listeners."""

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="howdy", guild_ids=devguilds)
    async def howdy(self, ctx):
        """Command to check if bot is alive or if you need a friend."""
        await ctx.respond(f"Howdy {ctx.author.mention}!")

    @discord.Cog.listener()
    async def on_message(self, message):
        """Called for every message sent that the bot can see"""

        # Ignore bot messages
        if message.author.bot:
            return

        if message.content.lower() == "brian":
            await message.reply("hall")
        if message.content.lower() == "hall":
            await message.reply("brian")


    @discord.Cog.listener()
    async def on_guild_join(self, guild):
        """Bot has joined a guild."""
        print(f"Joined {guild.name}")

    @discord.Cog.listener()
    async def on_guild_remove(self, guild):
        """Bot is kicked/removed."""
        print(f"Left {guild.name}")


def setup(bot):
    """Entry point for loading cogs. Required for all cogs"""
    bot.add_cog(GeneralCommands(bot))
