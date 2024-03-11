from selfcord.ext import commands

import logging
log = logging.getLogger(__name__)

import subprocess

class CountingCog(commands.Cog, name = __name__):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    log.info("loaded")

  @commands.command()
  async def num(self, ctx: commands.Context, n: int):
    await ctx.send(str(n))

async def setup(bot):
  await bot.add_cog(CountingCog(bot))
