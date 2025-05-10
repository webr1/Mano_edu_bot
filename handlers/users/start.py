import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from loader import dp,bot,db
from keyboards.default.defold_keys import main_menu
from keyboards.inline.inline_keys import *

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    username=message.from_user.username
    telegram_id=message.from_user.id
    full_name=message.from_user.full_name
    try:
        user=await db.add_user(full_name=full_name,username=username,telegram_id=telegram_id)
    except asyncpg.exceptions.UniqueViolationError:
        user=await db.select_user(telegram_id=telegram_id)
    await message.answer(f"Assalomu alaykum!{message.from_user.full_name}🌟 O‘quv markazimiz botiga xush kelibsiz! 🤖 Sizni bu yerda kutib olishdan xursandmiz! 🏫 Kurslar 📘, ro‘yxatdan o‘tish 📝 va savollaringizga javoblar 💬 shu yerda! {message.from_user.full_name}!" ,reply_markup=main_menu)
    count = await db.count_users()


    info = f"User haqida informatsiya \n"
    info+=f"User_name: @{username}\n"
    info+=f"User_id: {telegram_id}\n"
    info+=f"User_full_name: {full_name}\n"

    for admin in ADMINS:
        await bot.send_message(admin,info)
        await bot.send_message(admin,f"shuncha odam hozir ({count}) bazada")


@dp.message_handler(text="Ta'lim yo'nalishlari📚✨")
async def start_handler(message:types.Message):
    await message.delete()
    await message.answer("Biz – zamonaviy ta’lim markazi! 🎓 Har bir o‘quvchiga sifatli bilim va foydali ko‘nikmalar beramiz! 💡",reply_markup=kurslar)

@dp.callback_query_handler(text="back_job")
async def job_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.delete()

@dp.message_handler(text="Markaz haqida ma'lumotℹ️🏢")
async def start_handler(message:types.Message):
    await message.delete()
    await message.answer("Biz – zamonaviy ta’lim markazi! 🎓 Har bir o‘quvchiga sifatli bilim va foydali ko‘nikmalar beramiz! 💡",reply_markup=malumot_kurs)

