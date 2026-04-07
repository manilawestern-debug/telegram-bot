import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = "8749296190:AAHHCUQChGuT_HGr9hN1IlStu0zkX96-MpE"

async def delete_service(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message

    if msg.new_chat_members or msg.left_chat_member:
        try:
            await msg.delete()
        except:
            pass

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.StatusUpdate.ALL, delete_service))

    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
