# Environment Integrity Audit

## EG Audit Findings

| Check | Command / Source | Observed State | Expected State | Classification |
|---|---|---|---|---|
| EG-001 Declared as prod dependency? | `pyproject.toml` `[project] dependencies` | Yes (`"rapidfuzz>=3.14,<4.0"`) | Yes | HEALTHY |
| EG-002 Only dev/optional? | `pyproject.toml` | No | No | HEALTHY |
| EG-003 Does prod import it? | Source code | Yes | Yes | HEALTHY |
| EG-004 Which exact module? | `src/recongraph/matching/signals.py` | `from rapidfuzz import fuzz` | `from rapidfuzz import fuzz` | HEALTHY |
| EG-005 Prev suite ran under different env? | Local state vs reported | Yes | Yes | LOCAL_ENVIRONMENT_DRIFT |
| EG-006 `pytest` resolves to same interpreter? | `which python` / `which pytest` | Yes (`/opt/anaconda3/bin/python` / `pytest`) | Yes | HEALTHY |
| EG-007 Install works via documented cmds? | `README.md` is empty, `pip install -e .[dev]` is standard | Yes | Yes | DOCUMENTATION_DEFECT (missing docs) |
| EG-008 Reproducibility defect exists? | `pytest` failed collection | Yes | No | LOCAL_ENVIRONMENT_DRIFT |
| EG-009 Defect is declaration or local? | `pip show rapidfuzz` | Local | Local | LOCAL_ENVIRONMENT_DRIFT |
| EG-010 Smallest legitimate fix? | Local environment | Run `pip install -e .[dev]` | Restored environment | LOCAL_ENVIRONMENT_DRIFT |

## Root Cause
The `rapidfuzz` dependency is correctly declared in `pyproject.toml` as a primary project requirement. However, the current active Python interpreter (`/opt/anaconda3/bin/python`) does not have the package installed (`WARNING: Package(s) not found: rapidfuzz`). This proves the previous test suite execution (which reported 251 passing tests) was executed in a different local environment (likely a different `venv` or global installation) that contained `rapidfuzz`. The repository's declaration itself is fully sound.

## Proposed Fix
Because this is purely a local environment drift issue, the fix is to restore the environment from the repository's configuration by running the standard Python package installation command:
`pip install -e .[dev]`
