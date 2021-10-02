from aiogram import types
from fuzzywuzzy import fuzz

from loader import dp

sort_list = [
    "морская капуста",
    "майонез",
    "селедка",
    "кургрудка",
    "яйца",
    "колбаса вар",
    "колбасу вар",
    "сосиски",
    "колбаса для пиццы",
    "дрожжи",
    "корица",
    "перец",
    "ванилин",
    "ванильный сахар",
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
    "сулугуни",
    "мацарелла",
    "батон",
    "лаваш",
    "хлеб",
    "чай",
    "кофе",
    "туал.бум",
    "туалетная",
    "салфетки",
    "губки",
    "подс.масло",
    "горошек",
    "кукуруза",
    "томатная паста",
    "картофан",
    "морковь",
    "пельмени"
]


@dp.message_handler()
async def get_list(message: types.Message):
    if message.chat.id == -1001445673200 and (message.from_user.id == 843434988 or message.from_user.id == 410249555):
        mother_list = message.text
        await message.delete()
        mother_list = mother_list.split("\n")
        sorted_mother_list = ""
        num = 1
        for i in sort_list:
            for k in mother_list:
                if fuzz.partial_ratio(i.lower(), k.lower()) >= 80:
                    sorted_mother_list += str(num) + ") " + k + "\n"
                    num += 1
                    mother_list.remove(k)
                    break

        if mother_list:
            sorted_mother_list += "\n\nНе найдено:\n"
            for k in mother_list:
                sorted_mother_list += k + "\n"
        await message.answer(sorted_mother_list)
