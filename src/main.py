from selfcord.ext import commands
import selfcord

from dotenv import load_dotenv
load_dotenv()

from log_handler import DiscordWebHookHandler
import os, json, logging, asyncio
selfcord.utils.setup_logging(handler=DiscordWebHookHandler(), root=True)
log = logging.getLogger("main")

TOKEN = os.environ["DISCORD_TOKEN"]

bot = commands.Bot(command_prefix="^")

# 権限処理
"""
{ユーザーid: レベル}
TODO: レベル対応表作る
"""
with open("data/users.json") as fp:
  users = json.load(fp)

async def load_cogs():
  for cog in os.listdir("src/cogs/"):
    if cog.endswith(".py"):
      await bot.load_extension(f"cogs.{cog[:-3]}")
  log.info("cogs loaded")

@bot.event
async def on_message(m: selfcord.Message):
  # ガバガバ権限管理
  if m.author.id in users:
    await bot.process_commands(m)

if __name__ == "__main__":
  while True:
    asyncio.run(load_cogs())
    bot.run(TOKEN, log_handler=None)
