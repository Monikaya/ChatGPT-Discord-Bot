import nextcord
from nextcord import Webhook
import os
import aiohttp
from dotenv import load_dotenv
from revChatGPT.revChatGPT import Chatbot

load_dotenv()
intents = nextcord.Intents.default()
intents.message_content = True

config = {"email": f"{os.getenv('CHATGPT_EMAIL')}", "password": f"{os.getenv('CHATGPT_PASS')}"}
chatbot = Chatbot(config, conversation_id=None)

bot = nextcord.Client(intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.event
async def on_message(message):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(f"{os.getenv('WEBHOOK')}", session=session)
        if message.webhook_id:
            return
        response = chatbot.get_chat_response(message.content, output="text")['message']
        await webhook.send(response)


@bot.slash_command()
async def reset(ctx):
    chatbot.reset_chat()
    await ctx.send("Your chat has been reset!")


bot.run(os.getenv("TOKEN"))
