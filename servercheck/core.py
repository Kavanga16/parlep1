def cpu_status(cpu: int, warn: int, alert: int) -> str:
    if cpu > alert:
        return "ALERT"
    if cpu > warn:
        return "WARN"
    return "OK"


def validate_cpu(cpu: int) -> None:
    if cpu < 0 or cpu > 100:
        raise ValueError("CPU must be in range 0-100")


def validate_thresholds(warn, alert) -> None:
    if not (0 < warn < alert < 100):
        raise ValueError("Thresholds must satisfy 0 < warn < alert < 100")


def exit_code(status: str) -> int:
    mapping = {"OK": 0, "WARN": 0, "ALERT": 1}
    return mapping.get(status, 3)
