CREATE TABLE IF NOT EXISTS accidents (
    id TEXT PRIMARY KEY,
    severity INTEGER,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    city TEXT,
    state TEXT,
    temperature FLOAT,
    humidity FLOAT,
    weather_condition TEXT,
    visibility FLOAT,
    wind_speed FLOAT,
    accident_duration INTERVAL
);

-- Index for faster querying
CREATE INDEX IF NOT EXISTS idx_state ON accidents(state);