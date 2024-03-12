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

  async def send_bot_help(self, 
    mapping: typing.Mapping[typing.Optional[commands.Cog], list[commands.Command]]
  ):
    await self.get_destination().send(
      "```"+
      "Usage: ^command [option] ...\n"+
      # "Commands:\n"+cmds+"\n"
      "License AGPLv3+: GNU AGPL version 3 or later <https://www.gnu.org/licenses/agpl-3.0.html>.\n"+
      "Source Code: https://github.com/akku1139/selfbot\n```"
    )

async def setup(bot: commands.Bot):
  bot.help_command = Help()

async def teardown(bot: commands.Bot):
  bot.help_command = None
