.PHONY: help fmt fmt-check lint test check

PY=./.venv/Scripts/python.exe

help:
	@echo "Targets: lint | fmt | fmt-check | test | check"

fmt:
	$(PY) -m ruff format .

fmt-check:
	$(PY) -m ruff format --check .

lint:
	$(PY) -m ruff check .

test:
	$(PY) -m pytest -q

check: lint fmt-check test
