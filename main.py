"""Runs the discord bot"""
from pathlib import Path
from common.cfg import bot
import keys


@bot.listen()
async def on_ready():
    """Bot is now ready to rumble."""
    print("Ready to go")

# load extensions from the cogs dir
if __name__ == '__main__':
# .py files in cogs that are not cogs
ignored = [
    "cogs.music.buttons",
    "cogs.music.player",
    "cogs.music.song",
  "cogs.rpspvp.game"
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
