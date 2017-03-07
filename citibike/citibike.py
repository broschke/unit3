# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 15:09:52 2017

@author: Bernardo.Roschke
"""

import requests
from pandas.io.json import json_normalize
import sqlite3 as lite
import time
from dateutil.parser import parse 
import collections

con = lite.connect('citi_bike.db')
cur = con.cursor()

for i in range(0,60):
    print(i)
    r = requests.get('http://www.citibikenyc.com/stations/json')
    
    exec_time = parse(r.json()['executionTime'])
    
    with con:
        cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%Y-%m-%dT%H:%M:%S'),))
    
    id_bikes = collections.defaultdict(int) #defaultdict to store available bikes by station
    
    #loop through the stations in the station list
    for station in r.json()['stationBeanList']:
        id_bikes[station['id']] = station['availableBikes']
    
    #iterate through the defaultdict to update the values in the database
    with con:
        for k, v in id_bikes.items():
            cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = (?)", (exec_time.strftime('%Y-%m-%dT%H:%M:%S'),))
    time.sleep(60)
