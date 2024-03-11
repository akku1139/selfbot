from selfcord.ext import commands
import selfcord

from log_handler import DiscordWebHookHandler
import os, json, logging, asyncio, time, subprocess
selfcord.utils.setup_logging(handler=DiscordWebHookHandler(), root=True)
log = logging.getLogger("bot")

bot = commands.Bot(command_prefix="^")

# 権限処理
"""
{ユーザーid: レベル}
TODO: レベル対応表作る
"""
with open("data/users.json") as fp:
  users = json.load(fp)

@bot.event
async def setup_hook():
  for cog in os.listdir("src/cogs/"):
    if cog.endswith(".py"):
      await bot.load_extension(f"cogs.{cog[:-3]}")
  log.info("cogs loaded")

@bot.event
async def on_message(m: selfcord.Message):
  # ガバガバ権限管理
  if str(m.author.id) in users:
    await bot.process_commands(m)
