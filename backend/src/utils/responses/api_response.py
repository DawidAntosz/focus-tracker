from typing import Optional, TypeVar, Generic
from pydantic import BaseModel
from .enums import ResponseStatus


T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    status: ResponseStatus = ResponseStatus.SUCCESS
    message: str
    data: Optional[T] = None
