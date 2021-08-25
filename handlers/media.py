import telegraph
from io import BytesIO
from aiogram.types import Message


BASE_URL = 'https://telegra.ph'


async def photo_message(message: Message) -> None:
    photo = BytesIO()
    await message.photo[-1].download(destination=photo)
    data = await telegraph.upload(file=photo)
    await message.reply(text=BASE_URL + data[0]['src'])


async def video_message(message: Message) -> None:
    video = BytesIO()
    await message.video.download(destination=video)
    data = await telegraph.upload(file=video)
    await message.reply(text=BASE_URL + data[0]['src'])


async def gif_message(message: Message) -> None:
    gif = BytesIO()
    await message.animation.download(destination=gif)
    data = await telegraph.upload(file=gif)
    await message.reply(text=BASE_URL + data[0]['src'])