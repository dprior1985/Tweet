#!/usr/bin/env python
import sys
from twython import Twython
import os
import datetime
import MySQLdb

CONSUMER_KEY = '## PERSONAL KEY ##'
CONSUMER_SECRET = '## PERSONAL KEY ##'
ACCESS_KEY = '## PERSONAL KEY ##'
ACCESS_SECRET = '## PERSONAL KEY ##'


api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

task = status=sys.argv[1]
message = status=sys.argv[2]

# Open database connection
db = MySQLdb.connect("localhost","danny","danny123","MYGARDEN" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
vWeatherAPITempData = "404 error";
vTempsensor2 = "404 error";

if (task == 'CPU'):
        cmd = '/opt/vc/bin/vcgencmd measure_temp'
        line = os.popen(cmd).readline().strip()
        temp = line.split('=')[1].split("'")[0]
        api.update_status(status='Dannyspi2.local CPU temperature is '+temp+' C - '+str(datetime.datetime.now()))
if (task == 'message'):
        api.update_status(status=message+' - '+str(datetime.datetime.now()))
if (task =='chart1'):
        photo = open('/var/www/Graph1.png','rb')
        api.update_status_with_media(media=photo, status='Outside Temp Chart - '+str(datetime.datetime.now()))
if (task =='chart2'):
        photo = open('/var/www/Graph2.png','rb')
        api.update_status_with_media(media=photo, status='Inside Temp Chart - '+str(datetime.datetime.now()))
if (task =='chart3'):
        photo = open('/var/www/Graph3.png','rb')
        api.update_status_with_media(media=photo, status='Outside Temp Chart all time - '+str(datetime.datetime.now()))
if (task =='chart4'):
        photo = open('/var/www/Graph4.png','rb')
        api.update_status_with_media(media=photo, status='Inside Temp Chart all time- '+str(datetime.datetime.now()))
if (task = 'tmep'):
	cursor.execute("select SaveData from ControlLog where RunNumberId = (select max(RunNumberId) from RunNumber) and ActionName = 'temp sensor 2' ;" )
	for row in cursor.fetchall():

		vTempsensor2 = (row[0])	
	
	api.update_status(status='Internal Temp - '+str(vTempsensor2)+'C - '+str(datetime.datetime.now()))
	
	cursor.execute("select SaveData from ControlLog where RunNumberId = (select max(RunNumberId) from RunNumber) and ActionName = 'Weather API' and LogDescription = 'Temp String' ;" )
	for row in cursor.fetchall():

		vWeatherAPITempData = (row[0])
	
	api.update_status(status='API - Bexley Temp - '+str(vWeatherAPITempData)+' - '+str(datetime.datetime.now()))
	

