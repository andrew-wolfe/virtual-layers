#mike byrne
#federal communications commission
#july 19, 2013
#simple python example to use ogr2ogr to export a postgis table to individual geojson files
#edit the variables below to create new features.  you will need to change in particular
#the myHigh variable to get the highest gid you want to export
#this is clearly not a finished script, but just an example to export individual rows
#as export files

import os

myHost = 'localhost'
myDB = 'feomike'
myPort = '54321'
mySchema = 'carto'
myTable = 'county_nad'
myHigh = 5
for gid in range(1,myHigh):
    print "    doing gid " + str(gid)
    str1 = 'ogr2ogr -f "geojson" feat' + str(gid) 
    str2 =  '.geojson PG:"host=' + myHost + ' dbname=' + myDB + ' port=' + myPort + '" '
    str3 = '-sql "SELECT * FROM ' + mySchema + "." + myTable + ' where gid = ' + str(gid) + '"'
    os.system(str1 + str2 + str3)
