import datetime
from abstracts import *
import hexcodec

TYPE_CHQ_JOUR      = 0x007F

TYPE_CHQ_DIM       = 0x0001
TYPE_CHQ_LUN       = 0x0002
TYPE_CHQ_MAR       = 0x0004
TYPE_CHQ_MER       = 0x0008
TYPE_CHQ_JEU       = 0x0010
TYPE_CHQ_VEN       = 0x0020
TYPE_CHQ_SAM       = 0x0040

TYPE_CHQ_SEMAINE   = 0x0080

TYPE_CHQ_FAJR      = 0x0100
TYPE_CHQ_CHOUROUK  = 0x0200
TYPE_CHQ_DHOHR     = 0x0400
TYPE_CHQ_ASR       = 0x0800
TYPE_CHQ_MAGHREB   = 0x1000
TYPE_CHQ_ISHAA     = 0x2000

TYPE_CHQ_SALAT     = 0x3F00


class Date:
    def __init__(self):
        dt = datetime.datetime.now()
        self.setDate(dt.day, dt.month, dt.year)
    
    def setDate(self, jj, mm, aa):
        self.jj = jj
        self.mm = mm
        self.aa = aa
        if (self.aa >= 2000) : self.aa -= 2000
        self._calcNbreJours()
    
    def getJour(self):
        return self.jj
    
    def setJour(self, nv):
        self.jj = nv
        self._calcNbreJours()
    
    def getMois(self):
        return self.mm
    
    def setMois(self, nv):
        self.mm = nv
        self._calcNbreJours()
    
    def getAnnee(self):
        return self.aa
    
    def setAnnee(self, nv):
        self.aa = nv
        self._calcNbreJours()
        
    def isBissextile(self):
        if (self.aa % 4) == 0:
            return 1
        return 0
    
    def getJourSem(self):
        return self.day
    
    def _calcNbreJours(self):
        nld = (self.aa - 1) / 4
        nj = self.aa * 365 + nld
        if (self.mm > 1) : nj += 31
        if (self.mm > 2) : nj += 28 + self.isBissextile()
        if (self.mm > 3) : nj += 31
        if (self.mm > 4) : nj += 30
        if (self.mm > 5) : nj += 31
        if (self.mm > 6) : nj += 30
        if (self.mm > 7) : nj += 31
        if (self.mm > 8) : nj += 31
        if (self.mm > 9) : nj += 30
        if (self.mm > 10) : nj += 31
        if (self.mm > 11) : nj += 30
        nj += self.jj
        
        self.days = nj
        self.day = (self.days % 7) + 1
        
    def getNbreJours(self):
        return self.days 
    
    def parseString(self, s):
        self.setDate(int(s[8:]),int(s[5:7]),int(s[0:4]))
        
    # v = nombre de jours depuis 01/01/2000
    def parseInteger(self, v):
        self.aa = int(v / 365.25)
        v -= self.aa * 365      # annees
        v -= (self.aa - 1) / 4  # jours bissextiles
        self.mm = 1
        if v > 31: # Jan
            self.mm += 1
            v -= 31
        if v > 28: # Fev
            self.mm += 1
            v -= 28 + self.isBissextile()
        if v > 31: # Mar
            self.mm += 1
            v -= 31
        if v > 30: # Avr
            self.mm += 1
            v -= 30
        if v > 31: # Mai
            self.mm += 1
            v -= 31
        if v > 30: # Jui
            self.mm += 1
            v -= 30
        if v > 31: # Jul
            self.mm += 1
            v -= 31
        if v > 31: # Aou
            self.mm += 1
            v -= 31
        if v > 30: # Sep
            self.mm += 1
            v -= 30
        if v > 31: # Oct
            self.mm += 1
            v -= 31
        if v > 30: # Nov
            self.mm += 1
            v -= 30
        self.jj = v
        self._calcNbreJours()

    def __str__(self):
        return "%04d/%02d/%02d" % (self.aa, self.mm, self.jj)

    def __cmp__(self, obj):
        if self.days > obj.days:
            return 1
        elif self.days < obj.days:
            return -1
        else:
            return 0
            
class Time:
    def __init__(self):
        dt = datetime.datetime.now()
        self.setTime(dt.hour, dt.minute)
        
    def setTime(self, hh, mm):
        self.hh = hh
        self.mm = mm
        self._calcMinutes()
        
    def _calcMinutes(self):
        self.mn = self.hh * 60 + self.mm
        
    def setHeure(self, nv):
        self.hh = nv
        self._calcMinutes()
        
    def getHeure(self):
        return self.hh
    
    def setMinute(self, nv):
        self.mm = nv
        self._calcMinutes()
        
    def getMinute(self):
        return self.mm
    
    def getNbreMinutes(self):
        return self.mn
    
    def parseString(self, s):
        self.setTime(int(s[0:2]), int(s[3:]))
        
    def parseInteger(self, v):
        self.hh = v / 60
        self.mm = v % 60
        self._calcMinutes()
        
    def parse(self, obj):
        if isinstance(obj, str) or isinstance(obj, unicode):
            self.parseString(obj)
        elif isinstance(obj, int):
            self.parseInteger(obj)
        elif isinstance(obj, Time):
            self.parseInteger(obj.getNbreMinutes())
        else:
            raise ValueError
        
    def __cmp__(self, obj):
        if self.mn > obj.mn:
            return 1
        elif self.mn < obj.mn:
            return -1
        else:
            return 0
    
    def __str__(self):
        return "%02d:%02d" % (self.hh, self.mm)
    
    def __repr__(self):
        return hexcodec.int2bcd(self.hh) + hexcodec.int2bcd(self.mm)
        
