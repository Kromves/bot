from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def reference_menu_keyboard():
    markup = InlineKeyboardMarkup()
    link_button = InlineKeyboardButton(
        "Generate Link 🔗",
        callback_data="reference_link"
    )
    markup.add(link_button)
    return markup