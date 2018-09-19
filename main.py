from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging
import web_server
import shared

# In order to execute this code pip should be installed, then executes these commands:
# - pip install python-telegram-bot
# - pip install python-telegram-bot[socks]


logging.basicConfig(filename='RS_bot.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.WARNING)

logger = logging.getLogger(__name__)

my_token = "673291427:AAHokJVmKsbZDvrgzhJtD-oOCacVRSN1VHE"

REQUEST_KWARGS = {
  'proxy_url': 'socks5://go.socadd.com:443',
  # Optional, if you need authentication:
  'urllib3_proxy_kwargs': {
    'username': 'ir124484',
    'password': '08740874',
  }
}



# **************************** Authorization **********************************

authorized_users = ['M_R_Heydarian']


def isUserAuthorized(user):
    if user.username in authorized_users:
        return True
    else:
        return False





# pp = telegram.utils.request.Request(proxy_url='socks5://go.socadd.com:443', urllib3_proxy_kwargs={'username': 'ir124484','password': '08740874'})
# bot = telegram.Bot(token=my_token, request=pp)


def ping(bot, update, args):
  user = update.message.from_user
  if isUserAuthorized(user):
    bot.send_message(chat_id=update.message.chat_id, text="At your service " + user.first_name)
  else:
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, you are not authorized")


def add(bot, update, args):
    user = update.message.from_user
    if isUserAuthorized(user):
      if len(args) == 2:
        type = args[0]
        amount = float(args[1])

        shared.update_hours(type, amount)
        bot.send_message(chat_id=update.message.chat_id, text="Activity time has been added successfully")


def subtract(bot, update, args):
    user = update.message.from_user
    if isUserAuthorized(user):
      if len(args) == 2:
        type = args[0]
        amount = float(args[1])

        shared.update_hours(type, amount)
        bot.send_message(chat_id=update.message.chat_id, text="Leisure time has been subtracted successfully")

def activity(bot, update, args):
    user = update.message.from_user
    if isUserAuthorized(user):
        if len(args) == 1:
            type = args[0]

            shared.update_hours_activity(type)
            bot.send_message(chat_id=update.message.chat_id, text="Activity time has been subtracted stored")


def get_fun_time(bot, update):
    user = update.message.from_user
    if isUserAuthorized(user):
        bot.send_message(chat_id=update.message.chat_id, text="/result " + str(shared.get_fun_hours()))


updater = Updater(my_token, request_kwargs=REQUEST_KWARGS)
dispatcher = updater.dispatcher

ping_handler = CommandHandler('ping', ping, pass_args=True)
add_handler = CommandHandler('add', add, pass_args=True)
sub_handler = CommandHandler('subtract', subtract, pass_args=True)
activity_handler = CommandHandler('activity', activity, pass_args=True)
get_fun_handler = CommandHandler('getFun', get_fun_time)

dispatcher.add_handler(ping_handler)
dispatcher.add_handler(add_handler)
dispatcher.add_handler(sub_handler)
dispatcher.add_handler(get_fun_handler)
dispatcher.add_handler(activity_handler)

updater.start_polling()

web_server.start_server()