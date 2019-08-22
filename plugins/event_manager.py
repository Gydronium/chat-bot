import time
from datetime import datetime, timedelta
from kutana import Plugin
from db.events import *

plugin1 = Plugin(name="Register_event")


@plugin1.on_startswith_text("register_event")
async def _(message, env):
    try:
        data = env.body.split(',')
        message1 = data[0]
        date = data[1]
        ev_id = int(round(datetime.now().timestamp()/10))
        insert_event(event_id=ev_id, event_date=date, event_message=message1, event_is_upcoming=False)
        await env.reply("{}".format("Reg_event is successful"))
    except:
        await env.reply("{}".format("There was an error"))


plugin2 = Plugin(name="Get_upcoming_events")


@plugin2.on_text("get_upcoming_events")
async def _(message, env):
    for e in get_all_events():
        if (e.date <= datetime.now().date() + timedelta(7)) and (e.date > datetime.now().date()):
            await env.reply("{0} \n {1}".format(e.message, e.date))
    await env.reply('Это все')


plugin3 = Plugin(name="Get_all_events")


@plugin3.on_text("get_all_events")
async def _(message, env):
    for e in get_all_events():
        await env.reply("{0} \n {1} \n {2}".format(e.message, e.date, e.id))
    await env.reply('Это действительно все')


plugin4 = Plugin(name="Delete_old_events")


@plugin4.on_text("delete_old_events")
async def _(message, env):
    for e in get_all_events():
        if e.date < datetime.now().date():
            User1.delete_by_id(e)
    await env.reply('Старые события удалены')


plugin5 = Plugin(name="Update_event_date")


@plugin5.on_startswith_text("update_event_date")
async def _(message, env):
    try:
        data = env.body.split(',')
        ev_id = data[0]
        date = data[1]
        update_event(ev_id, '0', date, False, True)
        await env.reply('Дата события обновлена')
    except:
        await env.reply('There was an error')


plugin6 = Plugin(name="Update_event_message")


@plugin6.on_startswith_text("update_event_message")
async def _(message, env):
    try:
        data = env.body.split(',')
        ev_id = data[0]
        message = data[1]
        update_event(ev_id, message, 0, True, False)
        await env.reply('Сообщение события обновлено')
    except:
        await env.reply('There was an error')

plugins = [plugin1, plugin2, plugin3, plugin4, plugin5, plugin6]
