from typing import Optional, Any, NoReturn
from fastapi import HTTPException
from starlette.responses import JSONResponse
from .api_response import ApiResponse
from .enums import ResponseStatus


class Responses:

    @staticmethod
    def _build_response(status_code: int, status: ResponseStatus, message: str, data: Optional[Any] = None) -> JSONResponse:
        content = ApiResponse(status=status, message=message, data=data).model_dump()
        return JSONResponse(status_code=status_code, content=content)

    @staticmethod
    def success(message: str, data: Optional[Any] = None, status_code: int = 200) -> JSONResponse:
        return Responses._build_response(status_code, ResponseStatus.SUCCESS, message, data)

    @staticmethod
    def created(message: str, data: Optional[Any] = None) -> JSONResponse:
        return Responses._build_response(201, ResponseStatus.SUCCESS, message, data)

    @staticmethod
    def updated(message: str = "Resource updated successfully", data: Optional[Any] = None) -> JSONResponse:
        return Responses._build_response(200, ResponseStatus.SUCCESS, message, data)

    @staticmethod
    def deleted(message: str = "Resource deleted successfully") -> JSONResponse:
        return Responses._build_response(200, ResponseStatus.SUCCESS, message)

    @staticmethod
    def custom(
        status_code: int,
        message: str,
        status: ResponseStatus = ResponseStatus.SUCCESS,
        data: Optional[Any] = None
    ) -> JSONResponse:
        return Responses._build_response(status_code, status, message, data)

    @staticmethod
    def raise_error(status_code: int, message: str, data: Optional[Any] = None) -> NoReturn:
        raise HTTPException(
            status_code=status_code,
            detail=ApiResponse(status=ResponseStatus.ERROR, message=message, data=data).model_dump()
        )
