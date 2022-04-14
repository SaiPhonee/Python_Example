from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext):
    update.message.reply_text(f'Привет {update.effective_user.first_name}')

def help(update: Update, context: CallbackContext):
    update.message.reply_text(f'/hello - Приветствие\n/help - Cписок команд\n/sum - Сумма двух чисел')

def sum(update: Update, context: CallbackContext):
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    # print(msg)
    update.message.reply_text(f'{x} + {y} = {x+y}')

updater = Updater('5138331316:AAHC7l-Hd3Ai-ucQiuRYa4TjQdJQW81NcjY')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('sum', sum))
print('server start')
updater.start_polling()
updater.idle()