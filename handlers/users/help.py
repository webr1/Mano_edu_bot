from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish\n",
            "/help - Yordam\n"
            "/video - video chiqaradi\n")
    
    await message.answer("\n".join(text))