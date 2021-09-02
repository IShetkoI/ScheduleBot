from aiogram import types

from keyboards.callback_datas import choose_group_callback, choose_subgroup_callback, cancel_callback, schedule_callback


def choose_group_kb():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    bt1 = types.InlineKeyboardButton('4',
                                     callback_data=choose_group_callback.new(choose_group='choose_group',
                                                                             number_group=4))
    bt2 = types.InlineKeyboardButton('5',
                                     callback_data=choose_group_callback.new(choose_group='choose_group',
                                                                             number_group=5))
    keyboard.row(bt1, bt2)
    return keyboard


def choose_subgroup_kb():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    bt1 = types.InlineKeyboardButton('1',
                                     callback_data=choose_subgroup_callback.new(choose_subgroup='choose_subgroup',
                                                                                number_subgroup=1))
    bt2 = types.InlineKeyboardButton('2',
                                     callback_data=choose_subgroup_callback.new(choose_subgroup='choose_subgroup',
                                                                                number_subgroup=2))
    back_button = types.InlineKeyboardButton('Назад',
                                             callback_data=cancel_callback.new(cancel='cancel',
                                                                               from_what='choose_subgroup'))
    keyboard.row(bt1, bt2)
    keyboard.add(back_button)
    return keyboard


def main_schedule_kb(group: int, subgroup: int = None):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    if group == 4 and subgroup == 1:
        bt1 = types.InlineKeyboardButton('Сегодня',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='today41'))
        bt2 = types.InlineKeyboardButton('Сейчас',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='now41'))
        bt3 = types.InlineKeyboardButton('Завтра',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='tomorrow41'))
        back_button = types.InlineKeyboardButton(text="Назад",
                                                 callback_data=cancel_callback.new(cancel='cancel',
                                                                                   from_what='main41'))
        keyboard.row(bt1, bt2, bt3)
        bt4 = types.InlineKeyboardButton('Дни недели',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='days41'))
        keyboard.add(bt4, back_button)
    elif group == 4 and subgroup == 2:
        bt1 = types.InlineKeyboardButton('Сегодня',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='today42'))
        bt2 = types.InlineKeyboardButton('Сейчас',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='now42'))
        bt3 = types.InlineKeyboardButton('Завтра',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='tomorrow42'))
        back_button = types.InlineKeyboardButton(text="Назад",
                                                 callback_data=cancel_callback.new(cancel='cancel',
                                                                                   from_what='main42'))
        keyboard.row(bt1, bt2, bt3)
        bt4 = types.InlineKeyboardButton('Дни недели',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='days42'))
        keyboard.add(bt4, back_button)
    elif group == 5 and subgroup is None:
        bt1 = types.InlineKeyboardButton('Сегодня',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='today5'))
        bt2 = types.InlineKeyboardButton('Сейчас',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='now5'))
        bt3 = types.InlineKeyboardButton('Завтра',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='tomorrow5'))
        back_button = types.InlineKeyboardButton(text="Назад",
                                                 callback_data=cancel_callback.new(cancel='cancel',
                                                                                   from_what='main5'))
        keyboard.row(bt1, bt2, bt3)
        bt4 = types.InlineKeyboardButton('Дни недели',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='days5'))
        keyboard.add(bt4, back_button)
    return keyboard


