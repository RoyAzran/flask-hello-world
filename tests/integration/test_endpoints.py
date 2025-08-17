import requests

def test_health_endpoint(live_server):
    r = requests.get(f"{live_server}/health", timeout=5)
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_root_endpoint(live_server):
    r = requests.get(f"{live_server}/", timeout=5)
    assert r.status_code == 200
    assert "Hello CI/CD" in r.text
