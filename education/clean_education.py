# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 08:31:12 2017

@author: Bernardo.Roschke
"""
import sqlite3 as lite

con = lite.connect('education.db')
cur = con.cursor()

with con:
    cur.execute('drop table if exists expectancy')
    cur.execute('drop table if exists gdp')
    