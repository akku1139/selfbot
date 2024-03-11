from selfcord.ext import commands

import logging
log = logging.getLogger("cogs.cogs")

class ReloadCog(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    log.info("loaded")

  @commands.command(hidden=True)
  async def exts(self, ctx: commands.Context):
    await ctx.reply(str(list(self.bot.extensions.keys())))

  @commands.command(hidden=True)
  async def load(self, ctx: commands.Context, cog: str):
    await self.bot.load_extension(f"exts.{cog}")
    await ctx.reply(f"✅ exts.{cog} is loaded")

  @commands.command(hidden=True)
  async def reload(self, ctx: commands.Context, cog: str = ""):
    match cog:
      case "":
        log.info("reload bot")
        await self.bot.close()

      case _:
        await self.bot.reload_extension(f"exts.{cog}")
        await ctx.reply(f"🔄 reload exts.{cog}")
        log.info(f"reload exts.{cog}")

async def setup(bot):
  await bot.add_cog(ReloadCog(bot))
