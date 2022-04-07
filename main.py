"""Runs the discord bot"""
from common.cfg import bot
import keys


@bot.listen()
async def on_ready():
    """Bot is now ready to rumble."""
    print("Ready to go")

# load extensions from the cogs dir
# .py files in cogs that are not cogs
extensions = [
    "cogs.general",
    "cogs.blackjack.blackjack"
]

if __name__ == '__main__':
    # find all .py files in ./cogs
    for ext in extensions:
        try:
            bot.load_extension(ext)
            print(f"LOADED: {ext}")

        except Exception as e:
            print(f"Couldnt load {ext} because {e}")

# runs the bot. needs to stay at the bottom
bot.run(keys.BOT_TOKEN)
