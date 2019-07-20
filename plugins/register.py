from kutana import Plugin
from db.connection import *

plugin = Plugin(name="Register")

@plugin.on_text("register")
async def _(message, env):
    User.insert(id=message.from_id, is_boss=True).execute()
    await env.reply("{}".format("Registration successful"))