from selfcord.ext import commands

import logging, typing
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

  async def send_bot_help(self, mapping):
    await self.get_destination().send("test help")

async def setup(bot: commands.Bot):
  bot.help_command = Help()

async def teardown(bot: commands.Bot):
  bot.help_command = None
