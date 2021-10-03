from pyrogram import Client as Yonebot
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Yonebot.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start_(client: Yonebot, message: Message):
    await message.reply_text(
        f"""<b>Hey there {format(
        message.from_user.mention)} !
               I am Abscissa an Advanced Music bot created by My Master 𝔸 N I Ꮶ E T for playing music in the voice chats of Telegram Groups & Channels.\n\n Send me /help for more info.
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "Commands", url="https://telegra.ph/commands-06-14-2")
                  ],[
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/Gamer_4560"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Support Group", url="https://t.me/Family_Group26"
                    )],[
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/AbscissaMusic_Bot?startgroup=true"
                    )
                ]
            ]
        ),
    )

@Yonebot.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(client: Yonebot, message: Message):
      await message.reply_text("""**Abscissa Music Bot is Online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/Gamer_4560")
                ]
            ]
        )
   )


@Yonebot.on_message(filters.command("help") & filters.private & ~filters.channel)
async def help(client: Yonebot, message: Message):
    await message.reply_text(
        f"""<b>Hey there {format(
        message.from_user.mention)}
        
        **Setting up**
        
1) Make bot admin (Group and in channel if use cplay)
2) Start a voice chat
3) Try /play [song name] for the first time by an admin
4) If userbot joined enjoy music, If not add @Abscissa_Userbot to your group and retry

**For Channel Music Play**

1) Make me admin of your channel 
2) Send /userbotjoinchannel in linked group
3) Now send commands in linked group 

Send Me /commands To Know My Features
        """)
        

@Yonebot.on_message(filters.command("commands") & filters.private & ~filters.channel)
async def commands(client: Yonebot, message: Message):
    await message.reply_text(
        f"""<b>Hey there {format(
        message.from_user.mention)} The Music Bot commands are as follows
        
        **Commands**
        
**=>>🎧 Song Playing 🎧**
- /play: Play the requestd song
- /play [yt url] : Play the given yt url
- /play [reply yo audio]: Play replied audio
- /dplay: Play song via deezer
- /splay: Play song via jio saavn
- /ytplay: Directly play song via Youtube Music

**=>> Playback **

- /player: Open Settings menu of player
- /skip: Skips the current track
- /pause: Pause track
- /resume: Resumes the paused track
- /end: Stops media playback
- /current: Shows the current Playing track
- /playlist: Shows playlist

*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
        """)
