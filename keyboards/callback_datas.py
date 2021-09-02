from aiogram.utils.callback_data import CallbackData

# ======================================|Cancel|====================================

cancel_callback = CallbackData('cancel-prefix', 'cancel', 'from_what')
"""'cancel-prefix', 'cancel', 'from_what'"""

# =====================================|Schedule|===================================

choose_group_callback = CallbackData('choose_group-prefix', 'choose_group', 'number_group')
"""'choose_group', 'choose_group', 'number_group'"""

choose_subgroup_callback = CallbackData('choose_subgroup-prefix', 'choose_subgroup', 'number_subgroup')
"""'ChooseSubgroup-prefix', 'choose_subgroup', 'number_subgroup'"""

schedule_callback = CallbackData('mainSchedule-prefix', 'button', 'function')
"""'mainSchedule-prefix', 'button', 'function'"""
