import glob
import csv
import json


if __name__ == "__main__":
    h = glob.glob("Data/*address*")[0]
    outfile = open("yologeocode.json", 'w')
    
    with open(h, encoding="utf-8-sig") as infile:
        reader = csv.DictReader(infile)
    
        for x in reader:
            json.dump(x, outfile)
            outfile.write("\n") # json lines format

    