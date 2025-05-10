from keyboards.default.defold_keys import main_menu
from loader import dp,bot
from aiogram import types
from data.config import ADMINS
from states.list_of_students import *
from aiogram.dispatcher import FSMContext
from keyboards.inline.inline_keys import info_keys,back_1


@dp.message_handler(text="Kursga yozilish📝✅")
async def anketa_handler(message:types.Message):
    await message.answer("Har biriga javob bering. Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi")
    await message.answer("👨‍💼Ismizni kiriting:")
    await Data_students.name_student.set()



@dp.message_handler(state=Data_students.name_student)
async def name_handler(message:types.Message,state:FSMContext):
    try:
        name_student = str(message.text)

    except ValueError:
        await message.answer("Notugri ism")
    await state.update_data(
        {
            "name_student":name_student
        }

    )
    await message.answer("🕑 Yosh: Yoshingizni kiriting? Masalan, 19 ")
    await Data_students.age_student.set()

@dp.message_handler(state=Data_students.age_student)
async def age_handler(message:types.Message,state:FSMContext):
    try:
       age_student=int(message.text),
    except ValueError:
        await message.answer("Uzur faqat yoshizni kiriting:")

    await state.update_data(
        {
            "age_student":age_student
        }
    )
    await message.answer("🌐Biz haqimizda qaerdan bildiz masalan Telegram, Instagram, Facebook")
    await Data_students.info_how_know.set()


@dp.message_handler(state=Data_students.info_how_know)
async def info_know(message:types.Message,state:FSMContext):
    info_how_know=message.text
    await state.update_data(
        {
            "info_how_know":info_how_know
        }
    )

    await message.answer("🔎Uziz haqizda biroz mualimot bering nimaga qiziqansiz bundan oldin, masalan. Suzush, Inglis-tili, FootBall ")
    await Data_students.experiance_student.set()

@dp.message_handler(state=Data_students.experiance_student)
async def expa_handler(message:types.Message,state:FSMContext):
    experiance_student=message.text
    await state.update_data(
        {
               "experiance_student":experiance_student
        }
    )
    await message.answer("🏫Bundan oldin boshqa uquv kurslara tayorlangansizmi va qaysi, agar yoq bolsa 'yoq' deb qoldiring:")
    await Data_students.what_student_do.set()


@dp.message_handler(state=Data_students.what_student_do)
async def student_handler(message:types.Message,state:FSMContext):
    what_student_do=message.text
    await state.update_data(
        {
            "what_student_do":what_student_do
        }
    )
    await message.answer("🕰 Murojaat qilish vaqti: Qaysi vaqtda murojaat qilish mumkin? Masalan, 9.00 - 18.00 ")
    await Data_students.time_student.set()

@dp.message_handler(state=Data_students.time_student)
async def time_handler(message:types.Message,state:FSMContext):
    time_student=message.text
    await state.update_data(
        {
            "time_student":time_student
        }
    )
    await message.answer("📞 Aloqa: Bog`lanish uchun raqamingizni kiriting? Masalan, (+998) 90 123 45 67 ")
    await  Data_students.telephone_student.set()

@dp.message_handler(state=Data_students.telephone_student)
async def tele_student(message:types.Message,state:FSMContext):
    try:
        telephone_student = int(message.text)
    except ValueError:
        await message.answer("Iltimos togri nomer kiriting: ")
    # try:
    #
    # #    telephone_student=message.text.startswith("+998") and len(message.text)==11
    #     if telephone_student==1:
    #         await state.update_data(telephone_student=message.text)
    #     else:
    #         await message.answer("Raqamni togri kiriting: (+998)")
    # except AttributeError:
    #     await message.answer("Xato: iltimos sonni togri kiriting:! (+998)")


    await state.update_data(
        {
            "telephone_student":telephone_student
        }
    )


    data=await state.get_data()
    name=data.get("name_student")
    age=data.get("age_student")
    how_know=data.get("info_how_know")
    experiance=data.get("experiance_student")
    activity=data.get("what_student_do")
    time=data.get("time_student")
    phonenum=data.get("telephone_student")


    info = "hamma informatsiyalar shuyerda\n"
    info +=f"👨‍💼Ism: {name}\n"
    info +=f"🕑Yosh: {age}\n"
    info +=f"📚Biz haqimzda mualimontin olgan joy: {how_know}\n"
    info += f"💰Siz darajes: {experiance}\n"
    info += f"👨🏻‍💻Szini qiziqishiz: {activity}\n"
    info += f"🕰Vaqt: {time}\n"
    info += f"📞Sizni nomeriz: {phonenum}\n"



    await bot.send_message(ADMINS[0],info)
    await message.answer(info,reply_markup=info_keys)
    await state.finish()




@dp.callback_query_handler(text="togri")
async def tigri_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("🤗Sizni anketez muvofiyaqatliy qabul qilindi",reply_markup=back_1)

@dp.callback_query_handler(text="ortga_1")
async def back_1_handler(callback:types.CallbackQuery):
    await callback.message.delete()


@dp.callback_query_handler(text="notogri")
async def back_1_handler(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.reply(" Qabul qilinmadi",reply_markup=main_menu)



@dp.callback_query_handler(text="taklif")
async def sal_handler(callback:types.CallbackQuery):
    await callback.message.answer("Shuyerga maslaxatlarizni yozib qildiring")
    await Data_maslahat.bitta_text.set()


@dp.message_handler(state=Data_maslahat.bitta_text)
async def maslahat_handler(message:types.Message,state:FSMContext):
    bitta_text=message.text
    await state.update_data(
        {
          "bitta_text":bitta_text
        }
    )

    data_mas=await state.get_data()
    maslahat1=data_mas.get("bitta_text")


    adv=f"Sizni maslaxariz qabul qilindi:\n"
    adv+=f"{maslahat1}"



    await bot.send_message(ADMINS[0],adv)
    await message.answer(f"Taklif: ({adv})\n")
    await state.finish()

# @dp.message_handler(state="*", content_types=types.ContentType.TEXT)
# async def ignore_commands_in_state(message: types.Message, state: FSMContext):
#     current_state = await state.get_state()
#     if current_state is not None:
#         await message.answer("Iltimos, avval so'rovnomani to'ldiring!")
#         return






























