import requests
import sqlite3 as lite
import datetime

cities = {'Boston': '42.331960,-71.020173',
		  'Chicago': '41.837551,-87.681844',
		  'Denver': '39.761850,-104.881105',
		  'Salt_Lake_City': '40.778996,-111.932630',
		  'Washington_DC': '38.904103,-77.017229'}

key = '0f5a185898187109efc70c50e4a59b9d'

end_date = datetime.datetime.now()

url = 'https://api.forecast.io/forecast/'+key

con = lite.connect('weather.db')
cur = con.cursor()

cities.keys()
#with con:
#    cur.execute('CREATE TABLE daily_temp ( day_of_reading INT, Boston REAL, Chicago REAL, Denver REAL, Salt_Lake_City REAL, Washington_DC REAL);')

query_date = end_date - datetime.timedelta(days=30) #the current value being processed
print(int(query_date))
#with con:
#    while query_date < end_date:
#        cur.execute("INSERT INTO daily_temp(day_of_reading) VALUES (?)", (int(query_date.strftime('%Y-%m-%dT12:00:00')),))
#        query_date += datetime.timedelta(days=1)
#
#for k,v in cities.items():
#    query_date = end_date - datetime.timedelta(days=30) #set value each time through the loop of cities
#    while query_date < end_date:
#        #query for the value
#        r = requests.get(url + v + ',' +  query_date.strftime('%Y-%m-%dT12:00:00'))
#
#        with con:
#            #insert the temperature max to the database
#            cur.execute('UPDATE daily_temp SET ' + k + ' = ' + str(r.json()['daily']['data'][0]['temperatureMax']) + ' WHERE day_of_reading = ' + query_date.strftime('%s'))
#
#        #increment query_date to the next day for next operation of loop
#        query_date += datetime.timedelta(days=1) #increment query_date to the next day
#
#
#con.close() # a good practice to close connection to database