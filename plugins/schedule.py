import json

from kutana import Plugin, get_path

KEYBOARD_OBJECT_1 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {"type": "text", "payload": "10", "label": "Расписание"},
                "color": "primary",
            }
        ],
    ],
}

KEYBOARD_OBJECT_2 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {"type": "text", "payload": "11", "label": "Расписание на завтра"},
                "color": "primary",
            }
        ],
        [
            {
                "action": {"type": "text", "payload": "12", "label": "Расписание по дням недели"},
                "color": "primary",
            }
        ],
        [
            {
                "action": {"type": "text", "payload": "13", "label": "Расписание на сегодня"},
                "color": "primary",
            }
        ],
    ]
}

KEYBOARD_OBJECT_3 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {"type": "text", "payload": "21", "label": "Понедельник"},
                "color": "primary",
            },
            {
                "action": {"type": "text", "payload": "22", "label": "Вторник"},
                "color": "primary",
            },
            {
                "action": {"type": "text", "payload": "23", "label": "Среда"},
                "color": "primary",
            },

        ],
        [
            {
                "action": {"type": "text", "payload": "24", "label": "Четверг"},
                "color": "primary",
            },
            {
                "action": {"type": "text", "payload": "25", "label": "Пятница"},
                "color": "primary",
            },
            {
                "action": {"type": "text", "payload": "26", "label": "Суббота"},
                "color": "primary",
            },
        ]
    ],
}

# Keyboard that will be send to VKONTAKTE is a STRING!
KEYBOARD_STRING_1 = json.dumps(KEYBOARD_OBJECT_1)

# Plugins for sending keyboard.
plugin1 = Plugin(name="Schedule", description="Keyboard for vkontakte")


@plugin1.on_text("schedule")
async def _(message, env):
    await env.reply("Schedule", keyboard=KEYBOARD_STRING_1)


KEYBOARD_STRING_2 = json.dumps(KEYBOARD_OBJECT_2)
KEYBOARD_STRING_3 = json.dumps(KEYBOARD_OBJECT_3)

# Plugin for intercepting messages with payload.
plugin2 = Plugin(name="_Keyboard_listener", priority=10)


@plugin2.on_has_text()
async def _(message, env):
    payload = message.raw_update["object"].get("payload")

    if not payload:
        return "GOON"

    elif payload == "12":
        await env.reply("Выберите нужный вариант", keyboard=KEYBOARD_STRING_3)
    elif payload == "21":
        await env.reply("8:30 - 10:05  Еще рано"
                        "10:15 - 11:50  Вторую пару можно и пропустить"
                        "12:00 - 13:35  Пора бы и в столовую сходить"
                        "13:50 - 15:25  Тихий час"
                        "15:40 - 17:15  Пора бы и домой"
                        "17:25 - 19:00 Кто-то еще учится?"
                        "Академ"
                        "Армейка"
                        "Семья"
                        "Работа"
                        "Тебе уже 30 и ты не стал магом"
                        "Ты проиграл")
    elif payload == "22":
        await env.reply("8:30 - 10:05  Еще рано"
                        "10:15 - 11:50  Вторую пару можно и пропустить"
                        "12:00 - 13:35  Пора бы и в столовую сходить"
                        "13:50 - 15:25  Тихий час"
                        "15:40 - 17:15  Пора бы и домой"
                        "17:25 - 19:00 Кто-то еще учится?"
                        "Академ"
                        "Армейка"
                        "Семья"
                        "Работа"
                        "Кот использует тебя как подстилку"
                        "Ты проиграл")
    elif payload == "23":
        await env.reply("8:30 - 10:05  Еще рано"
                        "10:15 - 11:50  Вторую пару можно и пропустить"
                        "12:00 - 13:35  Пора бы и в столовую сходить"
                        "13:50 - 15:25  Тихий час"
                        "15:40 - 17:15  Пора бы и домой"
                        "17:25 - 19:00 Кто-то еще учится?"
                        "Академ"
                        "Армейка"
                        "Семья"
                        "Работа"
                        "Ты проиграл")
    elif payload == "24":
        await env.reply("8:30 - 10:05  Еще рано"
                        "10:15 - 11:50  Вторую пару можно и пропустить"
                        "12:00 - 13:35  Пора бы и в столовую сходить"
                        "13:50 - 15:25  Тихий час"
                        "15:40 - 17:15  Пора бы и домой"
                        "17:25 - 19:00 Кто-то еще учится?"
                        "Академ"
                        "Армейка"
                        "Семья"
                        "Работа"
                        "Ты проиграл")
    elif payload == "25":
        await env.reply("8:30 - 10:05  Еще рано"
                        "10:15 - 11:50  Вторую пару можно и пропустить"
                        "12:00 - 13:35  Пора бы и в столовую сходить"
                        "13:50 - 15:25  Тихий час"
                        "15:40 - 17:15  Пора бы и домой"
                        "17:25 - 19:00 Кто-то еще учится?"
                        "Академ"
                        "Армейка"
                        "Семья"
                        "Работа"
                        "Ты проиграл")
    elif payload == "26":
        await env.reply("8:30 - 10:05  Еще рано"
                        "10:15 - 11:50  Вторую пару можно и пропустить"
                        "12:00 - 13:35  Пора бы и в столовую сходить"
                        "13:50 - 15:25  Тихий час"
                        "15:40 - 17:15  Пора бы и домой"
                        "17:25 - 19:00 Кто-то еще учится?"
                        "Академ"
                        "Армейка"
                        "Семья"
                        "Работа"
                        "Ты проиграл")
    elif payload == "27":
        await env.reply("В воскресенье надо спать")

    await env.reply("Выберите нужный вариант", keyboard=KEYBOARD_STRING_2)


plugins = [plugin1, plugin2]
