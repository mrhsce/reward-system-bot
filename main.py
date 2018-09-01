import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging
import os.path

# In order to execute this code pip should be installed, then executes these commands:
# - pip install python-telegram-bot
# - pip install python-telegram-bot[socks]

authorized_users = ['M_R_Heydarian']

WORK_TYPE = "work"
STUDY_TYPE = "study"
FUN_TYPE = "fun"

WORK_FACTOR = 4
STUDY_FACTOR = 3

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

work_total_hour = 0
study_total_hour = 0
fun_total_hour = 0


# File related functions
def retrieve_from_file():
  global work_total_hour, study_total_hour, fun_total_hour
  try:
    if os.path.exists('rs_vars'):
      f = open("rs_vars", "r")
      contents = f.read().split("\n")
      if len(contents) == 3:
        work_total_hour = float(contents[0].split("= ")[1])
        study_total_hour = float(contents[1].split("= ")[1])
        fun_total_hour = float(contents[2].split("= ")[1])
      f.close()
  except:
    print("Error reading the file")


def store_into_file():
  f = open("rs_vars", "w")
  f.write("Work hours" + " = " + str(work_total_hour) + "\n")
  f.write("Study hours" + " = " + str(study_total_hour) + "\n")
  f.write("fun hours" + " = " + str(fun_total_hour))
  f.close()


def calculate_hours(type, amount):
  global fun_total_hour
  if (type == WORK_TYPE):
    fun_total_hour = round(fun_total_hour + amount / WORK_FACTOR, 2)
  if (type == STUDY_TYPE):
    fun_total_hour = round(fun_total_hour + amount / STUDY_FACTOR, 2)


# pp = telegram.utils.request.Request(proxy_url='socks5://go.socadd.com:443', urllib3_proxy_kwargs={'username': 'ir124484','password': '08740874'})
# bot = telegram.Bot(token=my_token, request=pp)


def start(bot, update, args):
  user = update.message.from_user
  if (user.username in authorized_users):
    bot.send_message(chat_id=update.message.chat_id, text="At your service " + user.first_name)
  else:
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, you are not authorized")


def add(bot, update, args):
  if len(args) == 2:
    global work_total_hour, study_total_hour, fun_total_hour
    type = args[0]
    amount = float(args[1])
    if type == WORK_TYPE:
      work_total_hour += amount
    if type == STUDY_TYPE:
      study_total_hour += amount

    calculate_hours(type, amount)
    store_into_file()
    bot.send_message(chat_id=update.message.chat_id, text="Activity time has been added successfully")


def subtract(bot, update, args):
  if len(args) == 2:
    global work_total_hour, study_total_hour, fun_total_hour
    type = args[0]
    amount = float(args[1])
    if type == FUN_TYPE:
      fun_total_hour -= amount

    store_into_file()
    bot.send_message(chat_id=update.message.chat_id, text="Leisure time has been subtracted successfully")


def get_fun_time(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text="/result " + str(fun_total_hour))


updater = Updater(my_token, request_kwargs=REQUEST_KWARGS)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start, pass_args=True)
add_handler = CommandHandler('add', add, pass_args=True)
sub_handler = CommandHandler('subtract', subtract, pass_args=True)
get_fun_handler = CommandHandler('getFun', get_fun_time)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(add_handler)
dispatcher.add_handler(sub_handler)
dispatcher.add_handler(get_fun_handler)

updater.start_polling()
