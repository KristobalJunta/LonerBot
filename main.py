#!/usr/bin/python3
# -*- coding: utf8 -*-

from fuzzywuzzy import process
import sqlite3


conn = sqlite3.connect("lonerbot.sqlite")
cur = conn.cursor()

cur.execute("SELECT * FROM voices;")
voices = cur.fetchall()

print(voices)

texts = [v[2] for v in voices]

query = input("query: ")
result = process.extract(query, texts)
print(result)
