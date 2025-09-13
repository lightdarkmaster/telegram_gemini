import os
import logging
import google.generativeai as genai
from dotenv import load_dotenv
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get API keys
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I'm a Telegram bot powered by Google's Gemini AI.\n\n"
        "Send me any message and I'll respond using Gemini!\n"
        "Use /help to see available commands."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n\n"
        "Just send me a text and I'll reply with Gemini!"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_message = update.message.text
        user_name = update.effective_user.first_name

        logger.info(f"Received message from {user_name}: {user_message}")

        # Show typing action
        await context.bot.send_chat_action(
            chat_id=update.effective_chat.id,
            action=ChatAction.TYPING
        )

        # Get Gemini response
        response = model.generate_content(user_message)

        # Reply to user
        await update.message.reply_text(response.text)

        logger.info(f"Sent response to {user_name}")

    except Exception as e:
        logger.error(f"Error handling message: {e}")
        await update.message.reply_text(
            "Sorry, I encountered an error while processing your message."
        )

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Update {update} caused error {context.error}")

def main():
    if not TELEGRAM_TOKEN or not GEMINI_API_KEY:
        logger.error("Please set TELEGRAM_BOT_TOKEN and GEMINI_API_KEY in your environment.")
        return

    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Error handler
    application.add_error_handler(error_handler)

    logger.info("Bot is starting...")
    application.run_polling()

if __name__ == "__main__":
    main()

