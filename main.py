"""Runs the discord bot"""
from pathlib import Path
from common.cfg import bot
import keys


@bot.listen()
async def on_ready():
    """Bot is now ready to rumble."""
    print("Ready to go")


extensions = [
    "cogs.general",
    "cogs.minesweeper.minesweeper"
]

if __name__ == '__main__':
    for ext in extensions:
        try:
            bot.load_extension(ext)
            print(f"LOADED: {ext}")
        except Exception as e:
            print(f"Couldnt load {ext} because {e}")

# runs the bot. needs to stay at the bottom
bot.run(keys.BOT_TOKEN)
