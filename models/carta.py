from typing import Optional
from pydantic import BaseModel

class MagicCard(BaseModel):
    nome: str
    cmc: int
    texto: Optional[str] = None
    power: int
    resistance: int
    identificador: str