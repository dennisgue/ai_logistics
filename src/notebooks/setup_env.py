# ============================================================
# Environment Setup for Reproducibility and Portability
# ============================================================
# This block ensures that all custom modules stored in the `src/` folder
# can be imported from any notebook, regardless of the environment
# (local VS Code, SageMaker Studio, or Colab).

import sys
from pathlib import Path

# Automatically detect the project root (one level above the notebook folder)
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Define the path to the source code directory
SRC_PATH = PROJECT_ROOT / "src"

# Add 'src/' to Python's search path if not already included
if str(SRC_PATH) not in sys.path:
    sys.path.append(str(SRC_PATH))


# Example usage:
# Place the following lines at the beginning of each notebook
# to automatically configure the environment and import your utilities:
#
# %run ./setup_env.py
# from utils_data import *
