def cpu_status(cpu: int) -> str:
    if cpu > 75:
        return "ALERT"
    if cpu > 50:
        return "WARN"
    return "OK"


def validate_cpu(cpu: int) -> None:
    if cpu < 0 or cpu > 100:
        raise ValueError("CPU must be in range 0-100")


def exit_code(status: str) -> int:
    mapping = {"OK": 0, "WARN": 0, "ALERT": 1}
    return mapping.get(status, 3)
