# Contributing

Thanks for your interest in improving this monorepo. This guide explains how to develop, test, and contribute changes safely.

- Code style and linting
  - Python: ruff (Libria/libria-meta/.ruff.toml) and PEP8 line-length via formatter
  - Type checks: mypy (Libria/libria-meta/mypy.ini)
  - Run locally: `pre-commit install && pre-commit run -a`

- Tests
  - Libria/meta: `pytest -q Libria/libria-meta/tests`
  - Add focused tests adjacent to modules you change

- Orchestrator
  - Start: `python -m libria_meta.services.mezan_orchestrator`
  - UI: `/ui`, `/bench/ui`, `/bench/ui/new` (job form)

- Benchmarks
  - CLI: `python -m libria_meta.cli.qapflow_cli --bench qaplib --modes hybrid --time-limit 30 --out results.json --html report.html`
  - HTTP: POST `/bench` JSON or use the `/bench/ui/new` form

- QAP modular repo
  - Set `QAP_MODULAR_REPO_PATH` to your solver repo `src` path
  - Use `QAPFLOW_SAFE_MODE=1` to disable external backend

- Auto mode policy
  - Override thresholds with `QAPFLOW_AUTO_POLICY="S,M"` (defaults 20,50)

- CI
  - GitHub Actions run tests on 3.9–3.12, upload coverage
  - Nightly OptiBench replay produces JSON+HTML and drift checks

Please keep PRs focused and include before/after notes or screenshots for UI changes.
