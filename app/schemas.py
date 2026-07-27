from pydantic import BaseModel

class Link(BaseModel):
    url: str

class ShortCode(BaseModel):
    code: str