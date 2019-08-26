import json
import re

class dbfReader():
    def __init__(self, filename):
        self.infile = open(filename, "rb") 
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
    def numHeaders(self):
        self.infile.seek(4)
        
        self.records =self.read32()
        return self.records
    def headerStructureLen(self):
        self.infile.seek(8)
        return self.read16()
    def getFieldLen(self):
        self.infile.seek(10)
        self.fieldLen = self.read16()
        return self.fieldLen


    def readField(self, offset=0):
        self.infile.seek(32 + offset * self.fieldLen)
        return(self.infile.read(self.fieldLen))


class Header():
    def __init__(self, reclen):
        self.len = reclen
if __name__ == "__main__":
    
    #reader = dbfReader("data/Parcels/Parcels.dbf")
    reader = dbfReader("data/AtlasGrid/Davis_DBO_AtlasGrid.dbf")
    print(reader.lastMod())
    print(reader.numHeaders())
    print(reader.headerStructureLen())
    print(reader.getFieldLen())
    for x in range(0, reader.numHeaders()):

        m = reader.readField(x)
        name = str(m[0:9])
        print(name)

