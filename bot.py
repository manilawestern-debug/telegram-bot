from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters, ChatJoinRequestHandler

import os

TOKEN = os.getenv("8749296190:AAFTt1x-cs9Gq994KV_Uvo6ULorC4RYobo4")

# ✅ Auto approve join requests
async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.chat_join_request.approve()

# ✅ Delete join + leave messages
async def delete_service(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message

    if msg.new_chat_members or msg.left_chat_member:
        try:
            await msg.delete()
        except:
            pass

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(ChatJoinRequestHandler(approve))
app.add_handler(MessageHandler(filters.StatusUpdate.ALL, delete_service))

app.run_polling()
