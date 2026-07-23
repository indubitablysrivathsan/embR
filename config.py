from pathlib import Path
import os

# ─── ROOT ─────────────────────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent

# ─── DATA ─────────────────────────────────────────────────────────────────────
DATA_ROOT = PROJECT_ROOT / "../candl/data"

# ─── RESEARCH ─────────────────────────────────────────────────────────────────
RESEARCH_ROOT = PROJECT_ROOT / "data"

# ─── DUCKDB ───────────────────────────────────────────────────────────────────
NSE_DB_PATH = DATA_ROOT / "nse.db"