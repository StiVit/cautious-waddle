from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_transaction():
    data = {'date': '2024-01-01', 'product_id': 1, 'units_sold': 2, 'total_revenue': 1000, 'region': 'North America',
            'payment_method': 'Credit Card'}
    response = client.post("/api/transactions/", json=data)
    assert response.json()['date'] == '2024-01-01'
    assert response.json()['product_id'] == 1
    assert response.json()['total_revenue'] == 1000
    assert response.json()['region'] == 'North America'


def test_get_transaction():
    response = client.get('/api/transactions/1')
    assert response.json()['date'] == '2024-01-01'
    assert response.json()['product_id'] == 1
    assert response.json()['total_revenue'] == 1000
    assert response.json()['region'] == 'North America'


def test_update_transaction():
    data = {'date': '2024-01-01', 'product_id': 1, 'units_sold': 2, 'total_revenue': 1000, 'region': 'North America',
            'payment_method': 'Credit Card'}
    response = client.put('/api/transactions/1', json=data)
    assert response.json()['date'] == '2024-01-01'
    assert response.json()['product_id'] == 1
    assert response.json()['total_revenue'] == 1000
    assert response.json()['region'] == 'North America'


def test_delete_transction():
    response = client.delete('/api/transactions/260')
    assert response.json()['message'] == "Transaction deleted successfully"
