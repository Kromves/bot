from aiogram import types, Dispatcher

from config import bot
from keyboards import questionnaire_inline_buttons


async def questionnaire_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Python 🐍 or Mojo 🔥 ?",
        reply_markup=await questionnaire_inline_buttons.questionnaire_keyboard()
    )


async def initial_question(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="love or career ?",
        reply_markup=await questionnaire_inline_buttons.future_keyboard()
    )


async def python_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Oh cool, im python developer too\n"
             "Do u want switch to another language ?",
        reply_markup=await questionnaire_inline_buttons.python_questionnaire_keyboard()
    )
async def feture_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Are you sure of your choice?\n"
             "Don't regret it later ",
        reply_markup=await questionnaire_inline_buttons.love_questionnaire_keyboard()
    )

async def mojo_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Dont lie Mojo in alpha"
    )

async def career_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="You've made the right choice"
    )

async def yes_python_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Dont betray Python!"
    )


async def no_python_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Cool, stay in python"
    )

async def yes_love_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Good luck man!"
    )


async def no_love_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="We're always with you"
    )


def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        questionnaire_start,
        lambda call: call.data == "start_questionnaire"
    )
    dp.register_callback_query_handler(
        initial_question,
        lambda call: call.data == "initial_question"

    )
    dp.register_callback_query_handler(
        python_answer,
        lambda call: call.data == "python"
    )
    dp.register_callback_query_handler(
        mojo_answer,
        lambda call: call.data == "mojo"
    )
    dp.register_callback_query_handler(
        yes_python_answer,
        lambda call: call.data == "yes_python"
    )
    dp.register_callback_query_handler(
        no_python_answer,
        lambda call: call.data == "no_python"
    )
    dp.register_callback_query_handler(
        feture_answer,
        lambda call: call.data == "love i"
    )
    dp.register_callback_query_handler(
        career_answer,
        lambda call: call.data == "career i"
    )
    dp.register_callback_query_handler(
        yes_love_answer,
        lambda call: call.data == "yes_love"
    )
    dp.register_callback_query_handler(
        no_love_answer,
        lambda call: call.data == "no_love"
    )