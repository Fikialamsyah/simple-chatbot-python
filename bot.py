from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
import os
import openai

# Token bot Telegram
telegram_token = '6258970348:AAH-M-NegHWf1WJE_LtiSKUEHDvgja1xKU0'

# Token ChatGPT
openai_token = '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'

# Inisialisasi OpenAI ChatGPT
openai.api_key = openai_token
chatgpt_model = 'text-davinci-003'

# Fungsi untuk memproses pesan dan mengirimkan balasan dari ChatGPT
def process_message(update, context):
    message = update.message.text
    
    # Mengirimkan pesan ke ChatGPT
    response = openai.Completion.create(
        engine=chatgpt_model,
        prompt=message,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )
    
    # Mengirimkan balasan ke pengguna
    reply = response.choices[0].text.strip()
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply)

# Fungsi untuk menangani perintah /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Halo! Aku adalah Nufi bot yang didukung oleh ChatGPT. Mulai mengobrol dengan saya sekarang!")

# Fungsi utama
def main():
    updater = Updater(token=telegram_token, use_context=True)
    dispatcher = updater.dispatcher
    
    # Menangani perintah /start
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    
    # Menangani pesan
    message_handler = MessageHandler(Filters.text & ~Filters.command, process_message)
    dispatcher.add_handler(message_handler)
    
    # Memulai bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
