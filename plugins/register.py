from kutana import Plugin
from db.connection import *

plugin = Plugin(name="Register")

@plugin.on_text("register")
async def _(message, env):
    insert_user(user_id=message.from_id, user_is_boss=True)
    await env.reply("{}".format("Registration successful"))
