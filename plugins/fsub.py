from info import REQ_CHANNEL, ADMINS
from utils import is_requested
from pyrogram import enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#Replace with actual admin user IDs

async def check_fsub(client, message):
    if not REQ_CHANNEL and message.from_user.id in ADMINS:
        return True

    is_allowed = await is_requested(client, message.from_user.id)
    if is_allowed:
        return True

    invite_link = (await client.create_chat_invite_link(REQ_CHANNEL, creates_join_request=True)).invite_link
    buttons = [
        [InlineKeyboardButton("Join Updates Channel", url=invite_link)],
        [InlineKeyboardButton("🔄 Try Again", callback_data=f"checksub#{message.id}")]
    ]
    await client.send_message(
        chat_id=message.from_user.id,
        text=(
            "**To get the movie, please follow these steps:**\n\n"
            "1. Click the **Join Updates Channel** button below.\n"
            "2. Then click the **Request to Join Channel** button.\n"
            "3. After that, click the **Try Again** button to get the movie link."
        ),
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode=enums.ParseMode.MARKDOWN
    )
    return False
