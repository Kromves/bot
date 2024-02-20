from aiogram import types, Dispatcher
from config import bot
from keyboards import questionnaire_inline_buttons


async def questionnaire_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Python 🐍 or Mojo 🔥 ?",
        reply_markup=await questionnaire_inline_buttons.questionnaire_keyboard()
    )


async def python_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Oh cool, im python developer too\n"
             "Do u want switch to another language ?",
        reply_markup=await questionnaire_inline_buttons.python_questionnaire_keyboard()
    )


async def mojo_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Dont lie Mojo in alpha"
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


def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        questionnaire_start,
        lambda call: call.data == "start_questionnaire"
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