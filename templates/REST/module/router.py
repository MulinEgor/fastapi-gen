from fastapi import APIRouter, status, Depends
from typing import List

from api.{name}.config import {capitalized_name}ModuleConfig
from api.{name}.schemas.request import {capitalized_name}CreateSchema, {capitalized_name}UpdateSchema
from api.{name}.schemas.response import {capitalized_name}ResponseSchema
from api.{name}.service import {capitalized_name}Service
from api.{name}.dependencies import get_{name}_service


router = APIRouter(
    **{capitalized_name}ModuleConfig().model_dump()
)


@router.get(
    "/{id}",
    response_model={capitalized_name}ResponseSchema,
    status_code=status.HTTP_200_OK
)
async def get_{name}(
    id: int,
    service: {capitalized_name}Service = Depends(get_{name}_service)
) -> {capitalized_name}ResponseSchema:
    return await service.get(id)


@router.get(
    "/",
    response_model=List[{capitalized_name}ResponseSchema],
    status_code=status.HTTP_200_OK
)
async def get_all_{name}s(
    service: {capitalized_name}Service = Depends(get_{name}_service)
) -> List[{capitalized_name}ResponseSchema]:
    return await service.get_all()


@router.post(
    "/",
    response_model={capitalized_name}ResponseSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_{name}(
    payload: {capitalized_name}CreateSchema,
    service: {capitalized_name}Service = Depends(get_{name}_service)
) -> {capitalized_name}ResponseSchema:
    return await service.create(payload)


@router.put(
    "/{id}",
    response_model={capitalized_name}ResponseSchema,
    status_code=status.HTTP_200_OK
)
async def update_{name}(
    id: int,
    payload: {capitalized_name}UpdateSchema,
    service: {capitalized_name}Service = Depends(get_{name}_service)
) -> {capitalized_name}ResponseSchema:
    return await service.update(id, payload)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_{name}(
    id: int,
    service: {capitalized_name}Service = Depends(get_{name}_service)
) -> None:
    await service.delete(id)
