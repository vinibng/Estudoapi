from typing import NamedTuple

class MagicCard(NamedTuple):
    nome: str
    cmc: int
    texto: str
    power: int
    resistance: int
    identificador: str