@dp.callback_query_handler(text="kurslar")
async def qushimcha_kurs(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Qushimcha kurslar",reply_markup=qushimcha_kurslar)

@dp.callback_query_handler(text="back_2")
async def back_2_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Biz – zamonaviy ta’lim markazi! 🎓 Har bir o‘quvchiga sifatli bilim va foydali ko‘nikmalar beramiz! 💡",reply_markup=malumot_kurs)

@dp.callback_query_handler(text="home_1")
async def home_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("",reply_markup=main_menu)


@dp.callback_query_handler(text="robot")
async def robot_kurs(callback:types.CallbackQuery):
    await callback.message.edit_text("""🤖 Robototexnika Kurslari – Python Kurslari o‘quv markazida
Bizning Robototexnika kurslarimiz bolalar, o‘smirlar va texnikaga qiziquvchi kattalar uchun mo‘ljallangan. Darslar davomida siz haqiqiy robotlar yaratishni, ularni dasturlashni va turli sensorlar bilan ishlashni o‘rganasiz.

Nimalarni o‘rganasiz:
🔩 Robototexnika asoslari va komponentlari (motorlar, sensorlar, mikrokontrollerlar)
💡 Arduino va Raspberry Pi bilan ishlash
🧠 Robotlarni dasturlash (Python, C/C++)
⚙️ Harakatlanuvchi va mustaqil qaror qabul qiluvchi qurilmalar yaratish
🛠️ Amaliy loyihalar orqali bilimlarni mustahkamlash

Kreativ fikr, texnologiyaga qiziqish va muammolarni hal qilish ko‘nikmalarini rivojlantiring! Kelajak texnologiyalarini biz bilan o‘rganing.

📞 Aloqa uchun:
Telefon: +7 (123) 456-78-90""",reply_markup=qushimcha_kurslar)


@dp.callback_query_handler(text="smm")
async def robot_kurs(callback:types.CallbackQuery):
    await callback.message.edit_text("""SMM Kurslari – Python Kurslari o‘quv markazida
Bizning SMM (Social Media Marketing) kurslarimiz yangi boshlovchilar va bu sohada o‘zini rivojlantirmoqchi bo‘lganlar uchun mo‘ljallangan. Siz ijtimoiy tarmoqlarda samarali reklama yuritish, kontent yaratish va auditoriyani jalb qilish sir-asrorlarini o‘rganasiz.

Nimalarni o‘rganasiz:
📱 SMM asoslari va strategiyalari
📊 Instagram, Facebook, Telegram va TikTok platformalarida ishlash
✍️ Kreativ kontent yaratish va rejalashtirish
📈 Auditoriya tahlili va reklama kampaniyalarini boshqarish
🛠️ Amaliy loyihalar va topshiriqlar orqali bilimlarni mustahkamlash

SMM olamiga birinchi qadamingizni biz bilan qo‘ying va raqamli marketing sohasida professionalga aylaning!

📞 Aloqa uchun:
Telefon: +7 (123) 456-78-90""",reply_markup=qushimcha_kurslar)


@dp.callback_query_handler(text="english")
async def robot_kurs(callback:types.CallbackQuery):
    await callback.message.edit_text("""🇬🇧 Ingliz Tili Kurslari – Python Kurslari o‘quv markazida
Bizning Ingliz tili kurslarimiz boshlang‘ich darajadan boshlab, erkin gaplasha oladigan darajagacha mo‘ljallangan. Kurs davomida siz grammatika, so‘z boyligi, to‘g‘ri talaffuz va erkin muloqot qilishni o‘rganasiz.

Nimalarni o‘rganasiz:
📘 Ingliz tili grammatikasi asoslari
🗣️ Kundalik hayotda ishlatiladigan so‘zlar va iboralar
🎧 Eshitish, o‘qish, yozish va gapirish ko‘nikmalari
🧑‍🏫 Tajribali o‘qituvchilar bilan jonli darslar
📝 Har hafta amaliy mashqlar va testlar

Ingliz tilini biz bilan oson va samarali o‘rganing — ta’lim, ish va sayohat yo‘llarini oching!

📞 Aloqa uchun:
Telefon: +7 (123) 456-78-90""",reply_markup=qushimcha_kurslar)



@dp.callback_query_handler(text="kiber")
async def robot_kurs(callback:types.CallbackQuery):
    await callback.message.edit_text("""🔐 Kiberxavfsizlik Kurslari – Python Kurslari o‘quv markazida
Bugungi raqamli dunyoda kiberxavfsizlik bilimlari har qachongidan ham muhim! Bizning kurslarimiz yangi boshlovchilar va IT sohasiga kirishni istovchilar uchun mo‘ljallangan. Siz kompyuter xavfsizligi, tarmoq himoyasi va axborotlarni qanday himoyalashni o‘rganasiz.

Nimalarni o‘rganasiz:
🛡️ Kiberxavfsizlik asoslari va xatarlari
💻 Antiviruslar, firewall va himoya tizimlari
🔍 Xakerlik usullari va ularga qarshi choralar (etikal xakerlik)
🌐 Tarmoqlar xavfsizligi va shifrlash usullari
🧠 Real hayotdagi senariylar bilan amaliy mashg‘ulotlar

Axborotlaringizni himoya qilishni o‘rganing va IT sohasida talabgir mutaxassisga aylaning!

📞 Aloqa uchun:
Telefon: +7 (123) 456-78-90""",reply_markup=qushimcha_kurslar)

@dp.callback_query_handler(text="back_3")
async def back_3_handler(callback:types.CallbackQuery):
    await callback.message.delete()


@dp.callback_query_handler(text="aloqa")
async def robot_kurs(callback:types.CallbackQuery):
    await callback.message.edit_text("""📞 Biz bilan bog'lanish

Agar sizda kurslarimiz haqida savollar bo'lsa yoki ro'yxatdan o'tmoqchi bo'lsangiz, biz bilan quyidagi usullar orqali bog'lanishingiz mumkin:

Telefon: +7 (123) 456-78-90

Email: example@email.com

Manzil: Tashkent sh., Main Street, 12-uy

Biz sizga yordam berishdan mamnunmiz! Kurslar va ro'yxatdan o'tish jarayoni bo'yicha savollaringizni kutib qolamiz.""",reply_markup=malumot_kurs)



#Kurslar haqida informatsila berish
"""python xaqida"""
@dp.callback_query_handler(text="python")
async def python_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("""📚 Python Kurslari

Bizning Python kurslarimiz yangi boshlovchilar va tajribali dasturchilar uchun mo'ljallangan. Siz tilning asoslarini, mashhur kutubxonalar bilan ishlashni va amaliy loyihalar yaratishni o'rganasiz.

Nimalarni o'rganasiz:

🖥️ Python sintaksisi va asoslari

📊 NumPy, pandas, Django va Flask bilan ishlash

🛠️ Amaliy loyihalar va mashqlar

Pythonni biz bilan o'rganishni boshlang va dasturlash dunyosiga kirib boring!

📞 Aloqa: Telefon: +7 (123) 456-78-90""",reply_markup=back_10a)

@dp.callback_query_handler(text="back_10")
async def back_11_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Biz – zamonaviy ta’lim markazi! 🎓 Har bir o‘quvchiga sifatli bilim va foydali ko‘nikmalar beramiz! 💡",reply_markup=kurslar)

"""C++ XAQIDA"""


@dp.callback_query_handler(text="c++")
async def python_handler(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("""📚 C++ Kurslari

Bizning C++ kurslarimiz yangi boshlovchilar va o'z bilimlarini oshirmoqchi bo'lganlar uchun mos. Siz tilni, algoritmlar va yuqori samarali dasturlar yaratishni o'rganasiz.

Nimalarni o'rganasiz:

💻 Sintaksis va xotira bilan ishlash asoslari

⚙️ Algoritmlar va ma'lumotlar tuzilmalari

🛠️ Amaliy loyihalar va vazifalar

C++ ni biz bilan o'rganishni boshlang va samarali dasturlar yarating!

📞 Aloqa: Telefon: +7 (123) 456-78-90""", reply_markup=back_11a)


@dp.callback_query_handler(text="back_11")
async def back_11_handler(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Biz – zamonaviy ta’lim markazi! 🎓 Har bir o‘quvchiga sifatli bilim va foydali ko‘nikmalar beramiz! 💡", reply_markup=kurslar)

"""C# XAQIDA"""

@dp.callback_query_handler(text="c#")
async def python_handler(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("""📚 C# Kurslari

Bizning C# kurslarimiz yangi boshlovchilar va tajribali dasturchilar uchun mo'ljallangan. Siz tilning asoslarini, OOPni o'rganasiz va Windows ilovalarini hamda veb-servislar yaratishni o'rganasiz.

Nimalarni o'rganasiz:

🖥️ C# sintaksisi va OOP asoslari

🌐 Windows ilovalarini va veb-servislar yaratish

🛠️ Amaliy mashqlar va loyihalar

C#ni biz bilan o'rganishni boshlang va dasturlash ko'nikmalarini rivojlantiring!

📞 Aloqa: Telefon: +7 (123) 456-78-90""", reply_markup=back_11a)


@dp.callback_query_handler(text="back_12")
async def back_11_handler(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Biz – zamonaviy ta’lim markazi! 🎓 Har bir o‘quvchiga sifatli bilim va foydali ko‘nikmalar beramiz! 💡", reply_markup=kurslar)
"""JAVA XAQIGA"""


@dp.callback_query_handler(text="java")
async def python_handler(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("""📚 Java Kurslari

Bizning Java kurslarimiz yangi boshlovchilar va o'z bilimlarini oshirmoqchi bo'lganlar uchun mo'ljallangan. Siz tilning asoslarini, OOP va kuchli, kengaytiriladigan dasturlar yaratishni o'rganasiz.

Nimalarni o'rganasiz:

💡 Java sintaksisi va OOP asoslari

🌐 Veb-dasturlar va mobil ilovalar yaratish

🛠️ Amaliy loyihalar va mashqlar

Java ni biz bilan o'rganishni boshlang va dasturlash dunyosini kashf eting!

📞 Aloqa: Telefon: +7 (123) 456-78-90""", reply_markup=back_13a)


@dp.callback_query_handler(text="back_13")
async def back_11_handler(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Biz – zamonaviy ta’lim markazi! 🎓 Har bir o‘quvchiga sifatli bilim va foydali ko‘nikmalar beramiz! 💡", reply_markup=kurslar)
