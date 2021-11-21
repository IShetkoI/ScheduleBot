import sqlite3

from aiogram.types import CallbackQuery
from aiogram.utils.markdown import text

from data import config
from keyboards.callback_datas import choose_group_callback, choose_subgroup_callback, cancel_callback, schedule_callback
from keyboards.keyboards_scheduled import choose_subgroup_kb, main_schedule_kb, choose_group_kb, choose_week_kb, days_kb
from loader import dp
from handlers.schedule.get_schedule_list import get_schedule_list
from handlers.schedule.get_time_now import get_weekday, get_number_week, get_table_fourth, get_time_range, \
    get_table_fifth, get_table_fourth_for_week, get_table_fifth_for_week, get_time


@dp.callback_query_handler(choose_group_callback.filter(choose_group='choose_group'))
async def save_group(call: CallbackQuery, callback_data: dict):
    number_group = str(callback_data.get('number_group'))
    if int(number_group) == 4:
        await call.message.edit_text(text=text('А номер подгруппы?'))
        await call.message.edit_reply_markup(choose_subgroup_kb())
    else:
        await call.message.edit_text(text='Что выберем?')
        await call.message.edit_reply_markup(main_schedule_kb(5, None))


@dp.callback_query_handler(choose_subgroup_callback.filter(choose_subgroup='choose_subgroup'))
async def save_subgroup(call: CallbackQuery, callback_data: dict):
    number_subgroup = str(callback_data.get('number_subgroup'))
    await call.message.edit_text(text='Что выберем?')
    await call.message.edit_reply_markup(main_schedule_kb(4, int(number_subgroup)))


@dp.callback_query_handler(schedule_callback.filter(button='main'))
async def save_subgroup(call: CallbackQuery, callback_data: dict):
    conn = sqlite3.connect('data.sqlite')
    cursor = conn.cursor()

    function = str(callback_data.get('function'))
    message_text = 'Что-то пошло не так...'

# ===============================================4-1=====================================================================

    if get_weekday(False) is not None:
        if function == 'tomorrow41':
            keyboard = main_schedule_kb(4, 1)
            sql = "SELECT Time, {0} FROM '{1}'".format(get_weekday(False),
                                                       (get_table_fourth(1, False)))
            cursor.execute(sql)
            day_list = cursor.fetchall()
            message_text = get_schedule_list(day_list)
    else:
        message_text = 'Отдыхаем.'

    if get_weekday(False) is not None:
        if function == 'tomorrow42':
            keyboard = main_schedule_kb(4, 2)
            sql = "SELECT Time, {0} FROM '{1}'".format(get_weekday(False),
                                                       (get_table_fourth(2, False)))
            cursor.execute(sql)
            day_list = cursor.fetchall()
            message_text = get_schedule_list(day_list)
    else:
        message_text = 'Отдыхаем.'

    if get_weekday(False) is not None:
        if function == 'tomorrow5':
            keyboard = main_schedule_kb(5)
            sql = "SELECT Time, {0} FROM '{1}'".format(get_weekday(False),
                                                       (get_table_fifth(False)))
            cursor.execute(sql)
            day_list = cursor.fetchall()
            message_text = get_schedule_list(day_list)
    else:
        message_text = 'Отдыхаем.'

    if get_weekday() is not None:
        if function == 'today41':
            sql = "SELECT Time, {0} FROM '{1}'".format(get_weekday(), (get_table_fourth(1)))
            cursor.execute(sql)
            day_list = cursor.fetchall()
            message_text = get_schedule_list(day_list)
            keyboard = main_schedule_kb(4,1)

        elif function == 'now41':
            keyboard = main_schedule_kb(4, 1)
            if get_time_range() is not None:
                sql = 'SELECT Time, {0} FROM "{1}" WHERE Time Like "{2}"'.format(get_weekday(),
                                                                                 (get_table_fourth(1)),
                                                                                 get_time_range())
                cursor.execute(sql)
                day_list = cursor.fetchall()
                message_text = get_schedule_list(day_list)
                if message_text == '' and 0 <= get_time().hour * 60 + get_time().minute <= 560:
                    sql = 'SELECT Time, {0} FROM "{1}" WHERE Time Like "{2}"'.format(get_weekday(),
                                                                                     (get_table_fourth(1)),
                                                                                     '9.35 - 10.55')
                    cursor.execute(sql)
                    day_list = cursor.fetchall()
                    message_text = get_schedule_list(day_list)
                elif message_text == '':
                    message_text = 'Отдыхаем.'
            else:
                message_text = 'Отдыхаем.'
    else:
        message_text = 'Отдыхаем.'

    if function == 'days41':
        message_text = f'Какую выберите неделю, если сейчас {get_number_week()}-ая?'
        keyboard = choose_week_kb(4, 1)

    elif function == 'first_week41':
        message_text = 'Какой выберите день?'
        keyboard = days_kb(4, 1, 1)

    elif function == 'second_week41':
        message_text = 'Какой выберите день?'
        keyboard = days_kb(4, 1, 2)

    elif function in ['Monday411', 'Tuesday411', 'Wednesday411', 'Thursday411', 'Friday411', 'Saturday411']:
        day = function
        sql = "SELECT Time, {0} FROM '{1}'".format(day[:-3], (get_table_fourth_for_week(1, 1)))
        cursor.execute(sql)
        day_list = cursor.fetchall()
        message_text = get_schedule_list(day_list)
        keyboard = days_kb(4, 1, 1)

    elif function in ['Monday412', 'Tuesday412', 'Wednesday412', 'Thursday412', 'Friday412', 'Saturday412']:
        day = function
        sql = "SELECT Time, {0} FROM '{1}'".format(day[:-3], (get_table_fourth_for_week(1, 2)))
        cursor.execute(sql)
        day_list = cursor.fetchall()
        message_text = get_schedule_list(day_list)
        keyboard = days_kb(4, 1, 2)

