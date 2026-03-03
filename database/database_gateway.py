from ast import stmt
from requests import Session
from sqlalchemy import Engine, select, update, delete
from sqlalchemy.orm  import sessionmaker
from connector.dbfactory import get_database_engine
from models.carta import MagicCard
from connector.cartinha_dao import CartinhaDao


class CartinhaDBGateway():
    def __init__(self) -> None:
        self.engine:Engine = get_database_engine()



    def create_cartinha(self, magic_card:MagicCard):
        Session = sessionmaker(self.engine)
        with Session() as session:
            CartinhaDao(
                identificador=magic_card.identificador,
                nome=magic_card.nome,
                cmc= magic_card.cmc,
                texto=magic_card.texto,
                power=magic_card.power,
                resistance= magic_card.resistance,
            )            
            session.commit()

    def get_cartas(self):
        Session = sessionmaker(self.engine)
        with Session() as session:
            stmt = select(CartinhaDao)
            session.execute(stmt).all()
        return

    def get_cartinha_by_id(self, magic_card_id:str):
        Session = sessionmaker(self.engine)
        with Session() as session:
            cartinha = session.get(CartinhaDao , magic_card_id)
            session.execute(cartinha).all()
        return 
            

    def update_cartinha_by_id(self,magic_card_id:str):
        Session =sessionmaker(self.engine)
        with Session() as session:
            cartinha = session.get(CartinhaDao , magic_card_id)
            stmt= update(CartinhaDao).where(cartinha).values()
            session.execute(stmt)
        return 


    def delete_cartinha_by_id(self,magic_card_id:str):
        with Session() as session:
            stmt =select(CartinhaDao).where(CartinhaDao.identificador.in_([MagicCard]))
            session.delete(CartinhaDao.identificador.session.get())
        return 