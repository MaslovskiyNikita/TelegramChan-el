import asyncio
from os import getenv
from Consts import TOKEN
from aiogram import Bot, Dispatcher, types
from send_message_to_chat import private_router

token = getenv(TOKEN)
dp = Dispatcher()
bot = Bot(TOKEN)

async def main():
    dp.include_router(private_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())