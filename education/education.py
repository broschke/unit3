# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 14:20:04 2017

@author: bernardo.roschke
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlite3 as lite
import csv
import numpy as np
import matplotlib.pyplot as plt
url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"

r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

data = soup.findAll('tr', attrs=('class', 'tcont'))
data = data[:93]

country = [i.contents[1].string for i in data]
year = [int(i.contents[3].string) for i in data]
total = [int(i.contents[9].string) for i in data]
men = [int(i.contents[15].string) for i in data]
women = [int(i.contents[21].string) for i in data]

expectancy = pd.DataFrame(
        {'country' : country,
         'year' : year,
         'total' : total,
         'men' : men,
         'women' : women})
    
con = lite.connect('education.db')
cur = con.cursor()

expectancy.to_sql(name='expectancy', con=con)

#transposed GDP data with https://www.tableau.com/about/blog/2012/03/reshaping-data-made-easy-16353

with con:
    cur.execute('CREATE TABLE gdp (country_name text, year integer, gdp integer)')
    
with open('C:\\Users\\Bernardo.Roschke\\Dropbox\\Thinkful\\data\\unit 3\\education\\GDPtest.csv','r') as inputFile:
    inputReader = csv.reader(inputFile)
    for field in inputReader:
        #print(field)
        cur.execute('INSERT INTO gdp (country_name, year, gdp) VALUES (?, ?, ?);', field)

con.commit()

combined = pd.read_sql('select a.year, a.gdp, a.country_name, b.total, b.men, b.women from gdp a left join expectancy b on (a.year = b.year and a.country_name = b.country) where b.total is not null', con=con)

gdp = combined['gdp'].map(lambda x: float(x))
total = combined['total'].map(lambda x: int(x))
log_gdp = gdp.map(lambda x: np.log(x))

plt.scatter(log_gdp, total)
plt.xlabel('log_gdp')
plt.ylabel('years of education')
plt.show()