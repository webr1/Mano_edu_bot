from aiogram.types import KeyboardButton ,  ReplyKeyboardMarkup

main_menu=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ta'lim yo'nalishlari📚✨"),
            KeyboardButton(text="Kursga yozilish📝✅")
        ],

        [
            KeyboardButton(text="Markaz haqida ma'lumotℹ️🏢"),
            KeyboardButton(text="So'nggi yangiliklar🗞️🆕")
        ],
    ],
resize_keyboard=True

)
