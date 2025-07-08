from pyrogram import Client, filters
import openai
import asyncio
import random
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

bot = Client("gojoru_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def gpt_reply(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Gojoru, a funny, intelligent, anime-style bot who replies smartly."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

@bot.on_message(filters.text & ~filters.edited)
async def chat(client, message):
    if message.from_user.is_bot:
        return
    try:
        await message.chat.send_action("typing")
        await asyncio.sleep(random.uniform(0.6, 1.2))
        response = await gpt_reply(message.text)
        await message.reply(response)
    except Exception as e:
        await message.reply("Gojoru glitch mein chala gaya 😵‍💫")

bot.run()
