from flask import jsonify, request, Blueprint
import uuid

from controladores.crud_controler import Controlador
from models.carta import MagicCard
from database.database_gateway import CartinhaDBGateway

gateway = CartinhaDBGateway()
cartinha_blueprint = Blueprint("cartinha", __name__)


@cartinha_blueprint.post("/cartinha")
def post():

    data = request.get_json()

    card = MagicCard(**data, identificador=str(uuid.uuid4()))

    gateway.create_cartinha(card)

    return jsonify(card.model_dump()), 201


@cartinha_blueprint.get("/cartinha")
def get_cartinha():

    page = request.args.get("page", default=1, type=int)
    offset = request.args.get("offset", default=5, type=int)

    resultado = Controlador(gateway).get_card(page, offset)

    return jsonify(resultado), 200


@cartinha_blueprint.get("/cartinha/<string:cartinha_id>")
def get_cartinha_id(cartinha_id):

    carta_unica = Controlador(gateway).get_card_by_id(cartinha_id)

    if not carta_unica:
        return jsonify({"msg": "carta não existe"}), 404

    return jsonify(carta_unica), 200


@cartinha_blueprint.put("/cartinha/<string:cartinha_id>")
def update_cartinha_id(cartinha_id):

    data = request.get_json()

    carta_arrumada = Controlador(gateway).update_card_by_id(cartinha_id, data)

    if not carta_arrumada:
        return jsonify({"msg": "carta não existe"}), 404

    return jsonify({"msg": "item alterado"}), 200


@cartinha_blueprint.delete("/cartinha/<string:cartinha_id>")
def delete_cartinha_id(cartinha_id):

    carta_apagada = Controlador(gateway).delete_card_by_id(cartinha_id)

    if not carta_apagada:
        return jsonify({"msg": "carta não existe"}), 404

    return jsonify({"msg": "item apagado"}), 200