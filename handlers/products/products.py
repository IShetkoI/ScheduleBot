from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.callback_data import CallbackData
from fuzzywuzzy import fuzz

from handlers.states import States
from loader import dp


message_list_id = 1
message_list_text = ''

sort_list = [
    "морская капуста",
    "майонез",
    "селедка",
    "сельд",
    "кургрудка",
    "кур.грудка",
    "яйца",
    "колбаски",
    "колб.вар"
    "колбаса вар",
    "сардельки",
    "колбасу вар",
    "сосиски",
    "колбаса для пиццы",
    "дрожжи",
    "корица",
    "перец",
    "ванилин",
    "ванильный сахар",
    "приправа",
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
    "том.соус"
    "картофан",
    "картофель",
    "огурец",
    "огурцы",
    "помидоры",
    "томаты",
    "шампиньон",
    "лимон",
    "морковь",
    "пельмени",
    "морожки",
    "мороженки"
]

prod_callback = CallbackData('mainSchedule-prefix', 'prod', 'func')


def prod_kb():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    bt1 = types.InlineKeyboardButton('Добавить',
                                     callback_data=prod_callback.new(prod='prod',
                                                                     func="prod"))
    keyboard.row(bt1)
    return keyboard


@dp.callback_query_handler(prod_callback.filter(prod='prod'))
async def prod(call: CallbackQuery, callback_data: dict):
    await States.edit.set()


@dp.message_handler(state=States.edit)
async def ed(message: types.Message, state: FSMContext):
    mother_list = message.text + "\n" + message_list_text
    await message.delete()
    mother_list = mother_list.split("\n")
    sorted_mother_list = ""
    for i in sort_list:
        for k in mother_list:
            if fuzz.partial_ratio(i.lower(), k.lower()) >= 80:
                sorted_mother_list += k + "\n"
                mother_list.remove(k)
                break

    if mother_list:
        sorted_mother_list += "\n\nНе найдено:\n"
        for k in mother_list:
            sorted_mother_list += k + "\n"
    await state.reset_state()
    await dp.bot.edit_message_text(text=sorted_mother_list, chat_id=-1001445673200, message_id=message_list_id.message_id, reply_markup=prod_kb())


@dp.message_handler(commands='s')
async def get_list(message: types.Message):
    if message.chat.id == -1001445673200 and (message.from_user.id == 843434988 or message.from_user.id == 410249555):
        await States.new.set()


@dp.message_handler(state=States.new)
async def get_list(message: types.Message, state: FSMContext):
    if message.chat.id == -1001445673200 and (message.from_user.id == 843434988 or message.from_user.id == 410249555):
        global message_list_text
        global message_list_id
        mother_list = message.text
        await message.delete()
        mother_list = mother_list.split("\n")
        sorted_mother_list = ""
        for i in sort_list:
            for k in mother_list:
                if fuzz.partial_ratio(i.lower(), k.lower()) >= 80:
                    sorted_mother_list += k + "\n"
                    mother_list.remove(k)
                    break

        if mother_list:
            sorted_mother_list += "\n\nНе найдено:\n"
            for k in mother_list:
                sorted_mother_list += k + "\n"
        await state.reset_state()
        message_list_text = sorted_mother_list.replace("\n\nНе найдено:\n", "")
        message_list_id = await message.answer(sorted_mother_list, reply_markup=prod_kb())
