from database.database_gateway import CartinhaDBGateway


class Controlador:
    def __init__(self, db_gateway: CartinhaDBGateway) -> None:
        self.db_gateway = db_gateway

    def _to_dict(self, c):
        return {
            "identificador": c.identificador,
            "nome": c.nome,
            "cmc": c.cmc,
            "texto": c.texto,
            "power": c.power,
            "resistance": c.resistance
        }

    def get_card(self, page, offset):

        cartas = self.db_gateway.get_cartas()

        lista = [self._to_dict(c) for c in cartas]

        total = len(cartas)

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

        c = self.db_gateway.get_cartinha_by_id(cartinha_id)

        if not c:
            return None

        return self._to_dict(c)

    def update_card_by_id(self, cartinha_id, data):

        obj = self.db_gateway.update_cartinha_by_id(cartinha_id, data)

        if not obj:
            return None

        return True

    def delete_card_by_id(self, cartinha_id):

        ok = self.db_gateway.delete_cartinha_by_id(cartinha_id)

        if not ok:
            return None

        return True