def choose_week_kb(group: int, subgroup: int = None):
    if group == 4 and subgroup == 1:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        bt1 = types.InlineKeyboardButton('Первая',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='first_week41'))
        bt2 = types.InlineKeyboardButton('Вторая', callback_data=schedule_callback.new(button='main',
                                                                                       function='second_week41'))
        back_button = types.InlineKeyboardButton(text="Назад",
                                                 callback_data=cancel_callback.new(cancel='cancel',
                                                                                   from_what='choose_week41'))
        keyboard.row(bt1, bt2)
        keyboard.add(back_button)
    if group == 4 and subgroup == 2:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        bt1 = types.InlineKeyboardButton('Первая',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='first_week42'))
        bt2 = types.InlineKeyboardButton('Вторая', callback_data=schedule_callback.new(button='main',
                                                                                       function='second_week42'))
        back_button = types.InlineKeyboardButton(text="Назад",
                                                 callback_data=cancel_callback.new(cancel='cancel',
                                                                                   from_what='choose_week42'))
        keyboard.row(bt1, bt2)
        keyboard.add(back_button)
    if group == 5 and subgroup is None:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        bt1 = types.InlineKeyboardButton('Первая',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='first_week5'))
        bt2 = types.InlineKeyboardButton('Вторая', callback_data=schedule_callback.new(button='main',
                                                                                       function='second_week5'))
        back_button = types.InlineKeyboardButton(text="Назад",
                                                 callback_data=cancel_callback.new(cancel='cancel',
                                                                                   from_what='choose_week5'))
        keyboard.row(bt1, bt2)
        keyboard.add(back_button)
    return keyboard


def days_kb(group: int, subgroup: int = None, week: int= None):
    if group == 4 and subgroup == 1:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        bt1 = types.InlineKeyboardButton('Понедельник',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='Monday41'+str(week)))
        bt2 = types.InlineKeyboardButton('Вторник',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='Tuesday41'+str(week)))
        bt3 = types.InlineKeyboardButton('Среда',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='Wednesday41'+str(week)))
        bt4 = types.InlineKeyboardButton('Четверг',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='Thursday41'+str(week)))
        bt5 = types.InlineKeyboardButton('Пятница',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='Friday41'+str(week)))
        bt6 = types.InlineKeyboardButton('Суббота',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='Saturday41'+str(week)))
        back_button = types.InlineKeyboardButton(text="Назад",
                                                 callback_data=cancel_callback.new(cancel='cancel',
                                                                                   from_what='days41'+str(week)))
        keyboard.row(bt1, bt2, bt3)
        keyboard.row(bt4, bt5, bt6)
        keyboard.add(back_button)

    if group == 4 and subgroup == 2:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        bt1 = types.InlineKeyboardButton('Понедельник',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='Monday42'+str(week)))
        bt2 = types.InlineKeyboardButton('Вторник',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='Tuesday42'+str(week)))
        bt3 = types.InlineKeyboardButton('Среда',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='Wednesday42'+str(week)))
        bt4 = types.InlineKeyboardButton('Четверг',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='Thursday42'+str(week)))
        bt5 = types.InlineKeyboardButton('Пятница',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='Friday42'+str(week)))
        bt6 = types.InlineKeyboardButton('Суббота',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='Saturday42'+str(week)))
        back_button = types.InlineKeyboardButton(text="Назад",
                                                 callback_data=cancel_callback.new(cancel='cancel',
                                                                                   from_what='days42'+str(week)))
        keyboard.row(bt1, bt2, bt3)
        keyboard.row(bt4, bt5, bt6)
        keyboard.add(back_button)

    if group == 5 and subgroup is None:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        bt1 = types.InlineKeyboardButton('Понедельник',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='Monday5'+str(week)))
        bt2 = types.InlineKeyboardButton('Вторник',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='Tuesday5'+str(week)))
        bt3 = types.InlineKeyboardButton('Среда',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='Wednesday5'+str(week)))
        bt4 = types.InlineKeyboardButton('Четверг',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='Thursday5'+str(week)))
        bt5 = types.InlineKeyboardButton('Пятница',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='Friday5'+str(week)))
        bt6 = types.InlineKeyboardButton('Суббота',
                                         callback_data=schedule_callback.new(button='main',
                                                                             function='Saturday5'+str(week)))
        back_button = types.InlineKeyboardButton(text="Назад",
                                                 callback_data=cancel_callback.new(cancel='cancel',
                                                                                   from_what='days5'+str(week)))
        keyboard.row(bt1, bt2, bt3)
        keyboard.row(bt4, bt5, bt6)
        keyboard.add(back_button)
    return keyboard
