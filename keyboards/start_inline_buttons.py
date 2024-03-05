from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Questionnaire 🗒️",
        callback_data="start_questionnaire"
    )
    registration_button = InlineKeyboardButton(
        "Registration 😎",
        callback_data="registration"
    )
    my_profile_button = InlineKeyboardButton(
        "My Profile 🐲",
        callback_data="my_profile"
    )
    profiles_button = InlineKeyboardButton(
        "View Profiles",
        callback_data="random_profiles"
    )
    reference_button = InlineKeyboardButton(
        "Reference Menu 💵",
        callback_data="reference_menu"
    )
    news_button = InlineKeyboardButton(
        "Latest News 🗞️",
        callback_data="latest_news"
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(my_profile_button)
    markup.add(profiles_button)
    markup.add(reference_button)
    markup.add(news_button)
    return markup