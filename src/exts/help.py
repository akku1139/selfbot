from selfcord.ext import commands

import logging
log = logging.getLogger(__name__)

class Help(commands.HelpCommand):
  def __init__(self):
    super().__init__(
      show_hidden=False,
      command_attrs={
        "brief": "show this help",
        "description": '{"level":50}',
      }
    )

async def setup(bot: commands.Bot):
  bot.help_command = Help()

async def teardown(bot: commands.Bot):
  bot.help_command = None
