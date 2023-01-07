import pytest


@pytest.fixture()
def set_up():
    print("start")
    yield
    print('stop')


@pytest.fixture(scope='module')
def some():
    print("Начало")
    yield
    print('конец')
