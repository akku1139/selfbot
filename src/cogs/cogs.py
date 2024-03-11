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
  async def cogs(self, ctx: commands.Context, cog: str):
    await ctx.reply(str(self.bot.cogs.keys))

  @commands.command(hidden=True)
  async def load(self, ctx: commands.Context, cog: str):
    await self.bot.load_extension(f"cogs.{cog}")
    await ctx.reply(f"✅ cogs.{cog} is loaded")

  @commands.command(hidden=True)
  async def reload(self, ctx: commands.Context, cog: str = ""):
    match cog:
      case "":
        log.info("reload bot")
        await self.bot.close()

      case _:
        await self.bot.reload_extension(f"cogs.{cog}")
        await ctx.reply(f"🔄 reload cogs.{cog}")
        log.info(f"reload cogs.{cog}")

async def setup(bot):
  await bot.add_cog(ReloadCog(bot))
