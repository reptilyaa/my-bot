from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token="7325205146:AAEiXPyt3enFRSP_fKMWEibcIE-TGc-u2cc")
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)