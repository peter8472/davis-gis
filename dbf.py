import json
import re
import pdb
import glob
import sys
HEADEROFFSET=32

fieldLen = {

}
class dbfReader():
    def __init__(self, filename):
        self.infile = open(filename, "rb") 
        self.header = self.getHeaders()
    def readByte(self, order = "little"):
        g = self.infile.read(1)
        return int.from_bytes(g, order)
    def read32(self, order="little"):
        g = self.infile.read(4)
        return int.from_bytes(g, order)
    def read16(self, order="little"):
        g = self.infile.read(2)
        return int.from_bytes(g, order)

    
    def getversion(self):
        self.infile.seek(0)
        version = self.readByte()
        return version
    def lastMod(self):
        self.infile.seek(1)
        year = self.readByte() + 1900
        month= self.readByte()
        day = self.readByte()
        return (year, month,day)
    def numRecords(self):
        self.infile.seek(4)
        
        self.records =self.read32()
        return self.records
    def readHeaderStructureLen(self):
        self.infile.seek(8)
        return self.read16()
    def getHeaders(self):
        n = self.readHeaderStructureLen()
        self.infile.seek(HEADEROFFSET)
        # subtract 32 because the header length
        # includes the global header for the file
        
        tmp = self.infile.read(n - 32)
        return Headers(tmp)
    def readAllRecords(self):
        n = self.readHeaderStructureLen()
        self.infile.seek(n)
        for x in range(1,51):
            
            for i in self.header.fields:
                
                if i['type'] == "C":
                    data = self.infile.read(i['length'])
                    print(i['name'], str(data))
                elif i['type'] == "N":
                    data = self.infile.read(i['length'])
                    print(i['name'], str(data))
                elif i['type'] == "F":
                    # data = self.infile.read(i['length'])
                    data = self.infile.read(20)
                    print(i['name'], str(data))
                elif i['type'] == "D":
                    data = self.infile.read(8)
                    print(i['name'], str(data))
                else:
                    print("unmkown data type"+ i['type'])
            
            
        
        

    def getFieldLen(self):
        self.infile.seek(10)
        self.fieldLen = self.read16()
        return self.fieldLen




class Headers():
    def __init__(self, data):
        self.data = data
        self.fields = []
        for x in range(0,int(len(self.data)/32)):
            offset = x * 32
            name = self.data[offset:offset+10]
            name = str(name.split(b'\x00')[0], "utf-8")
            # length = self.data[offset+16]
            # count = self.data[offset+17]
            # not used in Davis
            length =  int.from_bytes(self.data[offset+16:offset+17], byteorder="little")
            dtype = chr(self.data[offset+11])
            self.fields.append({
                "name": name,
                "type": dtype,
                "length": length
            
            })
        # pdb.set_trace()
    def printFields(self):
        for i in self.fields:
            print(i)
    

    

    
def print_header(filename):
    reader = dbfReader(filename)
    
    print(reader.lastMod())
    print(reader.numRecords())
    print("header structure len: {}".format(reader.readHeaderStructureLen()))
    headers = reader.getHeaders()
    headers.printFields()
    
if __name__ == "__main__":
    cmd = "header"
    if len(sys.argv)> 1:
        cmd = sys.argv[1]
    files = glob.glob("data/gps*/*.dbf")
    
    if cmd == "header":
        for x in files:
            print_header(x)
    elif cmd == "all":
        for x in files:
            reader = dbfReader(x)
            reader.readAllRecords()
    elif cmd == "version":
        for x in files:
            reader = dbfReader(x)
            print(reader.getversion())