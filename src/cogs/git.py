from selfcord.ext import commands

import logging
log = logging.getLogger("cogs.git")

import subprocess

class GitCog(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    log.info("loaded")

  @commands.command(hidden=True)
  async def pull(self, ctx: commands.Context, sub: str):
    stdout = subprocess.run(["git","pull"], capture_output=True, text=True).stdout
    log.info("git pull")
    await ctx.send(f"```{stdout}```")

async def setup(bot):
  await bot.add_cog(GitCog(bot))
