from kutana import Plugin
from vk.manager import vk_manager
from db.connection import *

plugin = Plugin(name="Send all", description="Send all users a message")

@plugin.on_startswith_text("send all")
async def _(message, env):
    for u in get_all_users():
        await vk_manager.send_message(env.body, u.id)
    await env.reply("{}".format("Success"))
