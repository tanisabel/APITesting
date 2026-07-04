from utils.logger import logger

def test_delete_post(posts_api):
    logger.info("Eliminando post")

    response = posts_api.delete_post(2)

    logger.info(response.status_code)

    assert response.status_code == 200