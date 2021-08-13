import haver
import glob
import csv
import json
import collections
import sqlite3
import decimal
import time
def get_err(record):
    pass

MINCOUNT=150
def print_max_parcels(infile):

    apns = collections.defaultdict(lambda: 0)
    most = {} # these have too many addresses
    reader = csv.DictReader(infile)
    for x in reader:
        apns[x['APN']] += 1
        if apns[x['APN']] > MINCOUNT:
            if x['APN'] not in most:
                most[x['APN']] = x
    
    for j in most.values():
        print(j['X'],j['Y'],j['FULLADDRESS'], j['CITY'])

    
def offsetof(infile):
    '''prints the distance from X,Y to LONGITUDE,LATITUDE
    I wrote this because I can't figure out why the database has both'''    
    count=0
    reader = csv.DictReader(infile)

    for x in reader:
        xy = {
            "stop_lat": x['Y'],
            "stop_lon": x['X']
            }
        latlon = {
            "stop_lat": x['LATITUDE'],
            "stop_lon": x['LONGITUDE']
        }
        try:
            print (haver.feet(xy,latlon))
            count += 1
        except decimal.InvalidOperation as e:
            print(e)
            time.sleep(0.25)
            
    print("records: {} ".format(count))    


if __name__ == "__main__":
    #h = glob.glob("Data/*address*")[0]
    
    
    
    home = {
        "stop_lat": decimal.Decimal("38.558222567735427"),
        "stop_lon": decimal.Decimal("-121.758899370402233")
        }
    base = decimal.Decimal("1")
    for i in range(0,10):
        delta =  base / (10**i)
        latlon = {
            "stop_lat": home["stop_lat"] +delta,
            "stop_lon": home['stop_lon'] 
        }
        print (delta, haver.feet(home,latlon))

