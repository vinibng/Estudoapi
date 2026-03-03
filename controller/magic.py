from flask import Blueprint, Flask
from typing import NamedTuple
from flask import jsonify
from flask import request
import uuid
from models.carta import MagicCard
from database.database_gateway import CartinhaDBGateway

gateway = CartinhaDBGateway()
cartinha_blueprint = Blueprint("cartinha", __name__)

@cartinha_blueprint.post("/cartinha")#create
def post():
    data = request.get_json()

    card = MagicCard(
        nome=data["nome"],
        cmc=data["cmc"],
        texto=data["texto"],
        power=data["power"],
        resistance=data["resistance"],
        identificador=str(uuid.uuid4())
    )

    gateway.create_cartinha(card)

    return jsonify({"msg": "deu certo"}), 201

@cartinha_blueprint.get("/cartinha")#read all
def get_cartinha():
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

    return jsonify(lista), 200

@cartinha_blueprint.get("/cartinha/<string:cartinha_id>")#read one
def get_cartinha_id(cartinha_id):
    c = gateway.get_cartinha_by_id(cartinha_id)

    if not c:
        return jsonify({"msg": "carta não existe"}), 404

    return jsonify({
        "identificador": c.identificador,
        "nome": c.nome,
        "cmc": c.cmc,
        "texto": c.texto,
        "power": c.power,
        "resistance": c.resistance
    }), 200

@cartinha_blueprint.put("/cartinha/<string:cartinha_id>")#put/update
def update_cartinha_id(cartinha_id):
    data = request.get_json()
    obj = gateway.update_cartinha_by_id(cartinha_id, data)

    if not obj:
        return jsonify({"msg": "carta não existe"}), 404

    return jsonify({"msg": "item alterado"}), 200

@cartinha_blueprint.delete("/cartinha/<string:cartinha_id>")#delete
def delete_cartinha_id(cartinha_id):
    ok = gateway.delete_cartinha_by_id(cartinha_id)

    if not ok:
        return jsonify({"msg": "carta não existe"}), 404

    return jsonify({"msg": "item apagado"}), 200