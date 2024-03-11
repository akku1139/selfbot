from discord.ext import commands

import logging
log = logging.getLogger("cogs.git")

import os

class MyCog(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    log.info("loaded")

  @commands.command()
  async def git(self, ctx: commands.Context, sub: str):
    match sub:
      case "pull":
        os.system("git pull")

async def setup(bot):
  await bot.add_cog(MyCog(bot))
