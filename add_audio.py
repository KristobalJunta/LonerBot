#!/usr/bin/python3
# -*- coding: utf8 -*-

import sqlite3
from config import config


conn = sqlite3.connect(config.get('db'))
cur = conn.cursor()

try:
    while True:
        filename = input("filename: ")
        text = input("text: ")

        cur.execute("INSERT INTO voices(filename, transcribed) VALUES (?, ?)", [filename, text])
        conn.commit()
        print("inserted\n")
except KeyboardInterrupt:
    print("\n\ndone")
    exit()
