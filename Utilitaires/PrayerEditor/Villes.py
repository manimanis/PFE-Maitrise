#  -*- coding: utf8 -*-

import hexcodec
import libitl
import datetime
import thread
from abstracts import *

# Class to represent Geographic position
class GeoPosition(Serializable):
    def __init__(self):
        self.deg = 0
        self.min = 0
        self.sec = 0
        self.sens = 'N'
    
    def getDegree(self):
        return self.deg
    
    def setDegree(self, nv):
        self.deg = nv
    
    def getMinutes(self):
        return self.min
    
    def setMinutes(self, nv):
        self.min = nv
        
    def getSeconds(self):
        return self.sec
    
    def setSeconds(self, nv):
        self.sec = nv
        
    def getSens(self):
        return self.sens
    
    def setSens(self, nv):
        self.sens = nv
        
    def getFloat(self):
        v = self.deg + self.min / 60.0 + self.sec / 3600.0 
        if self.sens == 'S' or self.sens == 'W':
            v = -v
        return v
    
    def parseFloat(self, v, lat = True):
        if lat:
            self.sens = 'N'
        else:
            self.sens = 'E'
            
        if v < 0:
            v = -v
            if lat:
                self.sens = 'S'
            else:
                self.sens = 'W'
            
        self.deg = int(v)
        self.min = int((v - self.deg) * 60.0)
        self.sec = int((v - self.deg - self.min / 60.0) * 3600.0)
    
    def parseString(self, s):
        self.sens = s[-1]
        arr = s.split(':')
        self.deg = int(arr[0])
        self.min = int(arr[1])
        self.sec = int(arr[2][:-2])
        
    
    # ---------- Serializable
    def serialize(self):
        arr = []
        arr.append(self.deg)
        arr.append(self.min)
        arr.append(self.sec)
        arr.append(self.sens)
        
        return arr
    
    def deserialize(self, arr):
        self.deg = arr[0]
        self.min = arr[1]
        self.sec = arr[2]
        self.sens = arr[3]
        
    def format(self):
        return "%03d:%02d:%02d %c" % (self.deg, self.min, self.sec, self.sens)
        
    def __str__(self):
        return "%d:%02d:%02d %c" % (self.deg, self.min, self.sec, self.sens)
    
    def __repr__(self):
        return hexcodec.int2bcd(self.deg, 2) + hexcodec.int2bcd(self.min, 1) + \
                hexcodec.int2bcd(self.sec, 2) + self.sens
                
    def __cmp__(self, obj):
        sf = self.getFloat()
        of = obj.getFloat()
        if sf > of:
            return 1
        elif sf < of:
            return -1
        else:
            return 0

