from flask import Blueprint, Flask
from typing import NamedTuple
from flask import jsonify
from flask import request
import uuid
from models.carta import MagicCard


#ROTAS
cartas: list[MagicCard] = []
cartinha_blueprint = Blueprint("cartinha", __name__)

@cartinha_blueprint.post("/cartinha")#create
def post():
    dicionario_cartinha:dict = request.get_json()
    nome= dicionario_cartinha["nome"]
    cmc= dicionario_cartinha["cmc"]
    texto= dicionario_cartinha["texto"]
    power= dicionario_cartinha["power"]
    resistance= dicionario_cartinha["resistance"]
    cartas.append(MagicCard(nome=nome, cmc=cmc, texto=texto, power=power, resistance=resistance, identificador=str(uuid.uuid4())))
    return jsonify({"msg":"deu certo"}), 201

@cartinha_blueprint.get("/cartinha")#read all
def get_cartinha():
    listacartinha=[]
    for cartinha in cartas:
        cartinha._asdict()
        listacartinha.append(cartinha._asdict())
    return jsonify(cartas=listacartinha), 200

@cartinha_blueprint.get("/cartinha/<string:cartinha_id>")#read one
def get_cartinha_id(cartinha_id):
    for cartinha in cartas:
        if cartinha.identificador == cartinha_id:
            return jsonify(cartinha._asdict()), 200
    return jsonify({"msg":"carta não existe"}), 404

@cartinha_blueprint.put("/cartinha/<string:cartinha_id>")#update
def update_cartinha_id(cartinha_id):
    dicionario_cartinha:dict = request.get_json()
    nomenovo = dicionario_cartinha["nome"]
    cmcnovo = dicionario_cartinha["cmc"]
    textonovo = dicionario_cartinha["texto"]
    powernovo = dicionario_cartinha["power"]
    resistancenovo = dicionario_cartinha["resistence"]
    for cartinha in cartas:
        if cartinha.identificador == cartinha_id:
            cartinhanova = cartinha._replace(nome=nomenovo, cmc=cmcnovo, texto=textonovo, power=powernovo, resistance=resistancenovo) 
            cartas.append(cartinhanova)
            cartas.remove(cartinha)
            return jsonify({"msg":"item alterado"}), 200
    return jsonify({"msg":"carta não existe"}), 404

@cartinha_blueprint.delete("/cartinha/<string:cartinha_id>") #delete
def delete_cartinha_id(cartinha_id):
    for cartinha in cartas:
        if cartinha.identificador == cartinha_id:
                cartas.remove(cartinha)
                return jsonify({"msg": "item apagado"}), 200
    return jsonify({"msg":"carta não existe"}), 404
