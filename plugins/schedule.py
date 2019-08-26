import json, datetime

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

    if payload == "11":
        if datetime.datetime.today().isoweekday() == 1:
            payload = "22"
        elif datetime.datetime.today().isoweekday() == 2:
            payload = "23"
        elif datetime.datetime.today().isoweekday() == 3:
            payload = "24"
        elif datetime.datetime.today().isoweekday() == 4:
            payload = "25"
        elif datetime.datetime.today().isoweekday() == 5:
            payload = "26"
        elif datetime.datetime.today().isoweekday() == 6:
            payload = "27"
        elif datetime.datetime.today().isoweekday() == 7:
            payload = "21"
    if payload == "13":
        if datetime.datetime.today().isoweekday() == 1:
            payload = "21"
        elif datetime.datetime.today().isoweekday() == 2:
            payload = "22"
        elif datetime.datetime.today().isoweekday() == 3:
            payload = "23"
        elif datetime.datetime.today().isoweekday() == 4:
            payload = "24"
        elif datetime.datetime.today().isoweekday() == 5:
            payload = "25"
        elif datetime.datetime.today().isoweekday() == 6:
            payload = "26"
        elif datetime.datetime.today().isoweekday() == 7:
            payload = "27"

    if not payload:
        return "GOON"

    if payload == "12":
        await env.reply("Выберите нужный вариант", keyboard=KEYBOARD_STRING_3)
    elif payload == "21":
        await env.reply('Понедельник \n'
                        # '8:30 - 10:05  Еще рано \n'
                        # '10:15 - 11:50  Вторую пару можно и пропустить \n'
                        # '12:00 - 13:35  Пора бы и в столовую сходить \n'
                        # '13:50 - 15:25  Тихий час \n'
                        # '15:40 - 17:15  Пора бы и домой \n'
                        # '17:25 - 19:00 Кто-то еще учится? \n'
                        # 'Академ \n'
                        # 'Армейка \n'
                        # 'Семья \n'
                        # 'Работа \n'
                        # 'Тебе уже 30 и ты не стал магом \n'
                        # 'Ты проиграл \n')
                        'Чс \n'
                        '8:30 - 10:05 ОПМиРТС(семинар) Филимонов 507м \n'
                        '10:15 - 11:50 ОПМиРТС(лекция) Бошляков 505м \n'
                        '12:00 - 13:35 ОЭИМиРТС(лекция) Ипполитова 505м \n'
                        'Зн \n'
                        '8:30 - 10:05 БЖД 507м \n'
                        '10:15 - 11:50 ОПМиРТС(лекция) Бошляков 505м \n'
                        '12:00 - 13:35 ТАУ(семинар) Ипполитова 505м \n'
                        )
    elif payload == "22":
        await env.reply('Вторник \n'
                        # '8:30 - 10:05  Еще рано \n'
                        # '10:15 - 11:50  Вторую пару можно и пропустить \n'
                        # '12:00 - 13:35  Пора бы и в столовую сходить \n'
                        # '13:50 - 15:25  Тихий час \n'
                        # '15:40 - 17:15  Пора бы и домой \n'
                        # '17:25 - 19:00 Кто-то еще учится? \n'
                        # 'Академ \n'
                        # 'Армейка \n'
                        # 'Семья \n'
                        # 'Работа \n'
                        # 'Кот использует тебя как подстилку \n'
                        # 'Ты проиграл \n')
                        'Чс \n'
                        '8:30 - 10:05 Гидравлические следящие приводы СРТС (лекция) Калинин каф \n'
                        '10:15 - 11:50 Электрические следящие приводы СРТС (лекция) Буторин каф \n'
                        '12:00 - 13:35 Экономика (семинар) Лебедев 504м \n'
                        'Зн \n'
                        '8:30 - 10:05 Гидравлические следящие приводы СРТС (лекция) Калинин каф \n'
                        '10:15 - 11:50 Электрические следящие приводы СРТС (лекция) Буторин каф \n')
    elif payload == "23":
        await env.reply('Среда \n'
                        'Чс \n'
                        '8:30 - 10:05 Методы оптимизации (лекция) Романова 405м \n'
                        '10:15 - 11:50 Микропроцессорные устройства РТС СН (лекция) Рассадкин 225м \n'
                        '12:00 - 13:35 Технология производства СРТС (лекция+семинар) Круглов 115м \n'
                        'Зн \n'
                        '10:15 - 11:50 Микропроцессорные устройства РТС СН (лекция) Рассадкин 225м \n'
                        '12:00 - 13:35 Технология производства СРТС (лекция+семинар) Круглов 115м \n'
                        '13:50 - 15:25  Методы оптимизации (семинар) Романова 401м \n'
                        )
    elif payload == "24":
        await env.reply('Четверг \n'
                        'Чс \n'
                        '13:50 - 15:25 ТАУ (лекция) Третьяков 405м \n'
                        '15:40 - 17:15 ТАУ (лекция) Третьяков 405м \n'
                        '17:25 - 19:00 БЖД (лекция) 525э \n'
                        'Зн \n'
                        '13:50 - 15:25 ТАУ (лекция) Третьяков 405м \n'
                        '15:40 - 17:15 Экономика (лекция) Ряховская 525э \n'
                        '17:25 - 19:00 БЖД (лекция) 525э \n')
    elif payload == "25":
        await env.reply('Пятница \n'
                        'Чс \n'
                        '8:30 - 10:05  СР \n'
                        '10:15 - 11:50 СР \n'
                        '12:00 - 13:35 СР \n'
                        '13:50 - 15:25 СР \n'
                        '15:40 - 17:15 СР\n'
                        '17:25 - 19:00 СР \n'
                        'Зн \n'
                        '8:30 - 10:05  СР \n'
                        '10:15 - 11:50 СР \n'
                        '12:00 - 13:35 СР \n'
                        '13:50 - 15:25 СР \n'
                        '15:40 - 17:15 СР\n'
                        '17:25 - 19:00 СР \n')
    elif payload == "26":
        await env.reply('Суббота \n'
                        'Чс \n'
                        '8:30 - 10:05  СР \n'
                        '10:15 - 11:50 СР \n'
                        '12:00 - 13:35 СР \n'
                        '13:50 - 15:25 СР \n'
                        '15:40 - 17:15 СР\n'
                        '17:25 - 19:00 СР \n'
                        'Зн \n'
                        '8:30 - 10:05  СР \n'
                        '10:15 - 11:50 СР \n'
                        '12:00 - 13:35 СР \n'
                        '13:50 - 15:25 СР \n'
                        '15:40 - 17:15 СР\n'
                        '17:25 - 19:00 СР \n')
    elif payload == "27":
        await env.reply("Воскресеньк \n"
                        "В воскресенье надо спать")

    elif payload == "10":
        await env.reply("Выберите нужный вариант", keyboard=KEYBOARD_STRING_2)

    if payload == "31":
        await env.reply('Данная команда показывает текущую дату и время по гринвичу')
    elif payload == "32":
        await env.reply('Данная команда дублирует сообщение пользователя и отправляет в ответ (Например, '
                        'в ответ на echo hi вы получите от бота сообщение hi)')
    elif payload == "33":
        await env.reply('Данная команда заносит в базу данных какое-либо событие'
                        'Формат ввода таков: "Описание события",ГГГГММДД'
                        'Пример: register_event Рк по ТАУ,20191015'
                        'Если бот успешно занес данные в базу, то появится сообщение Reg_event is successful')
    elif payload == "34":
        await env.reply('Данная команда выдает данные о событиях,'
                        'которые произойдут в скором будущем (ближайшие 7 дней')
    elif payload == "35":
        await env.reply('Данная команда выдает данные о всех событиях в базе данных')
    elif payload == "36":
        await env.reply('Данная команда удаляет устарешвие события (дата которых меньше текущей даты хоть на 1 день)')
    elif payload == "37":
        await env.reply('Данная команда обновляет данные о дате события'
                        'Формат ввода таков: id события,ГГГГММДД'
                        'Пример: update_event_date 156632050,20191015'
                        'Если бот успешно обновил данные в базе, то появится сообщение Дата события обновлена'
                        'id события можно получить с помощью команды get_all_events')
    elif payload == "38":
        await env.reply('Данная команда обновляет данные о сообщении события'
                        'Формат ввода таков: id события,"Описание события"'
                        'Пример: update_event_message 156632050,Срок сдачи первой домашки по ТАУ'
                        'Если бот успешно обновил данные в базе, то появится сообщение Сообщение события обновлено'
                        'id события можно получить с помощью команды get_all_events')
    elif payload == "39":
        await env.reply('Данная команда выдает названия всех доступных команд')
    elif payload == "40":
        await env.reply('Данная команда заносит твои данные(id от ВКонтакте) в базу данных'
                        'чтобы бот мог слать сообщения самостоятельно (без твоего участия)'
                        'одна из функций использующее это - команда send_all')
    elif payload == "41":
        await env.reply('Данная команда выдает расписание')
    elif payload == "42":
        await env.reply('Данная команда отсылает всем пользователям, данные которых есть в базе, сообщение'
                        'Формат: send_all Завтра всем ко второй'
                        'В случае выполнения команды бот пришлет сообщение Success')





plugins = [plugin1, plugin2]
