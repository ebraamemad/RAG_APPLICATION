
from .BaseDataModel import BaseDataModel
from src.models.db_schemes import DataChunk
from .enums.DataBaseEnum import DataBaseEnum
from bson.objectid import ObjectId
from pymongo import InsertOne

class ChunkModel(BaseDataModel):

    def __init__(self, db_client: object):
        super().__init__(db_client=db_client)
        self.collection = self.db_client[DataBaseEnum.COLLECTION_CHUNK_NAME.value]

    async def create_chunk(self, chunk: DataChunk):
        result = await self.collection.insert_one(chunk.dict(by_alias=True, exclude_unset=True))
        chunk._id = result.inserted_id
        return chunk

    async def get_chunk(self, chunk_id: str):
        result = await self.collection.find_one({
            "_id": ObjectId(chunk_id)
        })

        if result is None:
            return None
        
        return DataChunk(**result)
#انت لما تديله ملف وعايزه يحوله الي chunks ويخنه في الداتا بيز متخلوش يمشي زي for loob يعني يعمل insert لكل chunk لوحده
#  ده هيبقي بطيء جدا لو عندك 1000 chunk مثلا
#  فممكن نعمل batch insert يعني نعمل insert لكل chunk في batch لوحده
#  يعني لو عندك 1000 chunk ممكن تقسمهم علي 10 batches كل batch فيها 100 chunk
#  وده هيبقي اسرع بكتير من انك تعمل insert لكل chunk لوحده

    async def insert_many_chunks(self, chunks: list, batch_size: int=100):

        for i in range(0, len(chunks), batch_size):
            batch = chunks[i:i+batch_size]

            operations = [
                InsertOne(chunk.dict(by_alias=True, exclude_unset=True))
                for chunk in batch
            ]

            await self.collection.bulk_write(operations)
        
        return len(chunks)

    async def delete_chunks_by_project_id(self, project_id: ObjectId):
        result = await self.collection.delete_many({
            "chunk_project_id": project_id
        })

        return result.deleted_count
    
    

    
