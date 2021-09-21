from data import config
from loader import dp
from aiogram import types


def get_fake_results(start_num: int, temp, size: int = 50):
    overall_items = 195
    results = []
    if size > 50:
        size = 50
    # Если результатов больше нет, отправляем пустой список
    if start_num >= overall_items:
        return []
    # Отправка неполной пачки (последней)
    elif start_num + size >= overall_items:
        for i in range(start_num, overall_items):
            results.append(list(temp.items())[i])
        return results
    else:
        for i in range(start_num, start_num + size):
            results.append(list(temp.items())[i])
        return results


def get_icon(item_num):
    if '.pdf' in item_num:
        return 'https://cdn.icon-icons.com/icons2/2790/PNG/128/pdf_filetype_icon_177525.png'
    elif '.xlsx' in item_num:
        return 'https://cdn.icon-icons.com/icons2/2790/PNG/128/xls_filetype_icon_177510.png'
    elif '.docx' in item_num or '.doc' in item_num:
        return 'https://cdn.icon-icons.com/icons2/2790/PNG/128/doc_filetype_icon_177541.png'
    elif '.json' in item_num:
        return 'https://cdn.icon-icons.com/icons2/2790/PNG/128/json_filetype_icon_177531.png'
    elif '.jpg' in item_num or '.jpeg' in item_num:
        return 'https://cdn.icon-icons.com/icons2/2790/PNG/128/jpg_filetype_icon_177533.png'
    elif '.html' in item_num:
        return 'https://cdn.icon-icons.com/icons2/2790/PNG/128/html_filetype_icon_177535.png'
    elif '.xml' in item_num:
        return 'https://cdn.icon-icons.com/icons2/2790/PNG/128/xml_filetype_icon_177509.png'
    elif '.zip' in item_num:
        return 'https://cdn.icon-icons.com/icons2/2790/PNG/128/zip_filetype_icon_177508.png'
    elif '.txt' in item_num:
        return 'https://cdn.icon-icons.com/icons2/2790/PNG/128/txt_filetype_icon_177515.png'
    elif '.csv' in item_num:
        return 'https://cdn.icon-icons.com/icons2/2790/PNG/128/csv_filetype_icon_177543.png'
    elif '.png' in item_num:
        return 'https://cdn.icon-icons.com/icons2/2790/PNG/128/png_filetype_icon_177523.png'
    elif '.ppt' in item_num:
        return 'https://cdn.icon-icons.com/icons2/2790/PNG/128/ppt_filetype_icon_177522.png'
    elif '.mp4' in item_num:
        return 'https://cdn.icon-icons.com/icons2/2790/PNG/128/filetype_mp_icon_177527.png'
    elif '.rar' in item_num:
        return 'https://cdn.icon-icons.com/icons2/2790/PNG/128/rar_filetype_icon_177520.png'
    elif '.rtf' in item_num:
        return 'https://cdn.icon-icons.com/icons2/2790/PNG/128/rtf_filetype_icon_177519.png'
    else:
        return 'https://cdn.icon-icons.com/icons2/2790/PNG/128/text_filetype_icon_177517.png'


# Инлайн-хэндлер из секции дополнительных материалов
@dp.inline_handler()
async def inline_handler_extra(query: types.InlineQuery):
    query_offset = int(query.offset) if query.offset else 0
    results=[]
    for item_num in get_fake_results(query_offset, temp=config.lib, size=len(config.lib)):
        if query.query.lower() in item_num[0].lower() or query.query.lower() in item_num[1][1].lower() or query.query.lower() in item_num[1][2].lower() or query.query == '':
            if len(str(item_num[1][2])) >= 30:
                file_name = item_num[1][2][:8]+"..."+item_num[1][2][-8:]
            else:
                file_name = item_num[1][2]
            results.append(types.InlineQueryResultArticle(id=str(item_num[0]), title=f"{item_num[0]}", description=f'{item_num[1][1]}\n{file_name}', thumb_url=get_icon(item_num[1][2]), input_message_content=types.InputTextMessageContent(message_text=f"/give_me {item_num[0]}")))
        # {имя файла:[айди сообшения, Категория, имя файла.формат]
    print(results)
    if len(results) < 50:
        # Результатов больше не будет, next_offset пустой
        await query.answer(results, is_personal=True, next_offset="", cache_time=1)
    else:
        # Ожидаем следующую пачку
        await query.answer(results, is_personal=True, next_offset=str(query_offset + 50), cache_time=1)
