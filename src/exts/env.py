from selfcord.ext import commands

from dotenv import load_dotenv

import logging
log = logging.getLogger(__name__)

class EnvCog(commands.Cog, name = __name__):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    log.info("loaded")

  @commands.command(hidden=True)
  async def env(self, ctx: commands.Context):
    load_dotenv()
    await ctx.send(f"reload env")

async def setup(bot: commands.Bot):
  await bot.add_cog(EnvCog(bot))
