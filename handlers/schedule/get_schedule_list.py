def get_schedule_list(scroll):
    text = ''
    for item in scroll:
        if item[1] != '':
            if item != scroll[-1]:
                text += str(item[0]) + '\n' + str(item[1]) + '\n\n'
            else:
                text += str(item[0]) + '\n' + str(item[1])
    return text
