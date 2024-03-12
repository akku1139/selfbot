import selfcord
from selfcord.ext import commands

import logging, json
log = logging.getLogger(__name__)

"""
{ユーザーid: レベル}
レベル1が最も高い
コマンド必要レベル >= ユーザーレベル
なら権限あり
"""
with open("data/users.json") as fp:
  users = json.load(fp)

class PermissionCog(commands.Cog, name = __name__):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    log.info("loaded")

  # @commands.command()
  # async def ping(self, ctx: commands.Context):
  #   await ctx.reply(f"ping: {self.bot.latency} sec")

async def setup(bot: commands.Bot):
  await bot.add_cog(PermissionCog(bot))

default_description = {
  "level": 1,
}

async def cmd_main(bot: commands.Bot, m: selfcord.Message):
  cmd = m.content[1:].split()[0]
  run_cmd = tuple(filter(lambda c: c.name == cmd, bot.commands))
  if not run_cmd:
    return

  desc = {
    **default_description,
    **json.loads(run_cmd[0].description)
  }

  # 権限を確認する
  # まずは存在しない場合除去
  if m.author.id not in users:
    return
  
  if desc["level"] >= users[m.author.id]:
    log.info(
      "Command executed\n" +
      f"by: {m.author.name} ({m.author.id})\n" +
      m.content
    )
    await bot.process_commands(m)
