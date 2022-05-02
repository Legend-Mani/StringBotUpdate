from Data import Data
from pyrogram import Client, filters
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events
from pyrogram.types import InlineKeyboardMarkup
from Config import ALIVE_PIC

ALPHA_PIC = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/9a207e6e453a93ab2b165.jpg"

# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, msg):
	user = await bot.get_me()
	mention = user["mention"]
	await bot.send_message(
		msg.chat.id,
                ALPHA_PIC,
		Data.START.format(msg.from_user.mention, mention),
		reply_markup=InlineKeyboardMarkup(Data.buttons)
	)
