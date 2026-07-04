import pytest

from api.users_api import UsersApi
from api.posts_api import PostsApi

@pytest.fixture
def users_api():

    return UsersApi()

@pytest.fixture
def posts_api():

    return PostsApi()