from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from connector.dbfactory import get_database_engine
from connector.cartinha_dao import CartinhaDao
from models.carta import MagicCard


class CartinhaDBGateway:

    def __init__(self):
        self.engine = get_database_engine()
        self.Session = sessionmaker(bind=self.engine)

    def create_cartinha(self, magic_card: MagicCard):
        with self.Session() as session:
            obj = CartinhaDao(
                identificador=magic_card.identificador,
                nome=magic_card.nome,
                cmc=magic_card.cmc,
                texto=magic_card.texto,
                power=magic_card.power,
                resistance=magic_card.resistance,
            )
            session.add(obj) #esta adicionando
            session.commit()

    def get_cartas(self):
        with self.Session() as session:
            stmt = select(CartinhaDao)
            result = session.execute(stmt).scalars().all()
            return result

    def get_cartinha_by_id(self, magic_card_id: str):
        with self.Session() as session:
            return session.get(CartinhaDao, magic_card_id)

    def update_cartinha_by_id(self, magic_card_id: str, data: dict):
        with self.Session() as session:
            obj = session.get(CartinhaDao, magic_card_id)

            if not obj:
                return None

            obj.nome = data["nome"]
            obj.cmc = data["cmc"]
            obj.texto = data["texto"]
            obj.power = data["power"]
            obj.resistance = data["resistance"]

            session.commit()
            return obj

    def delete_cartinha_by_id(self, magic_card_id: str):
        with self.Session() as session:
            obj = session.get(CartinhaDao, magic_card_id)

            if not obj:
                return False

            session.delete(obj)
            session.commit()
            return True