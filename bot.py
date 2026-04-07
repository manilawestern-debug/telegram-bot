from telegram.ext import Updater, MessageHandler, Filters

TOKEN = "8749296190:AAHHCUQChGuT_HGr9hN1IlStu0zkX96-MpE"

def delete_service(update, context):
    msg = update.message

    if msg.new_chat_members or msg.left_chat_member:
        try:
            context.bot.delete_message(
                chat_id=msg.chat_id,
                message_id=msg.message_id
            )
        except:
            pass

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.status_update, delete_service))

updater.start_polling()
updater.idle()
