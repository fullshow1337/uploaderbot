from cgitb import text
from aiogram.types import Message
from aiogram import md

async def message_with_keyboard(message: Message) -> None:
    answer = ''
    if message.reply_markup:
        for markup in message.reply_markup.inline_keyboard:
            for i in markup:
                answer += f"{md.hcode(i.text)}\n\n"
        await message.answer(text=answer)
