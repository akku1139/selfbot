from selfcord.ext import commands

import logging
log = logging.getLogger("cogs.help")

class Help(commands.HelpCommand):
  def __init__(self):
    super().__init__(
      show_hidden=False, # 隠しコマンドを表示するかどうか
    )

async def setup(bot):
  bot.help_command = Help()
