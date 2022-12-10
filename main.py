import nextcord
from nextcord import Webhook
import os
import aiohttp
from dotenv import load_dotenv

async def generate_response(msg):
    return "piss"

bot = nextcord.Client()
load_dotenv()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(f"{os.getenv('WEBHOOK')}", session=session)
        if message.webhook_id:
            return
        response = await generate_response(message.content)
        await webhook.send(response)


bot.run(os.getenv("TOKEN"))
