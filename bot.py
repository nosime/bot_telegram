import requests
import json
import emoji

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes



def get_balance():
    url = "https://api.smspool.net/request/balance?key=1mArejVW98MtXLxkHWnMe7X5b39vHP5m" 
    response = requests.get(url)

    data = response.json()
    balance = data["balance"]
    hir ="tett"
    return balance,hir
    
balance_value, hir_value = get_balance()
icon =emoji.emojize(":dizzy:")
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
async def sd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Balance: {balance_value}$')
async def sd1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Balance: {hir_value}${emoji.emojize(":dizzy:")}')

app = ApplicationBuilder().token("5511970076:AAHbXkdtloQ2fHt3qwrwAm0QZ2yCKfarV0I").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("sd", sd))
app.add_handler(CommandHandler("sd1", sd1))

app.run_polling()