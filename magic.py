from flask import Flask
import requests
from typing import NamedTuple
from flask import jsonify
from flask import request
import uuid
import sqlalchemy

flask =Flask(__name__)

class MagicCard(NamedTuple):
    nome: str
    cmc: int
    texto: str
    power: int
    resistance: int
    identificador: str

cartas: list[MagicCard] = []

@flask.post("/cartinha")#create
def post():
    dicionario_cartinha:dict = request.get_json()
    nome= dicionario_cartinha["nome"]
    cmc= dicionario_cartinha["cmc"]
    texto= dicionario_cartinha["texto"]
    power= dicionario_cartinha["power"]
    resistance= dicionario_cartinha["resistance"]
    cartas.append(MagicCard(nome=nome, cmc=cmc, texto=texto, power=power, resistance=resistance, identificador=str(uuid.uuid4())))
    return jsonify({"msg":"deu certo"}), 201

@flask.get("/cartinha")#read all
def get_cartinha():
    listacartinha=[]
    for cartinha in cartas:
        cartinha._asdict()
        listacartinha.append(cartinha._asdict())
    return jsonify(cartas=listacartinha), 200

@flask.get("/cartinha/<string:cartinha_id>")#read one
def get_cartinha_id(cartinha_id):
    for cartinha in cartas:
        if cartinha.identificador == cartinha_id:
            return jsonify(cartinha._asdict()), 200
        
@flask.put("/cartinha/<string:cartinha_id>")#update
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

@flask.delete("/cartinha/<string:cartinha_id>") #delete
def delete_cartinha_id(cartinha_id):
    for cartinha in cartas:
        if cartinha.identificador == cartinha_id:
                cartas.remove(cartinha)
                return jsonify({"msg": "item apagado"}), 200

flask.run()