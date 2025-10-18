# computer_infrastructure_assessment

## Setup

Follow these steps to create an isolated Python environment and install the packages listed in `requirements.txt`.

1. Create and activate a virtual environment (Linux/macOS):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Upgrade pip and install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

3. Quick verification (imports a couple of core packages):

```bash
python -c "import numpy as np, pandas as pd; print('numpy', np.__version__, 'pandas', pd.__version__)"
```

Notes
- `qiskit[visualization]` may install additional binary and GUI-related packages. If you only need the core quantum SDK, install `qiskit` without extras.
- Consider pinning package versions for reproducible installs. If you want, I can generate a pinned `requirements.txt` with specific versions.

If you'd like, I can also scaffold a small test or CI workflow that runs a smoke test after installation.