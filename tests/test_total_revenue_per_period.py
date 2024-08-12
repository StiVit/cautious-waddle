from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_measure_total_revenue_for_given_period():
    response = client.get('/api/transactions/period/2024-01-02/2024-03-16')
    assert response.json() == 32573.0
    response = client.get('/api/transactions/period/2024-01-02/2024-01-03')
    assert response.json() == 710.0


def test_total_revenue_for_certain_number_of_days():
    response = client.get('/api/transactions/days/2024-01-02/10')
    assert response.json() == 6088.0


def test_total_revenue_for_certain_number_of_months():
    response = client.get('/api/transactions/months/2024-01-02/10')
    assert response.json() == 82060.0
