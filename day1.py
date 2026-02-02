def cpu_status(cpu):
    if cpu > 75:
        return "ALERT"
    if cpu > 50:
        return "WARN"
    return "OK"


name = input("Server name:").strip()

while True:
    cpu_raw = input("CPU usage ()")

cpu_value = input("")
name = "db"
cpu = int(cpu_value)
status = cpu_status(cpu)


print(f"{name:10} |  CPU: {cpu:>3}% | STATUS: {status} ")


""" name = "api-prod"   
    cpu = 76

    status = cpu_status(cpu)
    print(f"{name:10} | CPU: {cpu:>3}% | STATUS: {status}")
    return 0 """
