import logging, os, urllib.request, json

class DiscordWebHookHandler(logging.Handler):
  webhook:str
  console:logging.StreamHandler
  def __init__(self):
    self.webhook = os.environ['LOG_WEBHOOK']
    self.console = logging.StreamHandler()
    super().__init__()

  def emit(self, record):
    try:
      self.console.emit(record)
      urllib.request.urlopen(urllib.request.Request(
        self.webhook,
        data=json.dumps({
          "content": "```js\n"+self.format(record)+"\n```"
        }).encode(),
        headers={
          "Content-Type": "application/json",
          "User-Agent": "DiscordBot (private use) Python-urllib/3.10",
        },
      )).close()
    except Exception:
      self.handleError(record)
