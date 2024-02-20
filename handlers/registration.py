import sqlite3
from aiogram import types, Dispatcher
from config import bot, MEDIA_DESTINATION
from database import bot_db
from keyboards import start_inline_buttons
import const
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class RegistrationStates(StatesGroup):
    nickname = State()
    biography = State()
    age = State()
    zodiac_sign = State()
    gender = State()  # Новое состояние для пола
    marital_status = State()  # Новое состояние для семейного положения
    photo = State()

async def registration_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Отправьте мне ваш никнейм, пожалуйста!"
    )
    await RegistrationStates.nickname.set()


async def load_nickname(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Отправьте мне вашу биографию!'
    )
    await RegistrationStates.next()


async def load_bio(message: types.Message,
                   state: FSMContext):
    async with state.proxy() as data:
        data['bio'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Сколько вам лет?\n"
             "(Отправьте только числовой текст)\n"
             "Пример: 27 или 29"
    )
    await RegistrationStates.next()


async def load_age(message: types.Message,
                   state: FSMContext):
    try:
        int(message.text)
    except ValueError:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Я просил отправить только числовой текст\n"
                 "Регистрация не удалась ❌\n"
                 "Пожалуйста, начните регистрацию заново!!!"
        )
        await state.finish()
        return

    async with state.proxy() as data:
        data['age'] = int(message.text)
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Теперь отправьте мне ваш знак зодиака'
    )
    await RegistrationStates.next()


async def load_zodiac_sign(message: types.Message,
                           state: FSMContext):
    async with state.proxy() as data:
        data['sign'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Укажите ваш пол"
    )
    await RegistrationStates.next()


async def load_gender(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Укажите ваше семейное положение'
    )
    await RegistrationStates.next()


async def load_marital_status(message: types.Message,
                              state: FSMContext):
    async with state.proxy() as data:
        data['marital_status'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Отправьте мне ваше фото\n"
             "только в формате фотографии"
    )
    await RegistrationStates.next()


async def load_photo(message: types.Message,
                     state: FSMContext):
    db = bot_db.Database()
    path = await message.photo[-1].download(
        destination_dir=MEDIA_DESTINATION
    )

    async with state.proxy() as data:
        db.sql_insert_profile(
            tg_id=message.from_user.id,
            nickname=data['nickname'],
            bio=data['bio'],
            age=data['age'],
            sign=data['sign'],
            gender=data['gender'],  # Добавлено поле пола
            marital_status=data['marital_status'],  # Добавлено поле семейного положения
            photo=path.name
        )

        with open(path.name, "rb") as photo:
            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=photo,
                caption=const.PROFILE_TEXT.format(
                    nickname=data['nickname'],
                    bio=data['bio'],
                    age=data['age'],
                    sign=data['sign'],
                    gender=data['gender'],  # Добавлено поле пола
                    marital_status=data['marital_status'],  # Добавлено поле семейного положения
                )
            )
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Вы успешно зарегистрировались 🎉🍾\n"
             "Поздравляю!!!"
    )
    await state.finish()


def register_registration_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        registration_start,
        lambda call: call.data == "registration"
    )
    dp.register_message_handler(
        load_nickname,
        state=RegistrationStates.nickname,
        content_types=['text']
    )
    dp.register_message_handler(
        load_bio,
        state=RegistrationStates.biography,
        content_types=['text']
    )
    dp.register_message_handler(
        load_age,
        state=RegistrationStates.age,
        content_types=['text']
    )
    dp.register_message_handler(
        load_zodiac_sign,
        state=RegistrationStates.zodiac_sign,
        content_types=['text']
    )
    dp.register_message_handler(
        load_gender,
        state=RegistrationStates.gender,
        content_types=['text']
    )
    dp.register_message_handler(
        load_marital_status,
        state=RegistrationStates.marital_status,
        content_types=['text']
    )
    dp.register_message_handler(
        load_photo,
        state=RegistrationStates.photo,
        content_types=types.ContentTypes.PHOTO
    )
