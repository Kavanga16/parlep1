import sys


def cpu_status(cpu):
     if cpu > 75 :
         return "ALERT"
     if cpu > 50:
        return "WARN" 
     return "OK"

while True:
    name = input("Server name: ").strip()
    while True:   
        cpu_raw = input("CPU usage(0-100): ").strip()
        try:
            cpu = int(cpu_raw)
        except ValueError:
            print("CPU must be a number")
            continue   
        
        if cpu < 0 or cpu > 100:   
            print("CPU must be in range 0-100")
            continue
     
        status = cpu_status(cpu)
        print(f"{name:10} |  CPU: {cpu:>3}% | STATUS: {status} ")
        break
    while True:
        repeat = input("Check another? (y/n):").strip().lower()
        if repeat == "y":
            break
        if repeat == "n":
            sys.exit(0)
        print("Please enter y or n")
        
    


