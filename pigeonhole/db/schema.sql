DROP TABLE IF EXISTS datasets;

CREATE TABLE datasets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    raw_file TEXT NOT NULL,
    file_type INTEGER NOT NULL
);