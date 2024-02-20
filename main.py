from aiogram import executor
from config import dp
from handlers import (
    start,
    questionnaire,
    group_actions,
    registration,
    profile
)
from database import bot_db


async def on_startup(_):
    db = bot_db.Database()
    db.sql_create_tables()


start.register_start_handlers(dp=dp)
questionnaire.register_questionnaire_handlers(dp=dp)
registration.register_registration_handlers(dp=dp)
profile.register_profile_handler(dp=dp)
group_actions.register_group_actions_handlers(dp=dp)

if __name__ == "__main__":
    executor.start_polling(
        dp,
        on_startup=on_startup
    )