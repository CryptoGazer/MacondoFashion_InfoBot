import typing
import random
from datetime import datetime

from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

from config import TOKEN, MEMBERS_INFO, LINKS_INFO

bot = Bot(TOKEN)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton("/members")).insert(KeyboardButton("/links"))


async def on_startup(_):
    print("...\n\tHere we go...\n...")


@dp.message_handler(commands=["start", "members"])
async def members_info(message: types.Message):
    await bot.send_message(message.from_user.id, MEMBERS_INFO[0],
                           reply_markup=kb)
    await bot.send_message(message.from_user.id, MEMBERS_INFO[1],
                           reply_markup=kb)
    await bot.send_message(message.from_user.id, MEMBERS_INFO[2],
                           reply_markup=kb)


@dp.message_handler(commands="links")
async def links_info(message: types.Message):
    await bot.send_message(message.from_user.id, LINKS_INFO[0],
                           reply_markup=kb)
    await bot.send_message(message.from_user.id, LINKS_INFO[1],
                           reply_markup=kb)
    await bot.send_message(message.from_user.id, LINKS_INFO[2],
                           reply_markup=kb)
    await bot.send_message(message.from_user.id, LINKS_INFO[3],
                           reply_markup=kb)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
