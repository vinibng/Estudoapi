from typing import Optional
from pydantic import BaseModel

class MagicCard(BaseModel):
    nome: str
    cmc: int
    texto: Optional[str] = None
    power: Optional[int] = None
    resistance: Optional[int] =None
    identificador: str