#!/usr/bin/python3

import asyncio
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

from settings import TELEGRAM_BOT_TOKEN, CUSTOM_REPLY


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# Defining Functions
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    This function initializes a conversation with the bot.... 
    """
    #Declaring firstname
    first_name = update.message.from_user.first_name

    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello {first_name.split()[0]}\nI'm a bot, please talk to me!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
   """
    This function guides users on which commands to use....
   """
    #Declaring firstnam
    # first_name = update.message.from_user.first_name

   text = """
/start    =>       Starts a Convesation with DeepChat
/todolist =>       Tells DeepChat to get ready for TodoList Creation
/help     =>       Guidains command 
"""
   await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    ################################################################################### 
    ##                      Here comes DeepChat's Power                              ##
    ###################################################################################


async def todolist_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
        This function gets/fetch info from google calender
    
    """

    #Declaring firstnam
    # first_name = update.message.from_user.first_name

    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, this is your to-do list")

async def custom_reply_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Custom replies function"""
    first_name = update.message.from_user.first_name
    message_text = update.effective_message.text
    reply_text = CUSTOM_REPLY.get(message_text)
    if reply_text:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=reply_text + f"{first_name.split()[0]}")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Oops! I don't understand what you mean, {first_name.split()[0]}")

    message_text = update.effective_message.text
    reply_text = CUSTOM_REPLY.get(message_text)
    if reply_text:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=reply_text)


if __name__ == "__main__":
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    
    """
    Command Handlers to handle /start, /help, /todolist and (more to come) commands
    """
    start_handler = CommandHandler('start', start_command)
    help_handler = CommandHandler('help', help_command)
    todolist_handler = CommandHandler('todolist', todolist_command)
    custom_reply_handler = MessageHandler(filters.TEXT, custom_reply_command)
    application.add_handler(start_handler)
    application.add_handler(custom_reply_handler)
    application.add_handler(help_handler)
    application.add_handler(todolist_handler)

    # Polling
    application.run_polling()

