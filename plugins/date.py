from kutana import Plugin
import datetime

plugin = Plugin(name="Date", description="Reply with send message")

@plugin.on_startswith_text("plugin")
async def _(message, env):
    now = datetime.datetime.now()
    await env.reply(now.strftime("%d-%m-%Y %H:%M"))
