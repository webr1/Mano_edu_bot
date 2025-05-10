from aiogram import types
from loader import bot,dp
from pathlib import Path


dow_path=Path().joinpath("Downloads","categories")
dow_path.mkdir(parents=True,exist_ok=True)


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def photo_saver(message:types.Message):
    await message.photo[-1].download(destination=dow_path)
    await message.reply("Xato kerakmas narsa yubormang")

@dp.message_handler(content_types=types.ContentType.VIDEO)
async def video_saver(message:types.Message):
    await message.video.download(destination=dow_path)
    await message.reply("Xato kerakmas narsa yubormang")

@dp.message_handler(content_types=types.ContentType.AUDIO)
async def audio_handler(message:types.Message):
    await message.audio.download(destination=dow_path)
    await message.reply("Xato kerakmas narsa yubormang")

@dp.message_handler(content_types=types.ContentType.STICKER)
async def stiker_handler(message:types.Message):
    await message.sticker.download(destination=dow_path)
    await message.reply("Xato kerakmas narsa yubormang")

@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def document_handler(message:types.Message):
    await message.document.download(destination=dow_path)
    await message.reply("Xato kerakmas narsa yubormang")

@dp.message_handler(content_types=types.ContentType.ANIMATION)
async def  animation_handler(message:types.Message):
    await message.animation.download(destination=dow_path)
    await message.reply("Xato kerakmas narsa yubormang")


