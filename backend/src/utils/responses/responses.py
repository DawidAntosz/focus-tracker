from typing import Optional, Any, NoReturn
from fastapi import HTTPException
from starlette.responses import JSONResponse
from .base import ApiResponse
from .enums import ResponseStatus


class Responses:
    @staticmethod
    def custom(status_code: int, message: str, status: ResponseStatus = ResponseStatus.SUCCESS, data: Optional[Any] = None) -> JSONResponse:
        content = ApiResponse(status=status, message=message, data=data).model_dump()
        return JSONResponse(status_code=status_code, content=content)

    @staticmethod
    def success(message: str, data: Optional[Any] = None) -> ApiResponse:
        return ApiResponse(status=ResponseStatus.SUCCESS, message=message, data=data)

    @staticmethod
    def created(message: str, data: Optional[Any] = None) -> JSONResponse:
        content = ApiResponse(status=ResponseStatus.SUCCESS, message=message, data=data).model_dump()
        return JSONResponse(status_code=201, content=content)

    @staticmethod
    def updated(message: str = "Resource updated successfully", data: Optional[Any] = None) -> ApiResponse:
        return ApiResponse(status=ResponseStatus.SUCCESS, message=message, data=data)

    @staticmethod
    def deleted(message: str = "Resource deleted successfully") -> ApiResponse:
        return ApiResponse(status=ResponseStatus.SUCCESS, message=message)

    @staticmethod
    def raise_error(status_code: int, message: str, data: Optional[Any] = None) -> NoReturn:
        raise HTTPException(
            status_code=status_code,
            detail=ApiResponse(status=ResponseStatus.ERROR, message=message, data=data).model_dump()
        )
