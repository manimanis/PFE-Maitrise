#  -*- coding: utf8 -*-

import hexcodec
import libitl
import datetime
import thread
from abstracts import *
from Villes import *
from Events import *

class PrayersTimes(Serializable):
    def __init__(self):
        self.day  = "--/--"
        self.fajr = Time()
        self.shuruq = Time()
        self.thuhr = Time()
        self.assr = Time()
        self.maghreb = Time()
        self.ishaa = Time()
    
    def getDay(self):
        return self.day
    
    def setDay(self, val):
        self.day = val
    
    def getFajr(self):
        return self.fajr
    
    def setFajr(self, val):
        self.fajr.parse(val)
        
    def getShuruq(self):
        return self.shuruq
    
    def setShuruq(self, val):
        self.shuruq.parse(val)
        
    def getDhohr(self):
        return self.thuhr
    
    def setDhohr(self, val):
        self.thuhr.parse(val)
        
    def getAsr(self):
        return self.assr
    
    def setAsr(self, val):
        self.assr.parse(val)
        
    def getMaghreb(self):
        return self.maghreb
    
    def setMaghreb(self, val):
        self.maghreb.parse(val)
        
    def getIshaa(self):
        return self.ishaa
    
    def setIshaa(self, val):
        self.ishaa.parse(val)
    
    def serialize(self):
        arr = [self.day, 
               str(self.fajr), 
               str(self.shuruq), 
               str(self.thuhr), 
               str(self.assr), 
               str(self.maghreb), 
               str(self.ishaa)]
        return arr
    
    def deserialize(self, arr):
        self.day = arr[0]
        self.fajr.parseString(arr[1])
        self.shuruq.parseString(arr[2])
        self.thuhr.parseString(arr[3]) 
        self.assr.parseString(arr[4])
        self.maghreb.parseString(arr[5])
        self.ishaa.parseString(arr[6])
        
    def __cmp__(self, obj):
        if obj == None: return 1
        s1 = self.day + str(self.ishaa) + str(self.maghreb) + str(self.assr) + str(self.thuhr) + str(self.shuruq) + str(self.fajr)
        s2 = self.day + str(obj.ishaa) + str(obj.maghreb) + str(obj.assr) + str(obj.thuhr) + str(obj.shuruq) + str(obj.fajr)
        if s1 > s2: return 1
        elif s2 > s1: return -1
        else: return 0
        
    def __repr__(self):
        return repr(self.fajr) + repr(self.shuruq) + repr(self.thuhr) +\
               repr(self.assr) + repr(self.maghreb) + repr(self.ishaa)

class PrayersUtility:
    def __init__(self):       
        self.coq = QueryUtility('towns.db')
    
    
class YearPrayersTimes(ItemsCollection):
    def __init__(self, ville, queryWhere = ""):
        query = 'SELECT journee, fajr, shuruq, thuhr, asr, maghreb, ishaa FROM prayers_times WHERE id_ville = %d' % ville.getId() + queryWhere
        ItemsCollection.__init__(self, PrayersTimes, 'towns.db', query)
        
        self.ville = ville
        self.query = query
        self.load()
        
        if self.getCount() != 366:
            self.generate()
            self.save()
    
    def deleteAll(self, cur):
        cur.execute("DELETE FROM prayers_times WHERE id_ville = %d" % (self.ville.getId(),))
        
    def insert(self, cur, items):
        i = 1
        for item in items:
            try:
                cur.execute("""INSERT INTO prayers_times VALUES (%d, "%s",
                    "%s", "%s", "%s", "%s", "%s", "%s")""" % (self.ville.getId(), item.getDay(),
                    str(item.getFajr()), str(item.getShuruq()), str(item.getDhohr()),
                    str(item.getAsr()), str(item.getMaghreb()), str(item.getIshaa())))
            except:
                print "Erreur"
                
            i += 1
    
    def searchByDay(self, day):
        for i in range(0, len(self.items)):
            data = self.items[i]
            if data.getDay() == day:
                return i
        return -1
    
    def generate(self):
        date = libitl.Date(datetime.datetime(2000, 1, 1))
        
        loc = libitl.Location()
        loc.setLatitude(self.ville.latitude.getFloat())
        loc.setLongitude(self.ville.longitude.getFloat())
        loc.setGmt(self.ville.gmt)
        loc.setDST(self.ville.DST)
        loc.setSeaLevel(0)
        loc.setPressure(1010)
        loc.setTemperature(25)
        
        conf = libitl.Method(self.ville.method)
        conf.setRoundMethod(2)
        
        self.removeAll()
        for i in range(0, 366):
            ptimes = libitl.PrayersTimes(loc, conf, date)
            obj = PrayersTimes()
            
            obj.setDay("%02d/%02d" % (date.getMonth(), date.getDay()))
            obj.setFajr(str(ptimes.getFajr())[0:5])
            obj.setShuruq(str(ptimes.getShuruq())[0:5])
            obj.setDhohr(str(ptimes.getThuhr())[0:5])
            obj.setAsr(str(ptimes.getAssr())[0:5])
            obj.setMaghreb(str(ptimes.getMaghreb())[0:5])
            obj.setIshaa(str(ptimes.getIshaa())[0:5])
            
            self.appendItem(obj)
            date.nextDay()
        
        self.pos = 0
    
    def __repr__(self):
        s = ""
        s += repr(self.ville) 
        while (len(s) % 128) != 0 : s += "\xff"
        
        for i in range(0, self.getCount()):
            if (i != 0) and (i % 10 == 0):
                s += '\xff' * 8
            s += repr(self.items[i])

        while (len(s) % 128) != 0 : s += "\xff"
        
        return s

if __name__ == '__main__':
    qu = QueryUtility('towns.db')
    ville = qu.queryOneObject('SELECT id_ville, pays, region, ville, longitude, latitude, gmt, dst, method FROM selected_ville', Ville)
    pr = YearPrayersTimes(ville)
    print pr.getCount()
    print len(repr(pr))
    print hexcodec.generateHexData(0, 0, repr(pr))