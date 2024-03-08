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
    referral_button = InlineKeyboardButton(
        "List of Referrals",
        callback_data="list_of_referrals"
    )
    markup.add(link_button)
    markup.add(referral_button)
    return markup