import os
import logging
import cv2
from telegram.ext import Updater ,CommandHandler
from telegram import Update
from telegram.ext import CallbackContext


class TelegramParkingBot:
    def __init__(self,API_KEY,cam,group_id):
        self.updater = Updater(token=API_KEY)
        self.dispatcher = self.updater.dispatcher
        self.ip_cam=cam
        self.group_id =group_id

    def start_bot(self):
        self.CreateHandlers()
        self.updater.start_polling()

    def send_message(self,msg,chat_id):
        try:
            self.dispatcher.bot.send_message(chat_id=chat_id, text=msg)
        except:
            print("crashed")

    def send_photo(self,pic,msg,chat_id):
        bytes_pic = cv2.imencode('.jpg', pic)[1].tobytes()
        try:
            self.dispatcher.bot.send_photo(chat_id=chat_id, photo=bytes_pic,caption=msg)
        except:
            print("crashed")

    def start(update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

    def current_pic(self ,update: Update, context: CallbackContext):
        snapshot = self.ip_cam.get_current_frame()
        bytes_pic = cv2.imencode('.jpg', snapshot)[1].tobytes()
        try:
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=bytes_pic, caption="Parking Now!")
        except:
            print("crashed")

    def CreateHandlers(self):
      start_handler = CommandHandler('start', self.start)
      pic_handler = CommandHandler('pic', self.current_pic)
      self.dispatcher.add_handler(start_handler)
      self.dispatcher.add_handler(pic_handler)
