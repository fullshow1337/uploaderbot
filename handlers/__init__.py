from aiogram.dispatcher import Dispatcher
from aiogram.types import ContentTypes
from aiogram import filters

from .start import start_command
from .media import photo_message, video_message, gif_message
from .keyboard import message_with_keyboard


def setup_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(start_command, commands='start', state='*')
    dp.register_message_handler(photo_message, content_types=ContentTypes.PHOTO, state='*')
    dp.register_message_handler(video_message, content_types=ContentTypes.VIDEO, state='*')
    dp.register_message_handler(gif_message, content_types=ContentTypes.ANIMATION, state='*')
    dp.register_message_handler(
        message_with_keyboard, filters.ForwardedMessageFilter(is_forwarded=True) &
        filters.ContentTypeFilter(content_types=ContentTypes.ANY)
    )