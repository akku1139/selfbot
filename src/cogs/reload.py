from selfcord.ext import commands

import logging
log = logging.getLogger("cogs.reload")

class ReloadCog(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    log.info("loaded")

  @commands.command(hidden=True)
  async def reload(self, ctx: commands.Context, cog: str = ""):
    match cog:
      case "":
        log.info("reload bot")
        await self.bot.close()

      case _:
        log.info(f"reload cogs.{cog}")
        await self.bot.reload_extension(f"cogs.{cog}")

async def setup(bot):
  await bot.add_cog(ReloadCog(bot))
