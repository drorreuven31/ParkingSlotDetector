import os
import logging
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

    def CreateHandlers(self):

        def start(update: Update, context: CallbackContext):
            context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

        def current_pic(update: Update, context: CallbackContext):
            snapshot = self.ipo_cam.get_current_frame()
            context.bot.send_photo(chat_id=update.effective_chat.id,photo =snapshot , caption ="Parking Now!")

        start_handler = CommandHandler('start', start)
        pic_handler = CommandHandler('pic', current_pic)
        self.dispatcher.add_handler(start_handler)
        self.dispatcher.add_handler(pic_handler)


    def send_message(self,msg,chat_id):
        self.dispatcher.bot.send_message(chat_id=chat_id, text=msg)

    def send_photo(self,pic,msg,chat_id):
        self.dispatcher.bot.send_photo(chat_id=chat_id, photo=pic,caption=msg)


