import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from Addy import LOGGER, app, userbot
from Addy.core.call import Adarshu
from Addy.misc import sudo
from Addy.plugins import ALL_MODULES
from Addy.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("ᴀssɪsᴛᴀɴᴛ ᴄʟɪᴇɴᴛ ᴠᴀʀɪᴀʙʟᴇs ɴᴏᴛ ᴅᴇғɪɴᴇᴅ, ᴇxɪᴛɪɴɢ...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Addy.plugins" + all_module)
    LOGGER("Addy.plugins").info("sᴜᴄᴄᴇssғᴜʟʟʏ ɪᴍᴘᴏʀᴛᴇᴅ ᴍᴏᴅᴜʟᴇs...")
    await userbot.start()
    await Adarshu.start()
    try:
        await Adarshu.stream_call("https://graph.org/file/37508c2235191fa104e3f.mp4")
    except NoActiveGroupCall:
        LOGGER("Addy").error(
            "ᴘʟᴇᴀsᴇ ᴛᴜʀɴ ᴏɴ ᴛʜᴇ ᴠɪᴅᴇᴏᴄʜᴀᴛ ᴏғ ʏᴏᴜʀ ʟᴏɢ ɢʀᴏᴜᴘ\ᴄʜᴀɴɴᴇʟ.\n\nsᴛᴏᴘᴘɪɴɢ ʙᴏᴛ..."
        )
        exit()
    except:
        pass
    await Adarshu.decorators()
    LOGGER("Addy").info(
        "ᴍᴀᴅᴇ ʙʏ @TeamAddy"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("Addy").info("sᴛᴏᴘᴘɪɴɢ ᴄʜᴀᴍᴘᴜ's ᴍᴜsɪᴄ ʙᴏᴛ...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())