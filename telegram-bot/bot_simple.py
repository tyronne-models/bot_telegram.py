from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = "8077066109:AAHasKoLBxI30WjDNcjBeY1eNd-2uYPac_I"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Quiero entrar al VIP🔱", callback_data="vip")],
        [InlineKeyboardButton("quiero entrar a OnlySpainAmateur🔞🧁", callback_data="amateur")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text("¡Bienvenido! 👋\n\nElige la opción que te interese:", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "vip":
        mensaje_vip = "Hola si estas interesado en entrar a OnlySpainVIP🧁 ✨ \n\nPaga por Paypal 20€\nA este enlace↘️\nhttps://www.paypal.com/paypalme/OnlyspainES\n\nAl hacer el pago ✅\nEnvia el comprobante a @jesus_gil00"
        await query.edit_message_text(text=mensaje_vip)
        
    elif query.data == "amateur":
        await query.edit_message_text(
            text="🔞 Redirigiendo a OnlySpainAmateur...",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("✨ Unirse a OnlySpainAmateur", url="https://t.me/+1BLNrL1Bc79mNzNk")]
            ])
        )

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    print("🤖 Bot iniciado - Esperando /start...")
    application.run_polling()

if __name__ == "__main__":

    main()
