from selfcord.ext import commands

from dotenv import load_dotenv

import logging
log = logging.getLogger(__name__)

class AICog(commands.Cog, name = __name__):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    log.info("loaded")

  @commands.command()
  async def gemini(self, ctx: commands.Context):
    
    await ctx.send(f"準備中")

async def setup(bot: commands.Bot):
  await bot.add_cog(AICog(bot))
