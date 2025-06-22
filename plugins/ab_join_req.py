from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest
from info import ADMINS, REQ_CHANNEL
from database.join_req import db

@Client.on_chat_join_request(filters.chat([REQ_CHANNEL]))
async def join_reqs(client, join_req: ChatJoinRequest):
    # print(f"Request: {join_req.from_user.id}")
    
    try:
        user_id = join_req.from_user.id

        requested = await db.get_req(user_id) 
        if requested:
            return
        
        await db.add_req(user_id=user_id)
    except Exception as e:
        print(e)
