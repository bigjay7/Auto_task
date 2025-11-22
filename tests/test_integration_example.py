# tests/test_integration_example.py
import pytest

from app import add_item, app, items


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as c:
        items.clear()
        yield c

def test_add_item_direct():
    # créer un contexte de requête POST et appeler directement la view
    items.clear()
    with app.test_request_context('/add', method='POST', data={'item': 'Banana'}):
        add_item()
    assert 'Banana' in items

def test_add_item_via_client(client):
    # utiliser le test client pour poster au endpoint
    resp = client.post('/add', data={'item': 'Apple'}, follow_redirects=False)
    assert resp.status_code == 302
    assert 'Apple' in items