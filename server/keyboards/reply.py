from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo


def profile_btn():
  btn = ReplyKeyboardMarkup(resize_keyboard=True)
  btn.add("Профиль", "Меню")
  btn.add("Тех. поддержка")

  return btn


def web_app_reply_btn(user_id):
  btn = ReplyKeyboardMarkup(resize_keyboard=True)
  btn.add(KeyboardButton(text="Open poco loco", web_app=WebAppInfo(url=f"https://poco-loco.netlify.app/{user_id}")))

  return btn