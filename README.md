# Macro Regime Intelligence Lab

## 3D Market State Observatory

![Python](https://img.shields.io/badge/Python-3.14.6-3776AB?logo=python&logoColor=white)
![Environment](https://img.shields.io/badge/environment-uv-DE5FE9)
![Tests](https://img.shields.io/badge/tests-pytest-0A9EDC?logo=pytest&logoColor=white)
![Code Quality](https://img.shields.io/badge/lint%20%26%20format-Ruff-D7FF64)
![Type Safety](https://img.shields.io/badge/types-Mypy%20strict-2A6DB2)

A reproducible quantitative research laboratory for macro-financial regime discovery, forward stress modeling, temporal validation, and interpretable 2D and 3D market-state analysis.

> Current stage: research infrastructure and evidence baseline. No dataset, fitted model, backtest result, or performance claim has been published yet.

## Research Question

Can a small and economically defensible set of market and macro-financial indicators identify distinct market regimes and estimate near-term financial stress out of sample without temporal leakage?

## Research Objectives

- Build auditable macro-financial data and feature contracts.
- Detect market regimes without hiding instability or label ambiguity.
- Estimate forward financial stress under chronological validation.
- Separate observed evidence, model output, and interpretation.
- Produce reproducible analytical artifacts and explicit failure reports.

## Evidence Protocol

Every empirical claim must be supported by reproducible data, explicit mathematical definitions, temporal validation, tests, and inspectable artifacts.

1. Source data must include provenance, release timing, and availability information.
2. Feature definitions must be mathematically specified and unit tested.
3. Predictive evaluation must preserve chronological order.
4. Model performance must be measured on unseen future periods.
5. Figures must distinguish observed evidence from interpretation.
6. Limitations, negative results, and failure cases must be recorded.
7. Reproduction steps must identify the runtime, dependencies, and configuration.

## Version 1 Scope

- Audit macro-financial data sources and their temporal limitations.
- Build deterministic and tested financial feature calculations.
- Discover market regimes and evaluate their stability.
- Estimate forward stress probability with walk-forward validation.
- Produce interpretable static and interactive analytical figures.
- Record reproducibility metadata, failure cases, and limitations.

## Methodological Guardrails

- No random train-test split for time-dependent evaluation.
- No future information in features, labels, preprocessing, or model selection.
- No crisis-prediction claim without out-of-sample evidence and uncertainty analysis.
- No causal claim from statistical association alone.
- No visual result without a traceable data and transformation path.

## Current Engineering Baseline

The repository currently provides the minimum enforceable foundation for later research code:

- CPython 3.14.6 runtime pin.
- uv-managed dependency and lockfile contract.
- Installable `src`-layout Python package.
- Executable package identity smoke tests with pytest.
- Ruff lint and formatting gates.
- Project-wide strict Mypy policy for Python 3.14.
- Explicit repository boundaries for local data, caches, secrets, and generated artifacts.

GitHub Actions CI is the next engineering milestone. Until it is added, the quality gates below must be executed locally before each commit.

## Repository Structure

```text
.
├── .python-version
├── .gitignore
├── README.md
├── pyproject.toml
├── uv.lock
├── src/
│   └── macro_regime_intelligence_lab/
│       └── __init__.py
└── tests/
    └── test_package_contract.py
```

The structure is intentionally small. Data pipelines, features, models, figures, and research reports will be added only when their contracts and validation requirements are defined.

## Quick Start

### macOS / Linux / WSL2

```bash
git clone https://github.com/valeriusvarda/macro-regime-intelligence-lab.git
cd macro-regime-intelligence-lab
uv sync --locked --managed-python
```

### Native Windows PowerShell

```powershell
git clone https://github.com/valeriusvarda/macro-regime-intelligence-lab.git
Set-Location macro-regime-intelligence-lab
uv sync --locked --managed-python
```

The project uses uv to provision and manage the repository runtime. A separately activated global Python environment is not required.

## Quality Gates

Run the complete local verification suite from the repository root:

```bash
uv lock --check --managed-python
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked mypy src tests
uv run --locked pytest -q
```

Each command enforces a different contract:

| Gate | Contract |
|---|---|
| `uv lock --check` | Dependency resolution is synchronized with the project manifest. |
| `ruff check` | Python source satisfies the active lint rules. |
| `ruff format --check` | Formatting is deterministic and repository-consistent. |
| `mypy src tests` | Source and tests satisfy the strict static typing policy. |
| `pytest -q` | Executable package contracts pass. |

## Development Sequence

```text
Concept
  -> mathematical definition
  -> hand calculation
  -> implementation
  -> test
  -> artifact
  -> interpretation
  -> atomic commit
```

## Research Roadmap

| Phase | Objective | Status |
|---|---|---|
| 0 | Reproducible runtime, package, tests, linting, formatting, and strict typing | In progress — CI remains |
| 1 | Data provenance, release-time audit, and schema contracts | Planned |
| 2 | Deterministic macro-financial feature engine | Planned |
| 3 | Regime discovery and stability diagnostics | Planned |
| 4 | Forward stress estimation with walk-forward validation | Planned |
| 5 | Interpretable 2D/3D observatory and reproducible research report | Planned |

## Non-Goals

- This repository does not provide investment advice or execute trades.
- It does not claim to predict financial crises with certainty.
- It does not treat statistical association as causal proof.
- It does not present in-sample fit as evidence of real-world predictive validity.
- It does not optimize for visual complexity at the expense of interpretability.

## Project Standard

Success is not measured by feature count or lines of code. It is measured by correctness, reproducibility, temporal validity, inspectability, and the ability to defend each research decision with evidence.

