import pytest
from pytest_factoryboy import register
from .factories import UserFactory, SuperuserFactory

register(UserFactory)
register(SuperuserFactory)


@pytest.fixture()
def user(user_factory):
    return user_factory()


@pytest.fixture()
def superuser(superuser_factory):
    return superuser_factory()
