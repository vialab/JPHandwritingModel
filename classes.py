from fastapi import HTTPException, status
from pydantic import BaseModel

class FileNotImageHTTPException(HTTPException):
    def __init__(self, message: str) -> None:
        super().__init__(status.HTTP_400_BAD_REQUEST, message)

class FileDoesNotExistHTTPException(HTTPException):
    def __init__(self, message: str) -> None:
        super().__init__(status.HTTP_400_BAD_REQUEST, message)

class PredictionFormResponse(BaseModel):
    romaji: str
    prediction: str