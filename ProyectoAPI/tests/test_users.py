from utils.logger import logger

def test_get_all_users(users_api):

    logger.info("Obteniendo usuarios")

    response = users_api.get_all_users()

    logger.info(response.status_code)

    assert response.status_code == 200

def test_get_user(users_api):

    logger.info("Inicia test: Obtener usuario")

    response = users_api.get_user(1)

    logger.info(response.status_code)

    body = response.json()

    logger.info(body)

    assert response.status_code == 200
    assert body["id"]  == 1
    assert body["username"] == "Bret"