# ==================================================4-2===========================================================

    if get_weekday() is not None:
        if function == 'today42':
            sql = "SELECT Time, {0} FROM '{1}'".format(get_weekday(), (get_table_fourth(2)))
            cursor.execute(sql)
            day_list = cursor.fetchall()
            message_text = get_schedule_list(day_list)
            keyboard = main_schedule_kb(4,2)

        elif function == 'now42':
            keyboard = main_schedule_kb(4, 2)
            if get_time_range() is not None:
                sql = 'SELECT Time, {0} FROM "{1}" WHERE Time Like "{2}"'.format(get_weekday(),
                                                                                 (get_table_fourth(2)),
                                                                                 get_time_range())
                cursor.execute(sql)
                day_list = cursor.fetchall()
                message_text = get_schedule_list(day_list)
                if message_text == '' and 0 <= get_time().hour * 60 + get_time().minute <= 560:
                    sql = 'SELECT Time, {0} FROM "{1}" WHERE Time Like "{2}"'.format(get_weekday(),
                                                                                     (get_table_fourth(2)),
                                                                                     '9.35 - 10.55')
                    cursor.execute(sql)
                    day_list = cursor.fetchall()
                    message_text = get_schedule_list(day_list)
                elif message_text == '':
                    message_text = 'Отдыхаем.'
            else:
                message_text = 'Отдыхаем.'
    else:
        message_text = 'Отдыхаем.'

    if function == 'days42':
        message_text = f'Какую выберите неделю, если сейчас {get_number_week()}-ая?'
        keyboard = choose_week_kb(4, 2)

    elif function == 'first_week42':
        message_text = 'Какой выберите день?'
        keyboard = days_kb(4, 2, 1)

    elif function == 'second_week42':
        message_text = 'Какой выберите день?'
        keyboard = days_kb(4, 2, 2)

    if function in ['Monday421', 'Tuesday421', 'Wednesday421', 'Thursday421', 'Friday421', 'Saturday421']:
        day = function
        sql = "SELECT Time, {0} FROM '{1}'".format(day[:-3], (get_table_fourth_for_week(2, 1)))
        cursor.execute(sql)
        day_list = cursor.fetchall()
        message_text = get_schedule_list(day_list)
        keyboard = days_kb(4, 2, 1)

    if function in ['Monday422', 'Tuesday422', 'Wednesday422', 'Thursday422', 'Friday422', 'Saturday422']:
        day = function
        sql = "SELECT Time, {0} FROM '{1}'".format(day[:-3], (get_table_fourth_for_week(2, 2)))
        cursor.execute(sql)
        day_list = cursor.fetchall()
        message_text = get_schedule_list(day_list)
        keyboard = days_kb(4, 2, 2)

