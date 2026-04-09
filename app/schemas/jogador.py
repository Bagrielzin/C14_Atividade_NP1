from pydantic import BaseModel

class Jogador(BaseModel):
    nome: str
    deck: list = []
    colecao: list = []
    registro: bool = False