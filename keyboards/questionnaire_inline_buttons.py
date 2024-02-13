from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    python_button = InlineKeyboardButton(
        "Python 🐍",
        callback_data="python"
    )
    mojo_button = InlineKeyboardButton(
        "Mojo 🔥",
        callback_data="mojo"
    )
    markup.add(python_button)
    markup.add(mojo_button)
    return markup


async def future_keyboard():
    markup = InlineKeyboardMarkup()
    love_button = InlineKeyboardButton(
        "Love",
        callback_data="love i"
    )
    career_button = InlineKeyboardButton(
        "Career",
        callback_data="career i"
    )
    markup.add(love_button)
    markup.add(career_button)
    return markup


async def python_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    python_button = InlineKeyboardButton(
        "Yes",
        callback_data="yes_python"
    )
    python_no_button = InlineKeyboardButton(
        "No",
        callback_data="no_python"
    )
    markup.add(python_button)
    markup.add(python_no_button)
    return markup


async def love_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    love_button = InlineKeyboardButton(
        "Yes",
        callback_data="yes_love"
    )
    love_no_button = InlineKeyboardButton(
        "No",
        callback_data="no_love"
    )
    markup.add(love_button)
    markup.add(love_no_button)
    return markup


