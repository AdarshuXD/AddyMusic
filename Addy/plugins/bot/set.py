import random
from typing import Union

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.errors import MessageNotModified
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    InputMediaVideo,
    Message,)

from TeamXBharat import app, PH_ON, GB 
from TeamXBharat.plugins.tools.stats import *
from TeamXBharat.utils.database import (
    add_nonadmin_chat,
    get_authuser,
    get_authuser_names,
    get_playmode,
    get_playtype,
    get_upvote_count,
    is_nonadmin_chat,
    is_skipmode,
    remove_nonadmin_chat,
    set_playmode,
    set_playtype,
    set_upvotes,
    skip_off,
    skip_on,
    get_served_users,
)
from TeamXBharat.utils.decorators.admins import ActualAdminCB
from TeamXBharat.utils.decorators.language import language, languageCB
from TeamXBharat.utils.inline.settings import (
    auth_users_markup,
    playmode_users_markup,
    setting_markup,
    vote_mode_markup,
)
from TeamXBharat.utils.inline.start import private_panel
from config import BANNED_USERS, OWNER_ID

#--------------------------------------------

#--------------------------------------------




@app.on_callback_query(filters.regex("gib") & ~BANNED_USERS)
@languageCB
async def gib_repo(client, CallbackQuery, _):
    LUI = random.choice(GB)
    medx = InputMediaVideo(media=LUI, caption="ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴄᴀᴛᴇɢᴏʀʏ ғᴏʀ\nᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ɢᴇᴛ ʜᴇʟᴩ.\nᴀsᴋ ʏᴏᴜʀ ᴅᴏᴜʙᴛs ᴀᴛ")
    await CallbackQuery.edit_message_media(media=medx,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="ᴏᴡɴᴇʀ", url="https://t.me/SexyCoder"
                    ),
                    
                    InlineKeyboardButton(
                        text="ʀᴇᴘᴏ", url="https://github.com/TheTelegramSupport"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="ᴄʟᴏsᴇ", callback_data="close"
                    )
                ],
            ]
        ),
    )




@app.on_callback_query(filters.regex("lood") & ~BANNED_USERS)
@languageCB
async def support(client, CallbackQuery, _):
    await CallbackQuery.edit_message_text(
        text="ʜᴇʀᴇ ᴀʀᴇ ꜱᴏᴍᴇ ɪᴍᴘᴏʀᴛᴀɴᴛ ʟɪɴᴋꜱ.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Coder", url="https://t.me/SexyCoder"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="Official Addy", url="https://t.me/OfficialAddy"
                    ),

                    InlineKeyboardButton(
                        text="ꜰᴜɴɴʏ", url="https://t.me/Horneygram"
                    ),
                    
                ],
                [
                    InlineKeyboardButton(
                        text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/SexyCoder"
                    ),

                    InlineKeyboardButton(
                        text="ᴄʜᴀᴛᴛɪɴɢ", url="https://t.me/AddySupport"
                    ),
                    
                ],
                [
                    InlineKeyboardButton(
                        text="ʙᴀᴄᴋ", callback_data=f"settingsback_helper"
                    )
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("support") & ~BANNED_USERS)
@languageCB
async def support(client, CallbackQuery, _):
    LULI = random.choice(PH_ON)
    med = InputMediaPhoto(media=LULI, caption="ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴄᴀᴛᴇɢᴏʀʏ ғᴏʀ\nᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ɢᴇᴛ ʜᴇʟᴩ.\nᴀsᴋ ʏᴏᴜʀ ᴅᴏᴜʙᴛs ᴀᴛ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ\n\nᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /")
    await CallbackQuery.edit_message_media(media=med,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=_["H_B_13"], callback_data=f"help_callback hb13"
                    ),
                    InlineKeyboardButton(
                        text=_["H_B_14"], callback_data=f"help_callback hb14"
                    ),
                    InlineKeyboardButton(
                        text=_["H_B_15"], callback_data=f"help_callback hb15"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text=_["H_B_16"], callback_data=f"help_callback hb16"
                    ),
                    InlineKeyboardButton(
                        text=_["H_B_17"], callback_data=f"help_callback hb17"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="◁", callback_data="settings_back_helper",
                    ),
                    InlineKeyboardButton(
                        text="ʜᴏᴍᴇ", callback_data="settingsback_helper"
                    ),
                    InlineKeyboardButton(
                        text="▷", callback_data=f"randi"
                    )
                ],
            ]
        ),
    )




@app.on_callback_query(filters.regex("suppor") & ~BANNED_USERS)
@languageCB
async def support(client, CallbackQuery, _):
    LUL = random.choice(PH_ON)
    medi = InputMediaPhoto(media=LUL, caption="ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴄᴀᴛᴇɢᴏʀʏ ғᴏʀ\nᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ɢᴇᴛ ʜᴇʟᴩ.\nᴀsᴋ ʏᴏᴜʀ ᴅᴏᴜʙᴛs ᴀᴛ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ\n\nᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /")
    await CallbackQuery.edit_message_media(media=medi,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=_["H_B_13"], callback_data=f"help_callback hb13"
                    ),
                    InlineKeyboardButton(
                        text=_["H_B_14"], callback_data=f"help_callback hb14"
                    ),
                    InlineKeyboardButton(
                        text=_["H_B_15"], callback_data=f"help_callback hb15"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text=_["H_B_16"], callback_data=f"help_callback hb16"
                    ),
                    InlineKeyboardButton(
                        text=_["H_B_17"], callback_data=f"help_callback hb17"
                    ),
                ],                
                [
                    InlineKeyboardButton(
                        text="◁", callback_data="settings_back_helper",
                    ),
                    InlineKeyboardButton(
                        text="ʜᴏᴍᴇ", callback_data="settingsback_helper"
                    ),
                    InlineKeyboardButton(
                        text="▷", callback_data=f"randi"
                    )
                ],
            ]
        ),
    )
