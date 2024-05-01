from motor.motor_asyncio import AsyncIOMotorClient
from store.core.config import settings


class MongoClient:
    def __init__(self) -> None:
        self.__client: AsyncIOMotorClient = AsyncIOMotorClient(settings.DATABASE_URL)

    def get(self) -> AsyncIOMotorClient:
        return self.__client


db_client = MongoClient()
