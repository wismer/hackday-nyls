import csv
import requests
import json
import cPickle as pickle


#open the csv file. The rU indicates universal newline mode. I think the dialect is unnecessary but haven't tried taking it out
f = open('accidents.csv', "rU")
csv_f = csv.reader(f, dialect=csv.excel_tab)

accidents = []

#the first row of the csv file is the header-->list of column names
colnamesstr= csv_f.next()
colnames=colnamesstr[0].split(",")

#retrieves information from sunrise-sunset api for a given lat/lng/date. Checks to see if given time is between sunrise and sunset
def setDark(time, lat, lng, date):
	content=requests.get("http://api.sunrise-sunset.org/json?lat=%s&lng=%s&date=%s" %(lat,lng,date)).content
	sunset=str(json.loads(content)[u'results'][u'sunset'])
	sunrise=str(json.loads(content)[u'results'][u'sunrise'])
	sunsettime=int(sunset.split(":")[0]+sunset.split(":")[1])-500
	sunrisetime=int(sunrise.split(":")[0]+sunrise.split(":")[1])-500
	sunsettime=sunsettime+1200
	dark=False
	if (time > sunsettime) or (time<sunrisetime):
		dark=True
	return dark

#reads each row of csv into list. Zips (combines) this list with colnames into a dictionary with colnames as keys. Adds dark as boolean
for row in csv_f:
	rowaslist=[item for item in csv.reader([row[0]],skipinitialspace=True)][0]
	newacc=(dict(zip(colnames, rowaslist)))
	newacc["TIME"]=int(newacc["TIME"].replace(":",""))
	try:
		newacc["Dark"]=setDark(newacc["TIME"],newacc['LATITUDE'], newacc['LONGITUDE'], newacc['DATE'])
	except Exception as e:
		print e
	accidents.append(newacc)
	

#just checking
print type(accidents[1])
print accidents[1]
print len(accidents)

#dump the info into a file
pickle.dump( accidents, open( "accidents.p", "wb" ) )




