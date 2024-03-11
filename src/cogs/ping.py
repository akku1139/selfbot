from selfcord.ext import commands

import logging
log = logging.getLogger("cogs.example")

class ExampleCog(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    log.info("loaded")

  @commands.command()
  async def ping(self, ctx: commands.Context):
    await ctx.send(f"ping: {self.bot.latency} sec")

async def setup(bot):
  await bot.add_cog(ExampleCog(bot))
