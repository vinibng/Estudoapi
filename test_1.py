def test_post_cartinha(client):
    payload = {
        "nome": "carta teste",
        "cmc": 1,
        "texto": "algum texto",
        "power": 2,
        "resistance": 3
    }

    response = client.post("/cartinha", json=payload)

    assert response.status_code == 201
    assert "identificador" in response.json


def test_get_cartinhas(client):
    response = client.get("/cartinha")

    assert response.status_code == 200
    assert "data" in response.json


def test_get_cartinha_by_id_not_found(client):
    response = client.get("/cartinha/id_inexistente")

    assert response.status_code == 404


def test_update_cartinha_not_found(client):
    response = client.put("/cartinha/id_inexistente", json={"nome": "novo"})

    assert response.status_code == 404


def test_delete_cartinha_not_found(client):
    response = client.delete("/cartinha/id_inexistente")

    assert response.status_code == 404