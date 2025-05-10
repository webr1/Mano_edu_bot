from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


info_keys=InlineKeyboardMarkup(
inline_keyboard=[
    [
        InlineKeyboardButton(text="✅Ha",callback_data="togri"),
        InlineKeyboardButton(text="❌Yoq",callback_data="notogri"),
    ]
  ]
)
back_1=InlineKeyboardMarkup(
inline_keyboard=[
    [
        InlineKeyboardButton(text="Ortga",callback_data="ortga_1"),
    ]
  ]
)

kurslar=InlineKeyboardMarkup(
  inline_keyboard=[
        [
            InlineKeyboardButton(text="🐍Python Dasturchilik",callback_data="python"),
        ],

        [
            InlineKeyboardButton(text="🌟C++ Dasturchilik",callback_data="c++"),
        ],

        [
            InlineKeyboardButton(text="💻C# Dasturchilik", callback_data="c#")
        ],

        [
            InlineKeyboardButton(text="🤯Java Dasturchilik",callback_data="java")
        ],

        [
            InlineKeyboardButton(text="◀️Back",callback_data="back_job")
        ]


    ]
)

malumot_kurs=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📚Qushincha kurslar",callback_data="kurslar"),
        ],

        [
            InlineKeyboardButton(text="📞Aloqa", callback_data="aloqa"),
        ],

        [
            InlineKeyboardButton(text="🕑Takliflar",callback_data="taklif")
        ],

        [
            InlineKeyboardButton(text="🌐Manzil", url="www.google.com/maps?ll=41.339757,69.285038&z=16&t=m&hl=uz&gl=US&mapclient=embed&cid=5956285218696080088"),
        ],

        [
            InlineKeyboardButton(text="◀️Back",callback_data="back_3")
        ]

    ]
)


qushimcha_kurslar=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🤖Robatatexnika kurs", callback_data="robot"),
        ],

        [
            InlineKeyboardButton(text="🎙SMM kurs",callback_data="smm"),
        ],

        [
            InlineKeyboardButton(text="🇺🇸Ingliz tili kurs", callback_data="english"),
        ],

        [
            InlineKeyboardButton(text="🖥Kiberhafsizlik kurs", callback_data="kiber")
        ],

        [
            InlineKeyboardButton(text="◀️Back",callback_data="back_2")
        ],

        [
            InlineKeyboardButton(text="🏠Home",callback_data="home_1")
        ],


    ]
)

"""
Kurslar uchun backklar 10_dan boshlamadi
"""
back_10a=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='◀️Back',callback_data="back_10")
        ]
    ]
)

back_11a=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='◀️Back',callback_data="back_11")
        ]
    ]
)

back_12a=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='◀️Back',callback_data="back_12")
        ]
    ]
)

back_13a=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='◀️Back',callback_data="back_13")
        ]
    ]
)