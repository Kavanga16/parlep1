import json
import subprocess
import sys


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    cmd = [sys.executable, "-m", "servercheck", *args]
    return subprocess.run(cmd, capture_output=True, text=True)


def test_cli_warn_text():
    r = run_cli("-n", "api", "-c", "60")
    assert r.returncode == 0
    assert "STATUS: WARN" in r.stdout
    assert r.stderr == ""


def test_cli_alert_json():
    r = run_cli("-n", "api", "-c", "90", "--json")
    assert r.returncode == 1
    data = json.loads(r.stdout)
    assert data["name"] == "api"
    assert data["cpu"] == 90
    assert data["status"] == "ALERT"
    assert data["exit_code"] == 1
    assert r.stderr == ""


def test_cli_out_of_range():
    r = run_cli("-n", "api", "-c", "200")
    assert r.returncode == 2
    assert r.stdout == ""
    assert "CPU must be in range 0-100" in r.stderr
