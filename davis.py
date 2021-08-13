'''works with the davis city business liscense directory, or at least
it used to.  Right now their maps service isn't working


'''
import json
import re
import argparse
import os
from pathlib import Path

def jdump(i):
    print(json.dumps(i,indent=4))



def search(g,name=None, street=None ,primaryNumber=None,
    secondaryAddress=None):
    results=[]
    for i in g:
        if name == None or re.search(name,i['name'], re.IGNORECASE):
        
            if street == None or re.search   (street,i['streetName'], re.IGNORECASE): 
                if primaryNumber==None or primaryNumber == i['primaryNumber']:
                    if secondaryAddress==None or secondaryAddress == i['secondaryAddress']:

                        # jdump(i)
                    # print(i['name'], i['address'], i['description'])
                        results.append(i)
                    # print()
    return results

def search2(g, searchobj=None):
    result = []
    # search the first key on the full database

    for k,v in searchobj.items():
    
        print(k,v)

def print_all_churches(datadir):
    results = []
    for x in datadir.glob("*.json"):
        with open(x) as infile:
            g = json.load(infile)
            x=search(g, name='taqueria guada')
            results.extend(x)
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='enter a regex search')
    parser.add_argument('name',  type=str, help='regex of charity  name', nargs='?')
    
    201812759349300326
    parser.add_argument('-e',  type=str, help='regex of charity  name')

    args = parser.parse_args()
    
    print(args)
    inpath = Path.home() /  "OneDrive" /     "davisbusiness"
    files = list(inpath.glob("20*"))

    files.sort(reverse=True)
    print(files[0])


    f = open(files[0])
    g = json.load(f)
    
    x=search(g, name=args.name)
    
    results = []
    print("{} results found".format(len(x)))
    for i in x:
        # results.append({'name': i['name'],'city':i['phoneNumber']})
        # results.append({'name': i['name']})
        results.append(i)
        # print(i['name'])
    tmp = json.dumps(results, indent=4)
    print(tmp)