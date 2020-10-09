from telegram.ext import Updater,CommandHandler,MessageHandler,Filters

ADAFRUIT_IO_USERNAME = os.getenv(ADAFRUIT_IO_USERNAME) #io username
ADAFRUIT_IO_KEY = os.getenv(ADAFRUIT_IO_KEY) #io key

from Adafruit_IO import Client, Data
aio = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)

def send_value(value):
  feed = aio.feeds('bot')
  aio.send_data(feed.key,value)

def turnoffthelight(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Bulb turned off")
  context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://pngimg.com/uploads/bulb/bulb_PNG1241.png')
  send_value(0)

def turnonthelight(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Bulb turned on")
  context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://img.icons8.com/plasticine/2x/light-on.png')
  send_value(1)

def input_message(update, context):
  text=update.message.text
  if text == 'turnonthelight':
    send_value(1)
    context.bot.send_message(chat_id=update.effective_chat.id,text="Bulb turned on")
    context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://pngimg.com/uploads/bulb/bulb_PNG1244.png')
  elif text == 'turnoffthelight':
    send_value(0)
    context.bot.send_message(chat_id=update.effective_chat.id,text="Bulb turned off")
    context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://pngimg.com/uploads/bulb/bulb_PNG1245.png')

def start(update,context):
  start_message= 'start'
  context.bot.send_message(chat_id=update.effective_chat.id, text=start_message)

u=Updater('1095551077:AAG6FFWWPPZCT6AKbSdda-6EthbeAt_-xQ4',use_context=True) #telegram token
dp = u.dispatcher
dp.add_handler(CommandHandler('turnoffthelight',turnoffthelight))
dp.add_handler(CommandHandler('turnonthelight',turnonthelight))
dp.add_handler(CommandHandler('start',start))
dp.add_handler(MessageHandler(Filters.text & (~Filters.command),input_message))
u.start_polling()
u.idle()
