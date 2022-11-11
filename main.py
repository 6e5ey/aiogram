import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from kaspi import kaspi_shop_get_info
from dotenv import load_dotenv

# environmental variables
load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print("Бот вышел в онлайн")


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Ехала, кидай SKU")
# reply to specific message


@dp. message_handler()
async def reply(message: types.Message):
    try:
        sku = message.text.split("_")[0]                # Turn sku_store into str and get rid of _
        await message.answer(kaspi_shop_get_info(sku))
    except:
        await message.answer("Ошибка. Проверьте данные")







if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)