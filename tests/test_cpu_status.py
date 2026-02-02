from servercheck.cli import cpu_status


def test_cpu_status_ok():
    assert cpu_status(0) == "OK"
    assert cpu_status(30) == "OK"
    assert cpu_status(50) == "OK"


def test_cpu_status_warn():
    assert cpu_status(51) == "WARN"
    assert cpu_status(60) == "WARN"
    assert cpu_status(75) == "WARN"


def test_cpu_status_alert():
    assert cpu_status(76) == "ALERT"
    assert cpu_status(90) == "ALERT"
    assert cpu_status(100) == "ALERT"
