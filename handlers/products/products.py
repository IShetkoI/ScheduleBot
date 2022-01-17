from pprint import pprint

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.callback_data import CallbackData
from fuzzywuzzy import fuzz

from handlers.states import States
from loader import dp

message_list_id = 1
message_decor_id = 1
food = {}

sort_list = [
    "морская капуста",
    "майонез",
    "селедка",
    "сельд",
    "краб",
    "кургрудка",
    "курина грудка",
    "кур.грудка",
    "яйца",
    "колбаски",
    "колб.вар"
    "колбаса вар",
    "сардельки",
    "колбасу вар",
    "сосиски",
    "колбаса для пиццы",
    "колбаса",
    "ветчина",
    "дрожжи",
    "консерва",
    "корица",
    "перец",
    "ванилин",
    "ванильный сахар",
    "приправа",
    "стружка",
    "паприка",
    "вафли",
    "гречка",
    "рис",
    "макароны",
    "спагетти",
    "сахар",
    "соль",
    "мука",
    "сода",
    "молоко",
    "сливки",
    "сгущенка",
    "кефир",
    "сметана",
    "творог",
    "слив масло",
    "сливмасло",
    "маслослив",
    "сыр",
    "сырки",
    "сыр плавленый",
    "сулугуни",
    "мацарелла",
    "батон",
    "лаваш",
    "хлеб",
    "чай",
    "кофе",
    "шоколад",
    "туал.бум",
    "тупо.бумага",
    "туалетная",
    "палочки",
    "салфетки",
    "мыло",
    "шампунь",
    "стиральный",
    "губки",
    "фольга",
    "пергамент",
    "подс.масло",
    "подсолнечное",
    "горошек",
    "кукуруза",
    "фасоль",
    "томатная паста",
    "том.соус",
    "вода",
    "картофан",
    "картофель",
    "огурец",
    "огурцы",
    "помидоры",
    "томаты",
    "шампиньон",
    "лимон",
    "капуста",
    "свекла",
    "свёкла",
    "морковь",
    "мандарины",
    "пельмени",
    "морожки",
    "мороженки"
]


def prod_kb(foods: dict):
    keyboard_main = types.InlineKeyboardMarkup(row_width=2)
    for key, value in foods.items():
        if value['click'] == 0:
            keyboard_main.add(types.InlineKeyboardButton(text=f"{key}", callback_data=prod_callback.new(prod='prod',
                                                                                                        food=f"{key[:13]}")))
        elif value['click'] == 1:
            keyboard_main.add(types.InlineKeyboardButton(text=strike(key), callback_data=prod_callback.new(prod='prod',
                                                                                                           food=f"{key[:13]}")))
        else:
            pass

    keyboard_main.add(types.InlineKeyboardButton(text="➕", callback_data=prod_callback.new(prod='prod', food="add")),
                      types.InlineKeyboardButton(text="🔄", callback_data=prod_callback.new(prod='prod',
                                                                                            food="repeat")))

    return keyboard_main


def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result


# start sort prod
@dp.message_handler(commands='s')
async def get_list(message: types.Message):
    global message_decor_id
    await message.delete()
    message_decor_id = await message.answer("Ожидаю список")
    await States.new.set()


# add prod
@dp.message_handler(state=States.new)
async def get_list(message: types.Message, state: FSMContext):
    global message_list_id, message_decor_id

    await dp.bot.delete_message(chat_id=message.chat.id, message_id=message_decor_id.message_id)

    sorted_list = ""
    unsorted_list = message.text.split("\n")

    await message.delete()

    for i in sort_list:
        for k in unsorted_list:
            if fuzz.partial_ratio(i.lower(), k.lower()) >= 80:
                sorted_list += k + "\n"
                unsorted_list.remove(k)

    for i in range(len(sorted_list.split("\n"))):
        if sorted_list.split("\n")[i] != '':
            temp = {sorted_list.split("\n")[i]: {'click': 0}}
            food.update(temp)

    if unsorted_list:
        message_list_id = await message.answer(text="Не найдено:\n\n" + str('\n'.join(map(str, unsorted_list))),
                                               reply_markup=prod_kb(food))
    else:
        message_list_id = await message.answer(text="Список:", reply_markup=prod_kb(food))

    await state.reset_state()


prod_callback = CallbackData('mainSchedule-prefix', 'prod', 'food')


# callback_query_handler
@dp.callback_query_handler(prod_callback.filter(prod='prod'))
async def prod(call: CallbackQuery, callback_data: dict):
    global message_list_id, message_decor_id
    action = callback_data.get('food')

    if action != "add" and action != "repeat":
        for key, value in food.items():
            if action == key[:13]:
                food[key]['click'] += 1
        message_list_id = await dp.bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                                 message_id=call.message.message_id,
                                                                 reply_markup=prod_kb(food))

    elif action == "repeat":
        for key, value in food.items():
            food[key]['click'] = 0
        message_list_id = await dp.bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                                 message_id=call.message.message_id,
                                                                 reply_markup=prod_kb(food))

    else:
        message_decor_id = await call.message.answer("Что добавим?")
        await States.edit.set()


# добавляем продукты in list
@dp.message_handler(state=States.edit)
async def ed(message: types.Message, state: FSMContext):
    global message_list_id, message_decor_id

    await dp.bot.delete_message(chat_id=message.chat.id, message_id=message_decor_id.message_id)

    sorted_list = ""
    unsorted_list = message.text.split("\n")

    await message.delete()

    for i in sort_list:
        for k in unsorted_list:
            if fuzz.partial_ratio(i.lower(), k.lower()) >= 80:
                sorted_list += k + "\n"
                unsorted_list.remove(k)

    for i in range(len(sorted_list.split("\n"))):
        if sorted_list.split("\n")[i] != '':
            temp = {sorted_list.split("\n")[i]: {'click': 0}}
            food.update(temp)

    if unsorted_list:
        message_list_id = await dp.bot.edit_message_text(
            text="Не найдено:\n\n" + str('\n'.join(map(str, unsorted_list))),
            chat_id=message.chat.id, message_id=message_list_id.message_id,
            reply_markup=prod_kb(food))
    else:
        message_list_id = await dp.bot.edit_message_text(text="Список:", chat_id=message.chat.id,
                                                         message_id=message_list_id.message_id,
                                                         reply_markup=prod_kb(food))

    await state.reset_state()
