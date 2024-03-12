from selfcord.ext import commands
import selfcord

from dotenv import load_dotenv
load_dotenv()

from log_handler import DiscordWebHookHandler
import os, logging, asyncio, subprocess
selfcord.utils.setup_logging(handler=DiscordWebHookHandler(), root=True)
log = logging.getLogger("main")

TOKEN = os.environ["DISCORD_TOKEN"]

bot = commands.Bot(command_prefix="^")

@bot.event
async def setup_hook():
  for cog in os.listdir("src/exts/"):
    if cog.endswith(".py"):
      await bot.load_extension(f"exts.{cog[:-3]}")
  log.info("exts loaded")

replaces = {
  "な": "にゃ",
  "https://x.com/": "https://fxtwitter.com/",
  "https://twitter.com/": "https://fxtwitter.com/",
}

@bot.event
async def on_message(m: selfcord.Message):
  if m.author.id == bot.user.id:
    c = m.content
    for word in replaces:
      if word in c:
        c = c.replace(word, replaces[word])
    if m.content != c:
      await m.edit(content=c)

  if m.content.startswith("^"):
    if(perm := bot.extensions.get("exts.permission")):
      getattr(perm, "cmd_main")(bot, m)

if __name__ == "__main__":
  try:
    bot.run(TOKEN, log_handler=None)
  except Exception as e:
    log.error(e)
    stdout = subprocess.run(["git","pull"], capture_output=True, text=True).stdout
    log.info("git pull\n"+stdout)
