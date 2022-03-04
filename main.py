"""Runs the discord bot"""
from pathlib import Path
from common.cfg import bot
import keys


@bot.listen()
async def on_ready():
    """Bot is now ready to rumble."""
    print("Ready to go")

ignored = [
    "cogs.rps.button"
    "cogs.rps.controller"
    "cogs.rps.model"
    "cogs.rps.rockpaperscissors"
    "cogs.rpspvp.game"
]

# load extensions from the cogs dir
if __name__ == '__main__':

    for ext in Path("./cogs").glob("**/*.py"):
        try:
            # parse string to correct format
            ext = str(ext).replace("/", ".").replace("\\", ".")
            ext = ext[:-3]  # trim .py extension

            if ext in ignored:
                continue

            bot.load_extension(ext)
            print(f"LOADED: {ext}")

        except Exception as e:
            print(f"Couldnt load {ext} because {e}")

# runs the bot. needs to stay at the bottom
bot.run(keys.BOT_TOKEN)
