import json
import re

def jdump(i):
    print(json.dumps(i,indent=4))

if __name__ == "__main__":
    #f = open("licenses.json")
    f = open("20190301.json")

    g = json.load(f)
    
    for i in g:
     #   if  re.search("safeway",i['name'], re.IGNORECASE):
          
        
            if (re.search   ('covel',i['streetName'], re.IGNORECASE) and
        i['address'].startswith("1435")):
                jdump(i)
