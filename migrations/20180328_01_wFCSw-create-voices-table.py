"""
Create voices table
"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        "CREATE TABLE voices(id INTEGER PRIMARY KEY, filename VARCHAR(255) NOT NULL, transcribed TEXT NOT NULL);",
        "DROP TABLE voices;"
    ),
    step(
        "CREATE UNIQUE INDEX unq_voices_filename on voices(filename);",
        "DROP INDEX unq_voices_filename;"
    )
]

