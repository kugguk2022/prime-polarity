# Contributing

Thanks for helping make **prime-polarity** better!

## Dev setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pre-commit install
pytest -q
```

## PR checklist
- Add or update **tests**.
- Run `ruff` and `black` (or rely on pre-commit).
- Include a short before/after `prime-polarity score` snippet if you add a new transform.
