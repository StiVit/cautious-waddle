from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_products():
    data = {"product_category": "Home Appliances", "product_name": "Test1", "unit_price": 0}
    response = client.post("/api/products/", json=data)
    assert response.status_code == 200
    assert response.json()['product_name'] == 'Test1'
    assert response.json()['unit_price'] == 0


def test_get_product():
    response = client.get("/api/products/2")
    assert response.json()['product_name'] == 'Dyson V11 Vacuum'
    assert response.json()['unit_price'] == 499.99


def test_update_product():
    data = {"product_category": "Home Appliances", "product_name": "Test3", "unit_price": 10.00}
    resource = client.put("/api/products/1", json=data)
    assert resource.json()['product_name'] == "Test3"
    assert resource.json()['unit_price'] == 10.00
    assert resource.json()['product_category'] == "Home Appliances"
