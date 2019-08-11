import time
from datetime import datetime, timedelta
from kutana import Plugin
from db.events import *

plugin1 = Plugin(name="Register_event")


@plugin1.on_text("register_event")
async def _(message, env):
    data = env.body.split(',')
    message = data[0]
    date = datetime.strptime(data[1], "%d%m%Y").date()
    ev_id = int(round(datetime.now().timestamp() * 1000))
    insert_event(event_id=ev_id, event_date=date, event_message=message, event_is_upcoming=False)
    await env.reply("{}".format("Reg_event is successful"))


plugin2 = Plugin(name="Get_upcoming_events")


@plugin2.on_text("get_upcoming_events")
async def _(message, env):
    for e in get_all_events():
        if (e.event_date <= datetime.now() + timedelta(7)) and (e.event_date > datetime.now()):
            await env.reply(e.message, '/n', e.event_date)
    await env.reply('Это все')


plugins = [plugin1, plugin2]
