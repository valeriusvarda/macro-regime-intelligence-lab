# Macro Regime Intelligence Lab

## 3D Market State Observatory

![Python](https://img.shields.io/badge/Python-3.14.6-3776AB?logo=python&logoColor=white)
![Environment](https://img.shields.io/badge/environment-uv-DE5FE9)
![Tests](https://img.shields.io/badge/tests-pytest-0A9EDC?logo=pytest&logoColor=white)
![Code Quality](https://img.shields.io/badge/lint%20%26%20format-Ruff-D7FF64)
![Type Safety](https://img.shields.io/badge/types-Mypy%20strict-2A6DB2)


An evidence-driven quantitative research laboratory built around one problem: financial markets change state, while many analytical systems are designed as if the data-generating process were stable.

> Current stage: research infrastructure and evidence baseline. No dataset, fitted model, backtest result, or performance claim has been published yet.

## The Problem

Volatility, correlation, liquidity, risk appetite, and policy transmission do not remain constant through time. Their relationships can reorganize during inflation shocks, liquidity contractions, crises, recoveries, and policy transitions.

A researcher observing the market at time `t` faces three constraints:

1. the true market regime is latent rather than directly observable;
2. future financial stress has not yet occurred;
3. only information released and available by time `t` may be used.

This makes the central challenge harder than producing a visually convincing cluster map or fitting a high-scoring model. The challenge is to determine whether a compact, economically defensible information set can identify a market state and estimate forward stress **without temporal leakage, hidden instability, or retrospective storytelling**.

## Research Decision

At each observation date, the system must attempt to:

1. infer the current latent market state from information available at that date;
2. estimate financial-stress risk over a defined future horizon;
3. quantify uncertainty, instability, and sensitivity to research choices;
4. preserve the evidence chain from source observation to final interpretation.

The primary research question is:

> Can a small and economically defensible set of market and macro-financial indicators identify distinct market regimes and improve near-term stress estimation out of sample, after release timing, model instability, and uncertainty are explicitly controlled?

A result is useful only if it survives chronological evaluation, timing audits, reasonable perturbations, transparent baseline comparison, and independent reproduction.

## Why Common Workflows Fail

| Failure mechanism | Research consequence |
|---|---|
| Revised data are treated as if they were known historically. | The model receives information that a real-time researcher could not have observed. |
| Random train-test splits are applied to time-dependent data. | Future structure leaks into model development and inflates apparent generalization. |
| One clustering output is presented as the true regime map. | Label ambiguity and sensitivity to seeds, windows, scaling, or model choice remain hidden. |
| In-sample fit is treated as predictive evidence. | Explanatory narratives are mistaken for forward validity. |
| Complex graphics substitute for an auditable evidence chain. | A persuasive figure cannot be traced back to source data and transformations. |
| Runtime, dependencies, and configuration are not reproducible. | Results cannot be independently regenerated or falsified. |

## Proposed Research System

The laboratory does not assume that one algorithm solves these failures. It responds to each failure mechanism with an explicit contract and a required form of evidence.

| Problem to solve | System response | Required evidence |
|---|---|---|
| Historical information availability is uncertain. | Build point-in-time data contracts containing provenance, release timing, revision policy, units, and missing-data semantics. | Availability audit showing what was knowable at each observation date. |
| Financial transformations can hide implementation error. | Define every feature mathematically before implementation and test deterministic calculations against hand-worked cases. | Specification, reference calculation, unit tests, and failure tests. |
| Market-state labels can be unstable or method-dependent. | Compare candidate regime models and measure sensitivity to seeds, windows, scaling, samples, and hyperparameters. | Stability diagnostics, transition analysis, and documented rejected models. |
| Forward-stress estimates can overfit historical crises. | Use expanding or rolling walk-forward evaluation with untouched future periods and simple baselines. | Fold-level out-of-sample metrics, calibration evidence, uncertainty, and baseline comparison. |
| Interpretation can outrun evidence. | Separate observed data, transformation, model output, diagnostic result, and human interpretation. | Traceable artifacts with explicit provenance and limitation notes. |
| Research results can depend on an unrecorded environment. | Lock the runtime and dependencies, enforce tests and static checks, and automate the gates in CI. | Clean-checkout reproduction and recorded verification results. |

## Falsifiable Hypotheses

The project will test rather than assume the following propositions:

- **H1 — Regime stability:** a compact indicator set can produce market-state distinctions that remain materially stable under reasonable methodological perturbations.
- **H2 — Forward usefulness:** regime-aware information can improve out-of-sample financial-stress estimation relative to predeclared simple baselines.
- **H3 — Diagnostic honesty:** instability, ambiguity, and failure can be detected and reported rather than hidden inside one final chart or score.

These hypotheses fail if, after timing controls and chronological validation:

- regime assignments change materially under minor and defensible research choices;
- predictive improvement disappears outside the development sample;
- results do not outperform the predeclared baselines;
- apparent performance depends on revised or unavailable information;
- uncertainty is too large to support the interpretation;
- a clean environment cannot reproduce the evidence.

A failed hypothesis is a valid research result. It must be recorded, not tuned away.

## Validation Contract

| Validation dimension | Question that must be answered |
|---|---|
| Data integrity | Where did each observation come from, when was it released, and could it have been known at time `t`? |
| Feature correctness | Does the implementation match the mathematical definition across normal, boundary, and failure cases? |
| Temporal validity | Is every preprocessing, fitting, selection, and evaluation step restricted to information available at that stage? |
| Regime validity | Are the inferred states distinct, persistent enough to interpret, and stable under reasonable perturbations? |
| Predictive usefulness | Does the system improve untouched future-period performance relative to predeclared baselines? |
| Calibration and uncertainty | Do estimated risks correspond to observed frequencies, and how uncertain are the conclusions? |
| Robustness | Does the conclusion survive plausible window, feature, model, and threshold changes? |
| Reproducibility | Can a clean checkout regenerate the same tested artifacts from declared inputs and configuration? |

Metric definitions, event horizons, baselines, and acceptance thresholds will be fixed before the relevant model comparison. They will not be chosen after inspecting the final test results.

## Evidence Protocol

Every empirical claim must be supported by reproducible data, explicit mathematical definitions, temporal validation, tests, and inspectable artifacts.

1. Source data must include provenance, release timing, and availability information.
2. Feature definitions must be mathematically specified and unit tested.
3. Predictive evaluation must preserve chronological order.
4. Model performance must be measured on unseen future periods.
5. Figures must distinguish observed evidence, model output, and interpretation.
6. Limitations, negative results, and failure cases must be recorded.
7. Reproduction steps must identify the runtime, dependencies, inputs, and configuration.

## Methodological Guardrails

- No random train-test split for time-dependent evaluation.
- No future information in features, labels, preprocessing, or model selection.
- No crisis-prediction claim without out-of-sample evidence, calibration, and uncertainty analysis.
- No causal claim from statistical association alone.
- No preferred model without comparison to predeclared simple baselines.
- No visual result without a traceable data and transformation path.
- No silent removal of unstable, contradictory, or negative results.

## Research Operating Loop

```text
Problem
  -> failure mechanism
  -> falsifiable hypothesis
  -> mathematical and data contract
  -> reference calculation
  -> implementation
  -> positive and negative tests
  -> out-of-sample evidence
  -> interpretation and limitations
  -> atomic commit
```

## Research Program

| Phase | Problem to resolve | Deliverable | Completion evidence | Status |
|---|---|---|---|---|
| 0 | How can every later result be independently verified? | Reproducible runtime, package contract, quality gates, and CI | Clean installation and automated checks on `main` | In progress — CI remains |
| 1 | What information was genuinely available at each historical date? | Point-in-time data and schema contracts | Provenance, release-lag, revision, unit, and missingness audit | Planned |
| 2 | Can each macro-financial signal be computed deterministically? | Tested feature engine | Mathematical specification, hand calculation, unit tests, and edge-case evidence | Planned |
| 3 | Do inferred market states represent stable structure or modeling noise? | Candidate regime models and stability diagnostics | Perturbation, persistence, transition, and rejected-model evidence | Planned |
| 4 | Do regime-aware signals improve forward-stress estimation? | Walk-forward benchmark system | Untouched future-period metrics, calibration, uncertainty, and baseline comparison | Planned |
| 5 | Can another researcher inspect the complete reasoning chain? | Interpretable 2D/3D observatory and research report | Reproducible figures, traceable artifacts, limitations, and failure report | Planned |

## Current Engineering Baseline

The repository currently provides the minimum enforceable foundation for later research code:

- CPython 3.14.6 runtime pin.
- uv-managed dependency and lockfile contract.
- Installable `src`-layout Python package.
- Executable package identity smoke tests with pytest.
- Ruff lint and formatting gates.
- Project-wide strict Mypy policy for Python 3.14.
- Explicit repository boundaries for local data, caches, secrets, and generated artifacts.

GitHub Actions CI is the next engineering milestone and is tracked in [Issue #1](https://github.com/valeriusvarda/macro-regime-intelligence-lab/issues/1). Until it is added, the quality gates below must be executed locally before each commit.

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

## Non-Goals

- This repository does not provide investment advice or execute trades.
- It does not claim to predict financial crises with certainty.
- It does not treat statistical association as causal proof.
- It does not present in-sample fit as evidence of real-world predictive validity.
- It does not optimize for model or visual complexity at the expense of interpretability.
- It does not hide null results, instability, or model failure.

## Project Standard

Success is not measured by feature count, lines of code, or visual complexity. It is measured by whether the project identifies a consequential problem, constructs a testable response, exposes the conditions under which that response fails, and allows another researcher to reproduce and challenge the evidence.
