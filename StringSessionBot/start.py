from Data import Data
from pyrogram import Client, filters
from telethon.tl.functions.users import GetFullUserRequest
from telethon import TelegramClient, events, Button
from pyrogram.types import InlineKeyboardMarkup
from Config import ALIVE_PIC, API_ID, API_HASH, BOT_TOKEN

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

help_msg = f"""

» click on generate button ; Then you'll get to see two buttons 
» 1.Pyrogram - For music bots 
» 2.Telethon - For all bots except music one !
» Choose what ya want ! 
» Submit API ID , API HASH , NUMBER , CODE !
» STRING WILL BE SENT TO SAVED MESSAGES ! ✨💫
____

Thx for using our bot ! ✨💫
"""

about_msg = f"""

** Alpha String Bot © **

Bot to generate session with privacy ! [©](https://t.me/NotReallyAlpha) 

[𝐃𝐄𝐯𝐄𝐬𝐇](https://t.me/iTz_DEv_xD) | [𝐀𝐋𝐏𝐇𝐀](https://t.me/NotReallyAlpha)

Language Used : Python
           
Contact Owner and Developers [here](https://t.me/BTS_CHAT_ZONE) 
"""

cmda_msg = f"""

**Available commands in Alpha Bot**

/start    - To start the bot ✨💫
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
$ If any suggestions   ••>>  [Alpha](t.me/NotReallyAlpha)

"""


# Start Message
@Alp.on(events.NewMessage(pattern="/start"))
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
