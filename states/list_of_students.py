from aiogram.dispatcher.filters.state import State,StatesGroup


class Data_students(StatesGroup):
    name_student=State()
    age_student=State()
    info_how_know=State()
    experiance_student=State()
    what_student_do=State()
    time_student=State()
    telephone_student=State()


class Data_maslahat(StatesGroup):
    bitta_text=State()
