from aiogram.types import Message


async def start_command(message: Message) -> None:
    await message.answer(text='Hello send me media file')