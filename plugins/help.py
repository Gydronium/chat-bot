import json

from kutana import Plugin

KEYBOARD_OBJECT_1 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {"type": "text", "payload": "31", "label": "Date"},
                "color": "primary",
            },
            {
                "action": {"type": "text", "payload": "32", "label": "Echo"},
                "color": "primary",
            },
            {
                "action": {"type": "text", "payload": "33", "label": "Register_event"},
                "color": "primary",
            },

        ],
        [
            {
                "action": {"type": "text", "payload": "34", "label": "Get_upcoming_events"},
                "color": "primary",
            },
            {
                "action": {"type": "text", "payload": "35", "label": "Get_all_events"},
                "color": "primary",
            },
            {
                "action": {"type": "text", "payload": "36", "label": "Delete_old_events"},
                "color": "primary",
            },
        ],
        [
            {
                "action": {"type": "text", "payload": "37", "label": "Update_event_date"},
                "color": "primary",
            },
            {
                "action": {"type": "text", "payload": "38", "label": "Update_event_message"},
                "color": "primary",
            },
            {
                "action": {"type": "text", "payload": "39", "label": "Plugins"},
                "color": "primary",
            },
        ],
        [
            {
                "action": {"type": "text", "payload": "40", "label": "Register"},
                "color": "primary",
            },
            {
                "action": {"type": "text", "payload": "41", "label": "Schedule"},
                "color": "primary",
            },
            {
                "action": {"type": "text", "payload": "42", "label": "Send all"},
                "color": "primary",
            },
        ],
    ],
}

KEYBOARD_STRING_1 = json.dumps(KEYBOARD_OBJECT_1)

plugin1 = Plugin(name="Help", description="Keyboard for vkontakte")


@plugin1.on_text("help")
async def _(message, env):
    await env.reply("Help", keyboard=KEYBOARD_STRING_1)
