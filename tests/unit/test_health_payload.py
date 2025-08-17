import pytest
from app import health_payload

def test_health_payload_ok():
    assert health_payload(True) == {"status": "ok"}

def test_health_payload_fail():
    assert health_payload(False) == {"status": "fail"}

@pytest.mark.parametrize("flag,expected", [
    (True,  {"status": "ok"}),
    (False, {"status": "fail"}),
])
def test_health_payload_param(flag, expected):
    assert health_payload(flag) == expected
