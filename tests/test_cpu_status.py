from servercheck.core import cpu_status, exit_code, validate_cpu


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


def test_validate_cpu():
    validate_cpu(0)
    validate_cpu(50)
    validate_cpu(100)
    try:
        validate_cpu(-1)
        assert False, "Expected ValueError for CPU < 0"
    except ValueError:
        pass
    try:
        validate_cpu(101)
        assert False, "Expected ValueError for CPU > 100"
    except ValueError:
        pass


def test_exit_code():
    assert exit_code("OK") == 0
    assert exit_code("WARN") == 0
    assert exit_code("ALERT") == 1
    assert exit_code("???") == 3
