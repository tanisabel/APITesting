from utils.logger import logger

def test_create_post(posts_api):

    body = {
        "title": "Mi primer post",
        "body": "Mi nombre es Tanya Arteaga",
        "userId": 2
    }

    logger.info("Creando nuevo post")

    response = posts_api.create_post(body)

    response_body = response.json()

    logger.info(response_body)

    assert response.status_code == 201
    assert response_body["title"] == body["title"]
    assert response_body["body"] == body["body"]
    assert response_body["userId"] == body["userId"]