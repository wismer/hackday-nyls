import csv
import requests
import json
import cPickle as pickle



f = open('accidents.csv', "rU")
csv_f = csv.reader(f, dialect=csv.excel_tab)

accidents = []
colnamesstr= csv_f.next()
colnames=colnamesstr[0].split(",")

#["DATE","TIME","BOROUGH","ZIP CODE","LATITUDE","LONGITUDE","LOCATION","ON STREET NAME","CROSS STREET NAME","OFF STREET NAME","NUMBER OF PERSONS INJURED","NUMBER OF PERSONS KILLED","NUMBER OF PEDESTRIANS INJURED","NUMBER OF PEDESTRIANS KILLED","NUMBER OF CYCLIST INJURED","NUMBER OF CYCLIST KILLED","NUMBER OF MOTORIST INJURED","NUMBER OF MOTORIST KILLED","CONTRIBUTING FACTOR VEHICLE 1","CONTRIBUTING FACTOR VEHICLE 2","CONTRIBUTING FACTOR VEHICLE 3","CONTRIBUTING FACTOR VEHICLE 4","CONTRIBUTING FACTOR VEHICLE 5","UNIQUE KEY","VEHICLE TYPE CODE 1","VEHICLE TYPE CODE 2","VEHICLE TYPE CODE 3","VEHICLE TYPE CODE 4","VEHICLE TYPE CODE 5"]
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

for row in csv_f:
	rowaslist=[item for item in csv.reader([row[0]],skipinitialspace=True)][0]
	newacc=(dict(zip(colnames, rowaslist)))
	newacc["TIME"]=int(newacc["TIME"].replace(":",""))
	try:
		newacc["Dark"]=setDark(newacc["TIME"],newacc['LATITUDE'], newacc['LONGITUDE'], newacc['DATE'])
	except Exception as e:
		print e
	accidents.append(newacc)
	


print type(accidents[1])
print accidents[1]
print len(accidents)
pickle.dump( accidents, open( "accidents.p", "wb" ) )




