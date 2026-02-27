from sqlalchemy import String, Integer, text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from dbfactory import engine
from sqlalchemy.orm import Session, declarative_base

Base = declarative_base()
class Carta(Base):#uma classe pra cada tabela
    __tablename__="cartinha"

    identificador: Mapped[str] = mapped_column(primary_key = True, server_default=text("gen_random_uuid()"))
    nome: Mapped[str] = mapped_column(String(30))
    cmc: Mapped[int] = mapped_column(Integer)
    texto: Mapped[str] = mapped_column(String(100))
    power: Mapped[int] = mapped_column(Integer)
    resistance: Mapped[int] = mapped_column(Integer)
    
    def __repr__(self) -> str:
        return f"Carta(identificador={self.identificador!r}, nome={self.nome!r}, texto={self.texto!r}, power={self.power!r}, resistance={self.resistance!r})"
        
Base.metadata.create_all(engine)
