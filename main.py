import nextcord
from nextcord import Webhook
import os
import aiohttp
import asyncio
from dotenv import load_dotenv
#from asyncChatGPT.asyncChatGPT import Chatbot
from revChatGPT.revChatGPT import Chatbot

intents = nextcord.Intents.default()
intents.message_content = True
load_dotenv()

config = {"email": f"{os.getenv('CHATGPT_EMAIL')}", "password": f"{os.getenv('CHATGPT_PASS')}"}

chatbot = Chatbot(config, conversation_id=None)

bot = nextcord.Client()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(f"{os.getenv('WEBHOOK')}", session=session)
        if message.webhook_id:
            return
        print(f"Message:{message}")
        print(f"Content: {message.content}")
        #response = chatbot.get_chat_response(message.content, output="text")['message']
        #await webhook.send(response)


bot.run(os.getenv("TOKEN"))
