from Data import Data
from pyrogram import Client, filters
from telethon.tl.functions.users import GetFullUserRequest
from telethon import TelegramClient, events, Button
from pyrogram.types import InlineKeyboardMarkup
from Config import ALIVE_PIC

Alp = TelegramClient('Alp', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

ALPHA_IMG = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/9a207e6e453a93ab2b165.jpg"

ALP_Button = [
        [
        Button.inline("👉 Click here to generate", data="generate_back")
        ],
        [
        Button.inline("✨ Tutorial 💫", data="help"),
        Button.inline("✨ Contact 💫", data="about")
        ],
        [
        Button.url("✨ Owner ❤️", "https://t.me/NotReallyAlpha"),
        Button.url("✨ Group 💜", "https://t.me/BTS_CHAT_ZONE")
        ],
        [
        Button.inline("✨ Commands 🔱", data="cmda"),
        Button.inline("✨ Alphaversion 🔥", data="alphaversion")
        ]
        ]

# Start Message
@TelegramClient.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       MigBot = await event.client.get_me()
       bot_name = MigBot.first_name
       bot_id = MigBot.id
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheMighty = event.chat_id
       firstname = replied_user.user.first_name
       userid = replied_user.user.id
       await event.client.send_file(TheMighty,
                  ALPHA_IMG,
                  Data.START.format(msg.from_user.mention, mention)
                  reply_markup=InlineKeyboardMarkup(Data.buttons))
