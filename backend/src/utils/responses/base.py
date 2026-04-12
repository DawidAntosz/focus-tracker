from typing import Optional, Any
from pydantic import BaseModel
from .enums import ResponseStatus


class ApiResponse(BaseModel):
    status: ResponseStatus = ResponseStatus.SUCCESS
    message: str
    data: Optional[Any] = None
