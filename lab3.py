import csv
from math import radians, cos, sin, asin, sqrt
"""
# Hamza Mahmood 33093 B
# haversine function taken from:
# http://stackoverflow.com/questions/15736995/how-can-i-quickly-estimate-the-distance-between-two-latitude-longitude-points
"""
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6367 * c
    return km

f = open('GeoLiteCity-Location.csv', 'r')
csv_f = csv.reader(f)
c = 0
myMap = {}
print "\nPlease wait while the prgram loads the csv file into the memory!\n"
for row in csv_f:
    if c < 2:                                   #skip the first two rows
        c += 1
        continue
    (locId, country, region, city, postalCode, latitude, longitude, metroCode, areaCode) = row
    if not(city == ""):                         #skiping the location without any city name
        myMap[city] = [latitude,longitude]
        
while(1):
    print "----------------------------------------------"
    print "Enter city name to search:"
    name = raw_input()

    value = myMap.get(name, "none")
    if not(value == "none"):
        #print value
        print "\n   Found!  \n"
        print "\n   Printing City names in 250km radius \n"
        for city in myMap:
            #print myMap[city][0]
            distance = haversine(float(value[1]),float(value[0]),float(myMap[city][1]),float(myMap[city][0]))
            #print distance
            if (distance < 250):            #searches cities in 250km radius of the city given
                print city
    else:
        print "Not found!"
        print "----------------------------------------------"