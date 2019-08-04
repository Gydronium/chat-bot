import json

from kutana import Plugin

KEYBOARD_OBJECT_1 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {"type": "text", "payload": "schedule", "label": "Расписание"},
                "color": "primary",
            }
        ]
    ]
}
KEYBOARD_OBJECT_2 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {"type": "text", "payload": "schedule_tomorrow", "label": "Расписание на завтра"},
                "color": "primary",
            }
        ],
        [
            {
                "action": {"type": "text", "payload": "schedule_week", "label": "Расписание по дням недели"},
                "color": "primary",
            }
        ]
    ]
}
KEYBOARD_OBJECT_3 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {"type": "text", "payload": "monday", "label": "Понедельник"},
                "color": "primary",
            },
            {
                "action": {"type": "text", "payload": "tuesday", "label": "Вторник"},
                "color": "primary",
            },
            {
                "action": {"type": "text", "payload": "Wednesday", "label": "Среда"},
                "color": "primary",
            },

        ],
        [
            {
                "action": {"type": "text", "payload": "Thursday", "label": "Четверг"},
                "color": "primary",
            },
            {
                "action": {"type": "text", "payload": "Friday", "label": "Пятница"},
                "color": "primary",
            },
            {
                "action": {"type": "text", "payload": "Saturday", "label": "Суббота"},
                "color": "primary",
            },
        ]
    ],
}

# Keyboard that will be send to VKONTAKTE is a STRING!
KEYBOARD_STRING_1 = json.dumps(KEYBOARD_OBJECT_1)

# Plugins for sending keyboard.
plugin1 = Plugin(name="schedule", description="Keyboard for vkontakte")


@plugin1.on_text("schedule")
async def _(message, env):
    if env.manager_type != "vkontakte":
        await env.reply("This example works only for vk.com")
        return

    await env.reply("schedule", keyboard=KEYBOARD_STRING_1)


KEYBOARD_STRING_2 = json.dumps(KEYBOARD_OBJECT_2)

# Plugin for intercepting messages with payload.
plugin2 = Plugin(name="_Keyboard_listener1", priority=20)


@plugin2.on_text("Расписание")
async def _(message, env):
    payload = message.raw_update["object"].get("payload")

    if not payload:
        return "GOON"

    await env.reply("Keyboard", keyboard=KEYBOARD_STRING_2)


plugins = [plugin1, plugin2]
