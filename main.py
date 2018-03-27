#!/usr/bin/python3
# -*- coding: utf8 -*-

from fuzzywuzzy import process
import sqlite3
from config import config


conn = sqlite3.connect(config.get('db'))
cur = conn.cursor()

cur.execute("SELECT * FROM voices;")
voices = cur.fetchall()

print(voices)

texts = [v[2] for v in voices]

query = input("query: ")
result = process.extract(query, texts)
print(result)
