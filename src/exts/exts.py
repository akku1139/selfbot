from selfcord.ext import commands

import logging
log = logging.getLogger(__name__)

class ReloadCog(commands.Cog, name = __name__):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    log.info("loaded")

  @commands.command(hidden=True)
  async def exts(self, ctx: commands.Context):
    await ctx.reply(str(list(self.bot.extensions.keys())))

  @commands.command(hidden=True)
  async def load(self, ctx: commands.Context, ext: str):
    await self.bot.load_extension(f"exts.{ext}")
    await ctx.reply(f"✅ exts.{ext} is loaded")

  @commands.command(hidden=True)
  async def unload(self, ctx: commands.Context, ext: str):
    await self.bot.unload_extension(f"exts.{ext}")
    await ctx.reply(f"🗑 exts.{ext} is unloaded")

  @commands.command(hidden=True)
  async def reload(self, ctx: commands.Context, ext: str = ""):
    match ext:
      case "":
        log.info("reload bot")
        await ctx.reply("restart bot")
        await self.bot.close()

      case _:
        await self.bot.reload_extension(f"exts.{ext}")
        await ctx.reply(f"🔄 reload exts.{ext}")
        log.info(f"reload exts.{ext}")

async def setup(bot):
  await bot.add_cog(ReloadCog(bot))
