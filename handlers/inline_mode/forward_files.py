from ctypes import Union

from loader import dp
from aiogram import types

from utils.misc import rate_limit


def choose_category(chat_title):
    if chat_title == 'Курсовая работа':
        category = 'Электроника'
    elif chat_title == 'ОКМ 2-4/5':
        category = 'БДСА'
    elif chat_title == 'АТП':
        category = 'Тау'
    elif chat_title == 'БД/ООП':
        category = 'БДСА'
    elif chat_title == 'Метрология':
        category = 'Метрология'
    elif chat_title == 'Электроника 2-4-1':
        category = 'БДСА'
    elif chat_title == 'АТП 2-4':
        category = 'БДСА'
    else:
        category = 'Другое'
    return category


def get_name_and_category(message: types.Message):
    if message.caption is None:
        document_name = message.document.file_name
        category = choose_category(message.chat.title)
    else:
        if message.caption.find('\n', 0, len(message.caption)-1) != -1:
            category = None

# {"message_id":13422,"from":{"id":410249555,"is_bot":false,"first_name":"AllCash","username":"IShetkoI","language_code":"ru"},
#                     "chat":{"id":410249555,"first_name":"AllCash","username":"IShetkoI","type":"private"},
#                     "date":1630232830,"media_group_id":"13041862646322530",
#                     "document":{"file_name":"9cf3426c690f2558cab0f03713e6b2f4.jpg","mime_type":"image\/jpeg","thumb":{"file_id":"AAMCAgADGQEAAjRuYStg_vjA4IStve1Nc_nTUlkXAAEvAAKDEQACaYFRScOBRX7_vcDUAQAHbQADIAQ","file_unique_id":"AQADgxEAAmmBUUly","file_size":14875,"width":214,"height":320},"file_id":"BQACAgIAAxkBAAI0bmErYP74wOCErb3tTXP501JZFwABLwACgxEAAmmBUUnDgUV-_73A1CAE","file_unique_id":"AgADgxEAAmmBUUk","file_size":80031}}


@rate_limit(0, key="save_file")
@dp.message_handler(content_types=['document', 'photo'])
async def save_file(message: types.Message):
    print(message)
    # message = dp.bot.forward_message(message.message_id, id_backup_chat, disable_notification=True)
    # message_id = message.message_id
    # author = message.from_user.username if message.from_user.username is not None else message.chat.first_name
    # document_name, category = get_name_and_category(message)
    # print(document_name, message_id)
    # temp = {message.caption: [message_id, message.from_user.username, ]
    #
    #         }
    # 'Вареник, чертеж': [1330, 'fgh', 'Электроника', -1001250101317, 'вареник ас.ppt'],
#     temp = {message.chat.username: {'info': {'chat_id': message.chat.id, 'first_name': message.chat.first_name, 'group': None, 'subgroup': None, 'week': None, 'referral': None},
#                                         'casino': {'bet': 50, 'balance': 1000, 'game': {'dice': None, 'darts': None, 'basketball': None, 'football': None, 'bow': None}},
#                                         'tic tac toe': {}
#                                         }}
#         config.users.update(temp)
# {"message_id":13417,"from":{"id":410249555,"is_bot":false,"first_name":"AllCash","username":"IShetkoI","language_code":"ru"},"chat":{"id":410249555,"first_name":"AllCash","username":"IShetkoI","type":"private"},"date":1630173025,"document":{"file_name":"9cf3426c690f2558cab0f03713e6b2f4.jpg","mime_type":"image\/jpeg","thumb":{"file_id":"AAMCAgADGQEAAjRpYSp3YQ26gukZgDkXA2Uiksp0etEAAoMRAAJpgVFJw4FFfv-9wNQBAAdtAAMgBA","file_unique_id":"AQADgxEAAmmBUUly","file_size":14875,"width":214,"height":320},"file_id":"BQACAgIAAxkBAAI0aWEqd2ENuoLpGYA5FwNlIpLKdHrRAAKDEQACaYFRScOBRX7_vcDUIAQ","file_unique_id":"AgADgxEAAmmBUUk","file_size":80031},"caption":"Hhhh"}
