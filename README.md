# servercheck

Small CLI utility to evaluate server CPU status.

## Usage

Pretty output:
python -m servercheck -n api -c 60

JSON output:
python -m servercheck -n api -c 90 --json

## Exit codes

0 - OK/WARN
1 - ALERT
2 - Invalid arguments (e.g., cpu out of 0-100)

