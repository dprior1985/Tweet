#!/usr/bin/env python
import sys
from twython import Twython
import os
import datetime


CONSUMER_KEY = '## PERSONAL KEY ##'
CONSUMER_SECRET = '## PERSONAL KEY ##'
ACCESS_KEY = '## PERSONAL KEY ##'
ACCESS_SECRET = '## PERSONAL KEY ##'


api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

task = status=sys.argv[1]
message = status=sys.argv[2]

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
