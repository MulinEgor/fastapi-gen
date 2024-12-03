from api.{name}.repository import {capitalized_name}Repository
from api.{name}.schemas.response import {capitalized_name}ResponseSchema
from api.{name}.schemas.request import {capitalized_name}CreateSchema, {capitalized_name}UpdateSchema


class {capitalized_name}Service:
    def __init__(self, repository: {capitalized_name}Repository):
        self.repository = repository
        
    async def get(self, id: int) -> {capitalized_name}ResponseSchema:
        return await self.repository.get(id)
    
    async def get_all(self) -> List[{capitalized_name}ResponseSchema]:
        return await self.repository.get_all()
    
    async def create(self, data: {capitalized_name}CreateSchema) -> {capitalized_name}ResponseSchema:
        return await self.repository.create(data.model_dump())
    
    async def update(self, id: int, data: {capitalized_name}UpdateSchema) -> {capitalized_name}ResponseSchema:
        return await self.repository.update(id, data.model_dump())
    
    async def delete(self, id: int):
        return await self.repository.delete(id)
