from typing import NamedTuple
from flask import jsonify, request, Blueprint
import uuid
from sqlalchemy import true
from models.carta import MagicCard
from database.database_gateway import CartinhaDBGateway


gateway = CartinhaDBGateway()
class Controlador:
    





    def get_card(self, page, offset):
        cartas = gateway.get_cartas()

        lista = []

        for c in cartas:
            lista.append({
                "identificador": c.identificador,
                "nome": c.nome,
                "cmc": c.cmc,
                "texto": c.texto,
                "power": c.power,
                "resistance": c.resistance
            })

        total = len(lista)
        start = (page - 1) * offset
        end = start + offset
        paginated = lista[start:end]

        return {
            "page": page,
            "offset": offset,
            "total": total,
            "data": paginated
        }

    def get_card_by_id(self, cartinha_id):
        c = gateway.get_cartinha_by_id(cartinha_id)

        if not c:
            return None

        return {
            "identificador": c.identificador,
            "nome": c.nome,
            "cmc": c.cmc,
            "texto": c.texto,
            "power": c.power,
            "resistance": c.resistance
        }

    def update_card_by_id(self,cartinha_id):
        data = request.get_json()
        obj = gateway.update_cartinha_by_id(cartinha_id, data)

        if not obj:
            return None
        
        return obj

    def delete_card_by_id(self, cartinha_id):
        ok = gateway.delete_cartinha_by_id(cartinha_id)

        if not ok:
            return None

    