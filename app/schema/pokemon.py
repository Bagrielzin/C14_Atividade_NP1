from pydantic import BaseModel

class Pokemon(BaseModel):
    id: int
    original_name: str
    name: str
    move: str
    description: str