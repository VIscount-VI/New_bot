"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types
from buttons import button
from loc import create_user, create_inventory
from states import FeedbState
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
API_TOKEN = '5731462370:AAGXikaid_W3aVqNul97k0w2bbffzbMJ8Sg'
import emoji

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage = MemoryStorage())



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    
    await message.reply("Salom " + emoji.emojize(":waving_hand:") + "siz ro`yhatdan o`tdingiz", reply_markup=button)
    await message.answer('Adminga xabar yuborishnigiz mumkun !! ' + emoji.emojize(":page_facing_up:"))
    await message.answer('Xabar yuborish uchun "Yuborish"ni bosing va xabar yuboring !!' + emoji.emojize(""))
    print(create_user(message.from_user.username, message.from_user.first_name, message.from_user.id))

@dp.message_handler(Text(startswith='Yuborish'))
async def feedb_1(message: types.Message):
    await FeedbState.body.set()


@dp.message_handler(state=FeedbState.body)
async def feedb_2(message: types. Message, state:FSMContext):
    await message.answer(create_inventory(message.from_user.first_name, message.from_user.id, message.text))
    await state.finish() 



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    