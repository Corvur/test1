import asyncio
import logging
import sys

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = "7218540653:AAH1r5HvxtYxeZG_h3kJ95bT8M7vgSjpSwU"

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Привет, я бот")


dp.message()
async def echo_handler(message: Message) -> None:
    await message.send_copy(chat_id=message.chat.id)


async def main() -> None:
    bot=Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
