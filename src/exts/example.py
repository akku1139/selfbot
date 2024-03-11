from selfcord.ext import commands

import logging
log = logging.getLogger(__name__)

class ExampleCog(commands.Cog, name = __name__):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    log.info("loaded")

  # @commands.command()
  # async def ping(self, ctx: commands.Context):
  #   await ctx.reply(f"ping: {self.bot.latency} sec")

async def setup(bot: commands.Bot):
  await bot.add_cog(ExampleCog(bot))
