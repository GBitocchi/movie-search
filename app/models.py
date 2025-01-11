from pydantic import BaseModel
from typing import Optional, List

class Movie(BaseModel):
    Title: str
    Year: int
    imdbID: str

class IndexResponse(BaseModel):
    message: str
    count: int

class ErrorResponse(BaseModel):
    detail: str