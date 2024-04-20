from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo


def web_app_inline_btn(user_id):
  btn = InlineKeyboardMarkup()
  btn.add(InlineKeyboardButton(text="Open poco loco", web_app=WebAppInfo(url=f"https://poco-loco.netlify.app/{user_id}")))

  return btn