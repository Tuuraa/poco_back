from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

import keyboards.reply as reply
import keyboards.inline as inline

API_TOKEN = '7107976356:AAELWm4P1Nb2sK2yEueUpBXBFSX4JOjDllU'
bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    await msg.reply(
        "Hi! I am your bot.",
        reply_markup=reply.profile_btn()
    )


@dp.message_handler(lambda msg: msg.text.lower() == 'меню')
async def poco_menu(msg: types.Message):
    await msg.answer(
        f"You can open site for order what you want 👇",
        reply_markup=inline.web_app_inline_btn(msg.from_user.id)
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)