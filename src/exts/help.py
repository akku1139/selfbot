from selfcord.ext import commands

import logging
log = logging.getLogger(__name__)

class HelpCog(commands.Cog, name = __name__):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    log.info("loaded")

  @commands.command(description='{"level":50}')
  async def help(self, ctx: commands.Context):
    cmds = ""
    for cmd in self.bot.commands:
      if cmd.hidden:
        continue
      cmds += f"{cmd.name} "
      await ctx.reply(
      "Usage:	^command [option] ...\n"+
      "Commands:\n"+cmds+"\n"
      "License AGPLv3+: GNU AGPL version 3 or later <https://www.gnu.org/licenses/agpl-3.0.html>.\n"+
      "Source Code: https://github.com/akku1139/selfbot\n"
    )

async def setup(bot: commands.Bot):
  await bot.add_cog(HelpCog(bot))
