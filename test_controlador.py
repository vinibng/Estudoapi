import pytest
from controladores.crud_controler import Controlador


class FakeCarta:
    def __init__(self, id):
        self.identificador = id
        self.nome = "teste"
        self.cmc = 1
        self.texto = "texto"
        self.power = 2
        self.resistance = 3


class FakeGateway:
    def get_cartas(self):
        return [FakeCarta("1"), FakeCarta("2"), FakeCarta("3")]

    def get_cartinha_by_id(self, id):
        if id == "1":
            return FakeCarta("1")
        return None

    def update_cartinha_by_id(self, id, data):
        if id == "1":
            return True
        return None

    def delete_cartinha_by_id(self, id):
        return id == "1"


@pytest.fixture
def controller():
    return Controlador(FakeGateway())


def test_get_card_paginated(controller):
    result = controller.get_card(page=1, offset=2)

    assert result["page"] == 1
    assert result["offset"] == 2
    assert result["total"] == 3
    assert len(result["data"]) == 2
    

def test_get_card_by_id_found(controller):
    result = controller.get_card_by_id("1")

    assert result is not None
    assert result["identificador"] == "1"


def test_get_card_by_id_not_found(controller):
    result = controller.get_card_by_id("999")

    assert result is None


def test_update_card_success(controller):
    result = controller.update_card_by_id("1", {"nome": "novo"})

    assert result is True


def test_update_card_fail(controller):
    result = controller.update_card_by_id("999", {})

    assert result is None


def test_delete_card_success(controller):
    result = controller.delete_card_by_id("1")

    assert result is True


def test_delete_card_fail(controller):
    result = controller.delete_card_by_id("999")

    assert result is None