# ====================================================5==============================================================
    if get_weekday() is not None:
        if function == 'today5':
            sql = "SELECT Time, {0} FROM '{1}'".format(get_weekday(), (get_table_fifth()))
            cursor.execute(sql)
            day_list = cursor.fetchall()
            message_text = get_schedule_list(day_list)
            keyboard = main_schedule_kb(5)

        elif function == 'now5':
            keyboard = main_schedule_kb(5)
            if get_time_range() is not None:
                sql = 'SELECT Time, {0} FROM "{1}" WHERE Time Like "{2}"'.format(get_weekday(),
                                                                                 (get_table_fifth()),
                                                                                 get_time_range())
                cursor.execute(sql)
                day_list = cursor.fetchall()
                message_text = get_schedule_list(day_list)
                if message_text == '' and 0 <= get_time().hour * 60 + get_time().minute <= 560:
                    sql = 'SELECT Time, {0} FROM "{1}" WHERE Time Like "{2}"'.format(get_weekday(),
                                                                                     (get_table_fifth()),
                                                                                     '9.35 - 10.55')
                    cursor.execute(sql)
                    day_list = cursor.fetchall()
                    message_text = get_schedule_list(day_list)
                elif message_text == '':
                    message_text = 'Отдыхаем.'
            else:
                message_text = 'Отдыхаем.'
    else:
        message_text = 'Отдыхаем.'


    if function == 'days5':
        message_text = f'Какую выберите неделю, если сейчас {get_number_week()}-ая?'
        keyboard = choose_week_kb(5)

    elif function == 'first_week5':
        message_text = 'Какой выберите день?'
        keyboard = days_kb(group=5, week=1)

    elif function == 'second_week5':
        message_text = 'Какой выберите день?'
        keyboard = days_kb(group=5, week=2)

    if function in ['Monday51', 'Tuesday51', 'Wednesday51', 'Thursday51', 'Friday51', 'Saturday51']:
        day = function
        sql = "SELECT Time, {0} FROM '{1}'".format(day[:-2], (get_table_fifth_for_week(1)))
        cursor.execute(sql)
        day_list = cursor.fetchall()
        message_text = get_schedule_list(day_list)
        keyboard = days_kb(5, week=1)

    if function in ['Monday52', 'Tuesday52', 'Wednesday52', 'Thursday52', 'Friday52', 'Saturday52']:
        day = function
        sql = "SELECT Time, {0} FROM '{1}'".format(day[:-2], (get_table_fifth_for_week(2)))
        cursor.execute(sql)
        day_list = cursor.fetchall()
        message_text = get_schedule_list(day_list)
        keyboard = days_kb(5, week=2)



    await call.message.edit_text(text=message_text)
    await call.message.edit_reply_markup(keyboard)


@dp.callback_query_handler(cancel_callback.filter(cancel='cancel'))
async def cancel_callback(call: CallbackQuery, callback_data: dict):
    from_what = str(callback_data.get('from_what'))
    if from_what == 'main41' or from_what == 'main42' or from_what == 'main5':
        await call.message.edit_text(text=text('Выберите номер подгруппы:'))
        await call.message.edit_reply_markup(choose_subgroup_kb())
    elif from_what == 'choose_subgroup':
        await call.message.edit_text("Выберите группу:")
        await call.message.edit_reply_markup(choose_group_kb())
    elif from_what == 'choose_week41':
        await call.message.edit_text(text='Что выберем?')
        await call.message.edit_reply_markup(main_schedule_kb(4, 1))
    elif from_what == 'choose_week42':
        await call.message.edit_text(text='Что выберем?')
        await call.message.edit_reply_markup(main_schedule_kb(4, 2))
    elif from_what == 'choose_week5':
        await call.message.edit_text(text='Что выберем?')
        await call.message.edit_reply_markup(main_schedule_kb(5))
    elif from_what == 'days411' or from_what == 'days412':
        await call.message.edit_text(text=f'Какую выберите неделю, если сейчас {get_number_week()}-ая?')
        await call.message.edit_reply_markup(choose_week_kb(4, 1))
    elif from_what == 'days421' or from_what == 'days422':
        await call.message.edit_text(text=f'Какую выберите неделю, если сейчас {get_number_week()}-ая?')
        await call.message.edit_reply_markup(choose_week_kb(4, 2))
    elif from_what == 'days51' or from_what == 'days52':
        await call.message.edit_text(text=f'Какую выберите неделю, если сейчас {get_number_week()}-ая?')
        await call.message.edit_reply_markup(choose_week_kb(5))
