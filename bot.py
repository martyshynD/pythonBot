from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
from aiogram.utils.keyboard import InlineKeyboardBuilder 
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message 
import random

# Ініціалізація 
API_TOKEN = 'your_token'
bot = Bot(token = API_TOKEN)
dp = Dispatcher()


# Відслідковування команди start
@dp.message(Command(commands = ['start']))
async def show_hello(message:types.Message):
    await message.reply("Hello!")


# клавіатурка
inline_keys = InlineKeyboardBuilder()
inline_keys.add(types.InlineKeyboardButton(text="Google",url="https://www.google.com"))
inline_keys.add(types.InlineKeyboardButton(text="Reddit",url="https://www.reddit.com"))



# відображенння клавіатурки
@dp.message(Command(commands = ['url']))
async def show_url(message:types.Message):
    await message.reply("Ти хотів посилання? От тобі!", reply_markup=inline_keys.as_markup())

# менюшка
@dp.message(Command(commands = ['menu']))
async def show_menu(message:types.Message):
# створюю клавіатурку    
    key_board = [[
        KeyboardButton(text='/url'),
        KeyboardButton(text='/start'),
        KeyboardButton(text='/info'),
        ],
        ]
    
    board=ReplyKeyboardMarkup(keyboard=key_board, resize_keyboard = True) 
    await message.reply("МЕНЮ", reply_markup=board)


# набір приколів
phrase = ["ти сьогодні неперевершений",
          "Політех - the best",
          "Я Бетмен",
          "Бот топ я танцюю хіп хоп"]


# ХАХА
@dp.message(Command(commands = ['haha']))
async def show_smth(message:types.Message):
    text = random.choice(phrase)
    await message.reply(text)


# виведення тексту який ти написав
@dp.message()
async def show_hello(message:types.Message):
    await message.reply(message.text)


# головна функція відслідковування
async def main():
    await dp.start_polling(bot) # вісдлідковує повідомлення всі у боті


# виклик головної функції
if __name__ == "__main__":
    asyncio.run(main())
