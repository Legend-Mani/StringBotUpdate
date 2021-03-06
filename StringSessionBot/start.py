import asyncio
import os
from Data import Data
from pyrogram import Client, filters
from telethon.tl.functions.users import GetFullUserRequest
from telethon import TelegramClient, events, Button
from telethon.tl.custom import button
from pyrogram.types import InlineKeyboardMarkup
from Config import API_ID, API_HASH, BOT_TOKEN

Alf = TelegramClient('Alf', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

ALPHA_IMG = "https://te.legra.ph/file/9a207e6e453a93ab2b165.jpg"

ALP_Button = [
        [
        Button.inline("๐ Click here to generate", data="generate_back")
        ],
        [
        Button.inline("โจ Tutorial ๐ซ", data="help"),
        Button.inline("โจ Contact ๐ซ", data="about")
        ],
        [
        Button.url("โจ Owner โค๏ธ", "https://t.me/NotReallyAlpha"),
        Button.url("โจ Group ๐", "https://t.me/BTS_CHAT_ZONE")
        ],
        [
        Button.inline("โจ Commands ๐ฑ", data="cmda"),
        Button.inline("โจ Alphaversion ๐ฅ", data="alphaversion")
        ]
        ]

help_msg = f"""

ยป click on generate button ; Then you'll get to see two buttons 
ยป 1.Pyrogram - For music bots 
ยป 2.Telethon - For all bots except music one !
ยป Choose what ya want ! 
ยป Submit API ID , API HASH , NUMBER , CODE !
ยป STRING WILL BE SENT TO SAVED MESSAGES ! โจ๐ซ
____

Thx for using our bot ! โจ๐ซ
"""

about_msg = f"""

** Alpha String Bot ยฉ **

Bot to generate session with privacy ! [ยฉ](https://t.me/NotReallyAlpha) 

[๐๐๐ฏ๐๐ฌ๐](https://t.me/iTz_DEv_xD) | [๐๐๐๐๐](https://t.me/NotReallyAlpha)

Language Used : Python
           
Contact Owner and Developers [here](https://t.me/BTS_CHAT_ZONE) 
"""

cmda_msg = f"""

**Available commands in Alpha Bot**

/start    - To start the bot โจ๐ซ
/generate - To start string generation !
/help     - To view the tutorial.
/about    - Details to contact the developer !

"""

alphaversion_msg = f"""

**Alpha Version**

$ Version Name     - end.2.0
$ Version started  - 01/05/2022
$ Updated by       - [Alpha](t.me/NotReallyAlpha)

**Updated features**

$ Added "commands" button for new users !
$ Added "Alpha Version" button !
$ Bug fixes 

**Upcoming update**

$ you can see next update on 15/05/2022 !
$ going to add cool pic : when the user starts the bot !

_____
$ If any suggestions   โขโข>>  [Alpha](t.me/NotReallyAlpha)

"""


# Start Message
@Alf.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       AlfBot = await event.client.get_me()
       bot_name = AlfBot.first_name
       bot_id = AlfBot.id
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheYashvi = event.chat_id
       firstname = replied_user.user.first_name
       userid = replied_user.user.id
       await event.client.send_file(TheYashvi,
                  ALPHA_IMG,
                  Data.START.format(msg.from_user.mention, mention),
                  buttons=ALP_Button)