# Class to represent a town in a region
class Ville(Serializable):
    def __init__(self):
        self.id = 0
        self.country = "Tunisie"
        self.region = ""
        self.ville = ""
        self.longitude = GeoPosition()
        self.latitude = GeoPosition()
        self.gmt = 0
        self.DST = False
        self.method = 5
        
    def getId(self):
        return self.id
    
    def setId(self, nv):
        self.id = nv
    
    def getCountry(self):
        return self.country
    
    def setCountry(self, nv):
        self.country = nv
        
    def getRegion(self):
        return self.region
    
    def setRegion(self, nv):
        self.region = nv
        
    def getVille(self):
        return self.ville
    
    def setVille(self, nv):
        self.ville = nv
        
    def getLongitude(self):
        return self.longitude
    
    def setLongitude(self, nv):
        self.longitude = nv
        
    def getLatitude(self):
        return self.latitude
    
    def setLatitude(self, nv):
        self.latitude = nv
        
    def getGMT(self):
        return self.gmt
    
    def setGMT(self, nv):
        self.gmt = nv
        
    def getDST(self):
        return self.DST
    
    def setDST(self, nv):
        self.DST = nv

    def getMethod(self):
        return self.method
    
    def setMethod(self, nv):
        self.method = nv
        
    def serialize(self):
        arr = []
        arr.append(self.id)
        arr.append(self.country)
        arr.append(self.region)
        arr.append(self.ville)
        arr.append(self.longitude.getFloat())
        arr.append(self.latitude.getFloat())
        arr.append(self.gmt)
        arr.append(self.DST)
        arr.append(self.method)
        
        return arr
    
    def deserialize(self, arr):
        self.id = arr[0]
        self.country = arr[1]
        self.region = arr[2]
        self.ville = arr[3]
        self.longitude.parseFloat(float(arr[4]))
        self.latitude.parseFloat(float(arr[5]))
        self.gmt = float(arr[6])
        self.DST = arr[7]
        self.method = arr[8]
    
    def __repr__(self):
        return self.country.encode('ascii') + '\xff' * (16 - len(self.country)) + \
            self.region.encode('ascii') + '\xff' * (16 - len(self.region)) + \
            self.ville.encode('ascii') + '\xff' * (16 - len(self.ville)) + \
            repr(self.longitude) + repr(self.latitude) + \
            hexcodec.int2bcd(int(self.gmt * 10)) + hexcodec.int2bcd(self.DST) + \
            hexcodec.int2bcd(self.method)
    
    def __cmp__(self, obj):
        if obj == None: return 1
        if self.country > obj.country:          return 1
        elif self.country < obj.country:        return -1
        else:
            if self.region > obj.region:        return 1
            elif self.region < obj.region:      return -1
            else:
                if self.ville > obj.ville:      return 1
                elif self.ville < obj.ville:    return -1
                else:
                    if self.longitude > obj.longitude:
                        return 1
                    elif self.longitude < obj.longitude:
                        return -1
                    else:
                        if self.latitude > obj.latitude:
                            return 1
                        elif self.latitude < obj.latitude:
                            return -1
                        else:
                            if self.gmt > obj.gmt:
                                return 1
                            elif self.gmt < obj.gmt:
                                return -1
                            else:
                                if self.DST > obj.DST:
                                    return 1
                                elif self.DST < obj.DST:
                                    return -1
                                else:
                                    if self.method > obj.method:
                                        return 1
                                    elif self.method < obj.method:
                                        return -1
                                    else:
                                        return 0

#class to represent multiple towns
class SelectedVillesCollection(ItemsCollection):
    def __init__(self, queryWhere = ""):
        query = 'SELECT id_ville, pays, region, ville, longitude, latitude, gmt, dst, method FROM selected_ville ' + queryWhere
        ItemsCollection.__init__(self, Ville, 'towns.db', query)
        
        self.query = query
        self.load()
    
    def deleteAll(self, cur):
        cur.execute("DELETE FROM selected_ville")
        
    def insert(self, cur, items):
        i = 1
        for item in items:
            try:
                cur.execute("""INSERT INTO selected_ville VALUES (%d, %d,
                    "%s", "%s", "%s", "%f", "%f", '%1.1f', %d, %d)""" % (i, item.getId(),
                    item.getCountry(), item.getRegion(), item.getVille(),
                    item.getLongitude().getFloat(), item.getLatitude().getFloat(), item.getGMT(),
                    item.getDST(), item.getMethod()))
            except:
                print "Erreur"
                
            i += 1
        
        
class VillesUtility: 
    def __init__(self):       
        self.coq = QueryUtility('towns.db')
        
    def searchVille(self, country, region, ville):
        return self.coq.queryOneObject('SELECT * FROM ville WHERE pays LIKE "%s" AND region LIKE "%s" AND ville LIKE "%s" ORDER BY ville' % (country, region, ville), Ville)
    
    def getCountryList(self, country = ""):
        return self.coq.queryArray('SELECT distinct pays FROM ville WHERE pays LIKE "%s%%" ORDER BY pays' % (country,))
    
    def getRegionsList(self, pays, region = ""):
        return self.coq.queryArray('SELECT distinct region FROM ville WHERE pays LIKE "%s" AND region LIKE "%s%%" ORDER BY region' % (pays, region))
    
    def getVillesList(self, pays, region, ville = ""):
        return self.coq.queryArray('SELECT distinct ville FROM ville WHERE pays LIKE "%s" AND region LIKE "%s" AND ville LIKE "%s%%" ORDER BY ville' % (pays, region, ville))
          
if __name__ == '__main__':
    villes = VillesCollection()
    print villes.getCount()
    
    villes.setQuery('WHERE pays = "Tunisia" and region = "Susah" and ville LIKE "H%"')
    print villes.getCount()
    
    print villes.getCountryList()
    print villes.getRegionsList('tunisia')
    print villes.getVillesList('tunisia', 'susah')
