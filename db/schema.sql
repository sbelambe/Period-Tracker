CREATE TABLE IF NOT EXISTS periods (
  id INTEGER PRIMARY KEY,
  start_date TEXT NOT NULL,    
  end_date   TEXT NOT NULL,  
  status     TEXT NOT NULL CHECK(status IN ('confirmed','predicted')),
  calendar_event_id TEXT,        -- GCal event id
  updated_at TEXT DEFAULT (datetime('now'))
);

-- Indexes for lookups by date and event id
CREATE INDEX IF NOT EXISTS idx_periods_date ON periods(start_date, end_date);
CREATE INDEX IF NOT EXISTS idx_periods_event ON periods(calendar_event_id);

-- stores incremental sync token to avoid re-downloading the entire calendar each time
-- keeps track of the event calendar being synced
-- if token is null, initial sync
-- else, sync_token<incremental sync value>
CREATE TABLE IF NOT EXISTS sync_state (
  id INTEGER PRIMARY KEY CHECK (id = 1),
  calendar_id TEXT DEFAULT 'primary',
  sync_token  TEXT,
  last_checked TEXT
);

INSERT OR IGNORE INTO sync_state (id) VALUES (1);
