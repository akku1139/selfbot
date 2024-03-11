from dotenv import load_dotenv
load_dotenv()

import importlib, os, time, subprocess, logging
from log_handler import DiscordWebHookHandler
log = logging.getLogger("main")
log.addHandler(DiscordWebHookHandler())

import bot

if __name__ == "__main__":
  while True:
    load_dotenv()
    importlib.reload(bot)
    try:
      bot.bot.run(os.environ["DISCORD_TOKEN"], log_handler=None)
    except Exception as e:
      log.error(e)
      time.sleep(5)
      stdout = subprocess.run(["git","pull"], capture_output=True, text=True).stdout
      log.info("git pull\n"+stdout)
