import datetime

from data import config


def get_time():
    delta = datetime.timedelta(hours=3, minutes=0)
    return datetime.datetime.now(datetime.timezone.utc) + delta


def get_weekday(condition: bool = True):
    number_day = get_time().weekday()
    if condition:
        if number_day == 0:
            return "Monday"
        elif number_day == 1:
            return "Tuesday"
        elif number_day == 2:
            return "Wednesday"
        elif number_day == 3:
            return "Thursday"
        elif number_day == 4:
            return "Friday"
        elif number_day == 5:
            return "Saturday"
        else:
            return None
    else:
        if number_day == 6:
            return "Monday"
        elif number_day == 0:
            return "Tuesday"
        elif number_day == 1:
            return "Wednesday"
        elif number_day == 2:
            return "Thursday"
        elif number_day == 3:
            return "Friday"
        elif number_day == 4:
            return "Saturday"
        else:
            return "Monday"


def get_number_week():
    number_week = int(datetime.datetime.utcnow().isocalendar()[1])
    if number_week % 2 == 0:
        return 2
    else:
        return 1


def get_table_fourth(subgroup):
    return f"4-{subgroup}-{get_number_week()}"


def get_table_fourth_for_week(subgroup, week):
    return f"4-{subgroup}-{week}"


def get_table_fifth():
    return f"5-{get_number_week()}"


def get_table_fifth_for_week(week):
    return f"5-{week}"


def get_time_range():
    time_now = get_time().hour * 60 + get_time().minute
    # 00:00 - 9:20 (1)
    if 0 <= time_now <= 560:
        return '8.00 - 9.20'

    # 9:20 - 10:55 (2)
    elif 560 < time_now <= 655:
        return '9.35 - 10.55'

    # 10:55 - 12:45 (3)
    elif 655 < time_now <= 765:
        return '11.25 - 12.45'

    # 12:45 - 14:20 (4)
    elif 765 < time_now <= 860:
        return '13.00 - 14.20'

    # 14:20 - 16:00 (5)
    elif 860 < time_now <= 960:
        return '14.40 - 16.00'

    # 16:00 - 23:59
    elif 960 < time_now <= (1380 + 55):
        return None
