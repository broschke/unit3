# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 15:47:04 2017

@author: bernardo.roschke
"""

import sqlite3 as lite

con = lite.connect('weather.db')
cur = con.cursor()

with con:
    cur.execute('drop table if exists daily_temp')