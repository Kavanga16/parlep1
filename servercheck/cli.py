import argparse
import json
import sys

from servercheck import __version__
from servercheck.core import cpu_status, validate_cpu


def main() -> int:
    parser = argparse.ArgumentParser(description="Check server CPU and return status")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("-n", "--name", required=True, help="server name")
    parser.add_argument("-c", "--cpu", required=True, type=int, help="cpu usage (0-100)")
    parser.add_argument("--json", action="store_true", help="output in json")

    args = parser.parse_args()
    name = args.name
    cpu = args.cpu

    try:
        validate_cpu(cpu)
    except ValueError:
        print("CPU must be in range 0-100", file=sys.stderr)
        return 2

    status = cpu_status(cpu)
    code = 1 if status == "ALERT" else 0

    if args.json:
        print(json.dumps({"name": name, "cpu": cpu, "status": status, "exit_code": code}))
    else:
        print(f"{name:10} | CPU: {cpu:>3}% | STATUS: {status}")

    return code


def cli() -> None:
    raise SystemExit(main())
