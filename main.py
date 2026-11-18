import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salut ! Moi c'est FRIENDZONE 😎 Envoie-moi /friendzone pour voir ton sort.")

async def friendzone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Désolé bro, tu es officiellement en FRIENDZONE 💔😂")

async def repondre(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texte = update.message.text.lower()
    if "salut" in texte or "bonjour" in texte:
        await update.message.reply_text("Salut mon gars ? Ça va ? 😎")
    elif "friendzone" in texte:
        await update.message.reply_text("Toi aussi t'es friendzone ? Bienvenue au club 😂")
    else:
        await update.message.reply_text("J'ai pas compris, envoie /friendzone 😅")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("friendzone", friendzone))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, repondre))
    print("Bot FRIENDZONE lancé...")
    app.run_polling()
