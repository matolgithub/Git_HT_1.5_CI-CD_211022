import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from logistic.models import Product, Stock


# ---------Fixtures and factories block

@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def host_url():
    URL = '/api/v1/'
    return URL


@pytest.fixture()
def product_factory():
    def factory(*args, **kwargs):
        return baker.make(Product, *args, **kwargs)

    return factory


@pytest.fixture()
def stock_factory():
    def factory(*args, **kwargs):
        return baker.make(Stock, *args, **kwargs)

    return factory


# -----------Tests block

# Example test
def test_example():
    assert True, "Just test example"
