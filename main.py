"""Runs the discord bot"""
from pathlib import Path
from common.cfg import bot
import keys


@bot.listen()
async def on_ready():
    """Bot is now ready to rumble."""
    print("Ready to go")

# .py files in cogs that are not cogs
ignored = [
    "cogs.music.buttons",
    "cogs.music.player",
    "cogs.music.song",
    "cogs.tictactoe.game",
    "cogs.rpspvp.game",
    "cogs.connect_four.game",
    "cogs.connect_four.buttons",
]

if __name__ == '__main__':
    # find all .py files in ./cogs
    for ext in Path("./cogs").glob("**/*.py"):
        try:
            # extensions must be in cogs.general format
            ext = str(ext).replace("/", ".").replace("\\", ".")
            ext = ext[:-3]  # trim .py extension

            # skip ignored extensions
            if ext in ignored:
                continue

            bot.load_extension(ext)
            print(f"LOADED: {ext}")

        except Exception as e:
            print(f"Couldnt load {ext} because {e}")

# runs the bot. needs to stay at the bottom
bot.run(keys.BOT_TOKEN)
