
import requests
import json
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Replace YOUR_TOKEN with your Telegram bot token
TOKEN = '5963162592:AAHuATzFgfCPIfQyX3R8qXlmElHjhFToxRg'

# Replace YOUR_API_KEY with your DeepAI API key
API_KEY = 'ebf44f0c-ab55-47e4-b157-54f6142ffa05'

# Initialize the Telegram bot
bot = telegram.Bot(token=TOKEN)

# Define the start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm a bot that can generate images from text. Just send me a message and I'll do the rest.")

# Define the generate command
def generate(update, context):
    # Get the text message from the user
    text = update.message.text

    # Send the text to the Text2Img API
    response = requests.post(
        'https://api.deepai.org/api/text2img',
        data={
            'text': text
        },
        headers={'api-key': API_KEY}
    )

    # Get the URL of the generated image from the API response
    generated_url = json.loads(response.text)['output_url']

    # Send the generated image to the user
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=generated_url)

# Initialize the updater and add the handlers
updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, generate))

# Start the bot
updater.start_polling()
updater.idle()
