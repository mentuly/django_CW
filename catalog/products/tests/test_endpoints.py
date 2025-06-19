import pytest
from django.urls import reverse

from .fixtures import product, product_discount, order


@pytest.mark.django_db
def test_product_list_empty(api_client):
    url = reverse("products:product-list")
    response = api_client.get(url)

    assert response.status_code == 200
    assert isinstance(response.data, list)
    assert response.data == []


@pytest.mark.django_db
def test_product_list(api_client, product, product_discount):
    url = reverse("products:product-list")
    response = api_client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 2
    assert isinstance(response.data, list)


@pytest.mark.django_db
def test_product_detail(api_client, product):
    url = reverse("products:product-detail", kwargs={"pk": product.pk})
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.data["name"] == product.name
    assert response.data["price"] == product.price
    assert response.data["discount"] == product.discount
    assert response.data["nomenclature"] == product.nomenclature
    assert response.data["category"] == product.category.id