class Event(Serializable):
    def __init__(self):
        self.idx = 0
        self.type = 0 # 0x4FFF
        self.startDate = Date()
        self.endDate = Date()
        self.time = Time()
        self.startInterval = 0
        self.endInterval = 0
        self.message = ""
        
    def serialize(self):
        arr = []
        arr.append(self.idx)
        arr.append(self.type)
        arr.append(str(self.startDate))
        arr.append(str(self.endDate))
        arr.append(str(self.time))
        arr.append(self.startInterval)
        arr.append(self.endInterval)
        arr.append(self.message)
        
        return arr
        
    def deserialize(self, arr):
        self.idx = arr[0]
        self.type = arr[1]
        self.startDate.parseString(arr[2])
        self.endDate.parseString(arr[3])
        self.time.parseString(arr[4])
        self.endInterval = int(arr[6])
        self.startInterval = int(arr[5])
        self.message = arr[7]
    
    def getIndex(self):
        return self.idx
    
    def setIndex(self, nv):
        self.idx = nv
        
    def getType(self):
        return self.type
    
    def setType(self, nv):
        self.type = nv
        
    def getStartDate(self):
        return self.startDate
    
    def setStartDate(self, nv):
        self.startDate = nv
        
    def getEndDate(self):
        return self.endDate
    
    def setEndDate(self, nv):
        self.endDate = nv
        
    def getTime(self):
        return self.time
    
    def setTime(self, nv):
        self.time = nv
        
    def getStartInterval(self):
        return self.startInterval
    
    def setStartInterval(self, nv):
        self.startInterval = nv
        
    def getEndInterval(self):
        return self.endInterval
    
    def setEndInterval(self, nv):
        self.endInterval = nv
        
    def getMessage(self):
        return self.message
    
    def setMessage(self, nv):
        self.message = nv
        
    def __cmp__(self, val):
        if val == None : return 1
        if self.idx > val.idx:   return 1
        elif self.idx < val.idx: return -1
        else:
            if self.type > val.type:   return 1
            elif self.type < val.type: return -1
            else:
                if self.startDate > val.startDate:   return 1
                elif self.startDate < val.startDate: return -1
                else:
                    if self.endDate > val.endDate:   return 1
                    elif self.endDate > val.endDate: return -1
                    else:
                        if self.time > val.time:  return 1
                        elif self.time > val.time: return -1
                        else:
                            if self.startInterval > val.startInterval:  return 1
                            elif self.startInterval > val.startInterval: return -1
                            else:
                                if self.message > val.message:   return 1
                                elif self.message < val.message: return -1
        return 0

class EventsCollection(ItemsCollection):
    def __init__(self):
        ItemsCollection.__init__(self, Event, 'towns.db', 'SELECT * FROM events')
        self.events = []
        self.pos = 0
        self.changed = False
        self.load()
        
    def deleteAll(self, c):
        c.execute('DELETE FROM events')   

    def insert(self, cur, items):
        i = 1
        for item in items:
            try:
                cur.execute("""INSERT INTO events VALUES (%d, %d,
                    "%s", "%s", "%s", "%s", "%s", "%s")""" % (item.getIndex(), item.getType(),
                    str(item.getStartDate()), str(item.getEndDate()), str(item.getTime()),
                    str(item.getStartInterval()), str(item.getEndInterval()), item.getMessage()))
            except:
                print "Erreur"
                raise 
                
            i += 1
                
if __name__ == "__main__":
##    dt = Date()
##    print '-'
##    print dt.getJour()
##    print dt.getMois()
##    print dt.getAnnee()
##    print dt.getNbreJours()
##    print dt.getJourSem()
##    
##    dt.parseString('2001/01/01')
##    print '-'
##    print dt.getJour()
##    print dt.getMois()
##    print dt.getAnnee()
##    print dt.getNbreJours()
##    print dt.getJourSem()
##    
##    dt.parseInteger(4238)
##    print '-'
##    print dt.getJour()
##    print dt.getMois()
##    print dt.getAnnee()
##    print dt.getNbreJours()
##    print dt.getJourSem()
##    
##    tm = Time()
##    print '/'
##    print tm.getHeure()
##    print tm.getMinute()
##    print tm.getNbreMinutes()
##    
##    tm.parseString('15:25')
##    print '/'
##    print tm.getHeure()
##    print tm.getMinute()
##    print tm.getNbreMinutes()
##    
##    tm.parseInteger(650)
##    print '/'
##    print tm.getHeure()
##    print tm.getMinute()
##    print tm.getNbreMinutes()

    e = Events()
    s = repr(e.serialize())
    print s
    e.deserialize(eval(s))
    print e.serialize()
    