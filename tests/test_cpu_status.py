from servercheck.core import cpu_status, exit_code, validate_cpu, validate_thresholds


def test_cpu_status_ok():
    assert cpu_status(0, warn=50, alert=75) == "OK"
    assert cpu_status(30, warn=50, alert=75) == "OK"
    assert cpu_status(50, warn=50, alert=75) == "OK"  # граница


def test_cpu_status_warn():
    assert cpu_status(51, warn=50, alert=75) == "WARN"
    assert cpu_status(60, warn=50, alert=75) == "WARN"
    assert cpu_status(75, warn=50, alert=75) == "WARN"  # граница alert


def test_cpu_status_alert():
    assert cpu_status(76, warn=50, alert=75) == "ALERT"
    assert cpu_status(90, warn=50, alert=75) == "ALERT"
    assert cpu_status(100, warn=50, alert=75) == "ALERT"


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


def test_validate_thresholds():
    validate_thresholds(50, 75)  # ok

    try:
        validate_thresholds(75, 50)
        assert False, "Expected ValueError for warn >= alert"
    except ValueError:
        pass

    try:
        validate_thresholds(50, 50)
        assert False, "Expected ValueError for warn == alert"
    except ValueError:
        pass

    try:
        validate_thresholds(-1, 75)
        assert False, "Expected ValueError for warn < 0"
    except ValueError:
        pass

    try:
        validate_thresholds(50, 101)
        assert False, "Expected ValueError for alert > 100"
    except ValueError:
        pass
