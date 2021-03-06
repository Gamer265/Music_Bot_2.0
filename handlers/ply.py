from os import path

from pyrogram import Client as Yonebot
from pyrogram.types import Message, Voice

from callsmusic import callsmusic, queues

import converter
from downloaders import youtube

from config import BOT_NAME as bn, DURATION_LIMIT
from helpers.filters import command, other_filters
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Yonebot.on_message(command("ply") & other_filters)
@errors
async def play(_, message: Message):

    lel = await message.reply("ð **Processing**")
    sender_id = message.from_user.id
    sender_name = message.from_user.first_name

    keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="ðð¨ð§ð ðð®ð¬ð¢ð ðð¨ð­ð¶ð¸",
                        url="https://t.me/KoraSupport")
                   
                ]
            ]
        )

    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"â {DURATION_LIMIT} minute(s) Too long audio! sorry i can't playâ¼ï¸"
            )

        file_name = get_file_name(audio)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )
    elif url:
        file_path = await converter.convert(youtube.download(url))
    else:
        return await lel.edit_text("â Please give me audio for playð¥²")

    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await lel.edit(f"#â£ **Queued** at position {position}!")
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        await message.reply_photo(
        photo="https://telegra.ph/file/fe77d94e2105721ce4353.jpg",
        reply_markup=keyboard,
        caption="â¶ï¸ **Playing** here the song requested byð¥{}!".format(
        message.from_user.mention()
        ),
    )
        return await lel.delete()
