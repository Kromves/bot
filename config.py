from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = config("TOKEN")
MEDIA_DESTINATION = config("MEDIA_DESTINATION")
GROUP_ID = config("GROUP_ID")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)