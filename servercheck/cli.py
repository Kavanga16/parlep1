import argparse
import json
import logging
import sys

from servercheck import __version__
from servercheck.core import cpu_status, validate_cpu


def main() -> int:
    parser = argparse.ArgumentParser(description="Check server CPU and return status")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("-n", "--name", required=True, help="server name")
    parser.add_argument("-c", "--cpu", required=True, type=int, help="cpu usage (0-100)")
    parser.add_argument("--json", action="store_true", help="output in json")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose logs to stderr")
    parser.add_argument("-q", "--quiet", action="store_true", help="only errors to stderr")

    args = parser.parse_args()

    level = logging.WARNING
    if args.verbose:
        level = logging.INFO
    if args.quiet:
        level = logging.ERROR

    logging.basicConfig(
        level=level,
        stream=sys.stderr,
        format="%(levelname)s: %(message)s",
    )

    name = args.name
    cpu = args.cpu

    logging.info("Parsed args: name=%s cpu=%s json=%s", name, cpu, args.json)

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
