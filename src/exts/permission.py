import selfcord
from selfcord.ext import commands

import logging, json
log = logging.getLogger(__name__)

"""
{
  ユーザーid: {
    "level": "レベル",
    "name"?: "Discordユーザー名",
    "nick"?: "ニックネーム",
    "desc"?: "理由",
  }
}

レベル1が最も高い
コマンド必要レベル >= ユーザーレベル
なら権限あり

権限レベルリスト
1: akku
10: 一般ユーザー
50: 現在最低権限
"""

users = {}
with open("data/users.json") as fp:
  users = json.load(fp)

def save_users():
  global users
  with open("data/users.json", "w") as fp:
    json.dump(users, fp)

  with open("data/users.json") as fp:
    users = json.load(fp)

class PermissionCog(commands.Cog, name = __name__):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    log.info("loaded")

  @commands.command(hidden=True)
  async def user_add(self, ctx: commands.Context,
    target: int, nick: str = "", desc = "",
  ):
    if not (user := self.bot.get_user(target)):
      await ctx.reply("ユーザーが見つからなかった")
      return

    users[str(user.id)] = {
      "level": 10,
      "name": user.name,
      "nick": nick,
      "desc": desc,
    }
    save_users()
    await ctx.reply(f"<@{user.id}> にレベル10の権限を追加")

    @commands.command(hidden=True)
    async def user_del(self, ctx: commands.Context, target: int):
      users.pop(str(target))
      save_users()
      await ctx.reply(f"<@{target}> の権限を剥奪")

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
    **json.loads(run_cmd[0].description or "{}")
  }

  # 権限を確認する
  # まずは存在しない場合除去
  if str(m.author.id) not in users:
    return
  
  if desc["level"] >= users[str(m.author.id)]["level"]:
    log.info(
      "Command executed\n" +
      f"by: {m.author.name} ({m.author.id})\n" +
      m.content
    )
    await bot.process_commands(m)

async def setup(bot: commands.Bot):
  await bot.add_cog(PermissionCog(bot))
