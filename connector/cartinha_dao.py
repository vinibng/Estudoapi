from sqlalchemy import String, Integer, text, Engine
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class CartinhaDao(Base):
    __tablename__="cartinha"
    identificador: Mapped[str] = mapped_column(primary_key = True, server_default=text("gen_random_uuid()"))
    nome: Mapped[str] = mapped_column(String(30))
    cmc: Mapped[int] = mapped_column(Integer)
    texto: Mapped[str] = mapped_column(String(100))
    power: Mapped[int] = mapped_column(Integer)
    resistance: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        return f"Carta(identificador={self.identificador!r}, nome={self.nome!r}, texto={self.texto!r}, power={self.power!r}, resistance={self.resistance!r})"

    @staticmethod
    def migrate_table(engine: Engine):
        Base.metadata.create_all(engine)