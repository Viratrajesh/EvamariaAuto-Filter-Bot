import motor.motor_asyncio
from info import DATABASE_NAME, DATABASE_URI


class Database:
    
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.req = self.db[f"req-{REQ_CHANNEL}"]

    async def add_req(self, user_id):
        """Add a user request to the database."""
        try:
            await self.req.update_one(
                {"_id": int(user_id)},
                {"$set": {"user_id": int(user_id)}},
                upsert=True
            )
        except Exception as e:
            pass
            
    async def get_req(self, user_id):
        """Check if a user has already requested."""
        try:
            return True if await self.req.find_one({"_id": user_id}) else False
        except Exception as e:
            print(f"Error retrieving request: {e}")
            return False
        
    async def delete_all_req(self):
        """Delete all requests."""
        try:
            await self.req.delete_many({})
        except Exception as e:
            print(f"Error deleting requests: {e}")

    async def get_all_req_count(self):
        """Count all requests."""
        try:
            return await self.req.count_documents({})
        except Exception as e:
            print(f"Error counting requests: {e}")
            return 0

db = Database(DATABASE_URI, DATABASE_NAME)
