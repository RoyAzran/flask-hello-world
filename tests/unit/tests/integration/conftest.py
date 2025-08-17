import os
import time
import signal
import socket
from multiprocessing import Process

import pytest

def _wait_for_port(host: str, port: int, timeout: float = 10.0):
    """Poll until a TCP port is open or timeout."""
    start = time.time()
    while time.time() - start < timeout:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            try:
                sock.connect((host, port))
                return True
            except OSError:
                time.sleep(0.2)
    raise TimeoutError(f"Server at {host}:{port} did not come up in {timeout}s")

def _run_server():
    # run the Flask app on a test port (avoid 5000 conflicts)
    from app import app
    app.run(host="127.0.0.1", port=5001)

@pytest.fixture(scope="session")
def live_server():
    proc = Process(target=_run_server, daemon=True)
    proc.start()
    try:
        _wait_for_port("127.0.0.1", 5001, timeout=15.0)
        yield "http://127.0.0.1:5001"
    finally:
        if proc.is_alive():
            # terminate more gently first
            os.kill(proc.pid, signal.SIGTERM)
            proc.join(timeout=3)
            if proc.is_alive():
                proc.terminate()
