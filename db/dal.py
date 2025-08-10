import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Optional

DB_PATH = Path(__file__).parent.parent / "data" / "period_tracker.db"
SCHEMA_PATH = Path(__file__).parent / "schema.sql"

@contextmanager
def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # allows dict-like access: row['start_date']
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()

def init_db():
    """Create tables if they don't exist."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with get_conn() as conn, open(SCHEMA_PATH, "r") as f:
        conn.executescript(f.read())
        
# SYNC TOKEN HANDLING
def get_sync_token() -> Optional[str]:
    with get_conn() as conn:
        cur = conn.execute("SELECT sync_token FROM sync_state WHERE id = 1")
        row = cur.fetchone()
        return row["sync_token"] if row else None

def set_sync_token(token: Optional[str]):
    with get_conn() as conn:
        conn.execute("""
            UPDATE sync_state
            SET sync_token = ?, last_checked = datetime('now')
            WHERE id = 1
        """, (token,))
        
def add_period():
    pass

def update_period_dates():
    pass

def find_period_by_event_id():
    pass

def get_confirmed_periods():
    pass

def delete_predicted_periods():
    pass