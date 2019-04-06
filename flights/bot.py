#setup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json

#Process
updater = Updater (token = '827150461:AAF42bulzSf-RvFF5kS8exW4QqOxSqK4oPo')
dispatcher = updater.dispatcher

def startCommand (bot, update):
    bot.send_message (chat_id = update.message.chat_id, text = 'Hey, let us talk')

def textM_base(bot, update):
    response = 'Got your message: ' + update.message.text
    bot.send_message(chat_id = update.message.chat_id, text = response)
    
def textM_AI(bot, update):
    request = apiai.ApiAI('bf7ec4912ae24272a694d3fa8536b24c').text_request()
    request.lang = 'en'
    request.session_id = 'SmallTalk'
    request.query = update.message.text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfullment']['speech']
    
    #Action enginer
    if response:
        bot.send_message(chat_id = update.message.chat_id, text = response)
    else:
        bot.sent_message(chat_id = update.message.chat_id, text = 'what?')

#bot handlers
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textM_base)

#dispatch the handlers
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

#Initiator
updater.start_polling(clean = True)

#stop with Ctrl + C
updater.idle()