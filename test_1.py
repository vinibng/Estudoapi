import pytest
from controladores.crud_controler import Controlador
from database.database_gateway import CartinhaDBGateway
from models.carta import MagicCard


@pytest.fixture
def carta():
    return Controlador(CartinhaDBGatewayMock())


def test_get_card(carta: Controlador):

    result = carta.get_card(1, 2)
    assert result == {"page": [MagicCard], "offset": 1, "total": 2, "data": 1}

def test_get_card_id(carta:Controlador):

    result = carta.get_card_by_id("goblin2")
    assert result == MagicCard(
                nome="Goblin2",
                cmc=611,
                texto="O goblin2",
                power=662,
                resistance=112,
                identificador="goblin2",
            )

class CartinhaDBGatewayMock(CartinhaDBGateway):

    def get_cartas(self):
        return [
            MagicCard(
                nome="Goblin",
                cmc=616,
                texto="O goblin",
                power=666,
                resistance=111,
                identificador="goblin",
            ),
            MagicCard(
                nome="Goblin2",
                cmc=611,
                texto="O goblin2",
                power=662,
                resistance=112,
                identificador="goblin2",
            ),
        ]
    

    def get_cartinha_by_id(self, magic_card_id: str):
        return super().get_cartinha_by_id(magic_card_id)