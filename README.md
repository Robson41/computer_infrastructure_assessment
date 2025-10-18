# computer_infrastructure_assessment

## Setup

Steps to install the packages listed in `requirements.txt`.

1. Upgrade pip and install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

2. Quick verification (imports a couple of core packages):

```bash
python -c "import numpy as np, pandas as pd; print('numpy', np.__version__, 'pandas', pd.__version__)"
```