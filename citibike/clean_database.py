# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 20:47:27 2017

@author: Bernardo.Roschke
"""
import sqlite3 as lite

con = lite.connect('citi_bike.db')
cur = con.cursor()

with con:
    cur.execute('drop table if exists citibike_reference')
    cur.execute('drop table if exists available_bikes')
