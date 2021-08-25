from aiogram.bot import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_polling

import logging
from config import BOT_TOKEN
from handlers import setup_handlers


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)
logging.basicConfig(level='INFO')


async def on_start(dp: Dispatcher) -> None:
    setup_handlers(dp=dp)


if __name__ == '__main__':
    start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=on_start
    )