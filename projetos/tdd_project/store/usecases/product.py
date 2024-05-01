# fmt: skip
from typing import Dict, List
from uuid import UUID

import pymongo
from store.db.mongo import db_client
from store.models.product import ProductModel
from store.schemas.product import ProductIn, ProductOut, ProductUpdateOut, ProductUpdate
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from store.core.exceptions import InvalidInserctionException, NotFoundException


class ProductUsecase:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn) -> ProductOut:
        product_model = ProductModel(**body.model_dump())
        await self.collection.insert_one(product_model.model_dump())

        return ProductOut(**product_model.model_dump())

    async def get(self, id: UUID) -> ProductOut:
        result = await self.collection.find_one({"id": id})

        if not result:
            raise NotFoundException(message=f"Product not found with filter id: '{id}'")

        return ProductOut(**result)

    async def query(self) -> List[ProductOut]:
        return [ProductOut(**item) async for item in self.collection.find()]

    # fmt: of
    async def query_filter_price_or_quantity(self, body: Dict) -> List[ProductOut]:
        if body["filter_by"] not in ["price", "quantity"]:
            raise InvalidInserctionException(
                message=f"""Invalid filter: {body["filter_by"]}. Expected: 'price' or 'quantity'."""  # noqa: 1
            )
        elif body["op"] not in [">", "<"]:
            raise InvalidInserctionException(
                message=f"""Invalid operator: {body["op"]}. Expected: '>' or '<'."""
            )

        filter_by: str = body["filter_by"]
        op = "gt" if body["op"] == ">" else "lt"
        value = body["value"]
        filter = {filter_by: {f"${op}": value}}

        return [ProductOut(**item) async for item in self.collection.find(filter)]

    # fmt: on

    async def update(self, id: UUID, body: ProductUpdate) -> ProductUpdateOut:
        result = await self.collection.find_one_and_update(
            filter={"id": id},
            update={"$set": body.model_dump(exclude_none=True)},
            return_document=pymongo.ReturnDocument.AFTER,
        )

        if not result:
            raise NotFoundException(message=f"Product not found with filter id: '{id}'")

        return ProductUpdateOut(**result)

    async def delete(self, id: UUID):
        product = await self.collection.find_one({"id": id})
        if not product:
            raise NotFoundException(message=f"Product not found with filter id: '{id}'")

        result = await self.collection.delete_one({"id": id})

        return True if result.deleted_count > 0 else False


product_usecase = ProductUsecase()
