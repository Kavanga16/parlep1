![ci](https://github.com/Kavanga16/parlep1/actions/workflows/ci.yml/badge.svg)

# servercheck

Small CLI utility to evaluate server CPU status.

## Features

- Calculate CPU status: "OK", "WARN", "ALERT"
- Text output or JSON output
- Exit codes suitable for scripts/CI
- Tested with "pytest", formatted/linted with "ruff", CI via GitHub Actions
- Makefile shortcuts ("make check", "make fix")

## Requirements

- Python 3.x
- (Optional) GNU Make (MSY2) for "make check"

## Install

### PowerShell (Windows)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .

### Git Bash (MSYS2)

py -m venv .venv
source .venv/Scripts/activate
python -m pip install -e .

### Usage

- Help: servercheck
- Text output: servercheck -n api -c 60
- JSON output: servercheck -n api -c 90 --json
- Run as a module: python -m servercheck -n api -c 60

## Thresholds 

You can configure thresholds via CLI flags (highest priority) or environment variables.

Environment variables:
- "SERVERCHECK_WARN"
- "SERVERCHECK_ALERT"

Example (Git Bash):
'''bash
SERVERCHECK_WARN=10 SERVERCHECK_ALERT=20 servercheck -n api -c 15
'''

## Exit codes

- 0 --- OK/WARN
- 1 --- ALERT
- 2 --- Invalid arguments (e.g., CPU out of 0-100)
- 3 --- Unknown status (defensive fallback)

## Development

- Run lint + formatting check + tests(MSYS2):  
 make check

- Auto-fix lint and reformat: 
 make fix

- Run tests only:
 python -m pytest -q

 ## Project structure

 - servercheck/core.py --- pure logic (status/validation/helpers)
 - servercheck/cli.py --- CLI parsing and output formatting
 - tests/ --- unit + CLI + local HTTP server tests

 ## Roadmap

- Add more checks (e.g., URL health check subcommand)
- Improve CLI UX (more output formats, clearer errors)


