import sqlite3

# Abstract class to serialize data
class Serializable:   
    def serialize(self):
        raise NotImplementedError
    
    def deserialize(self, arr):
        raise NotImplementedError

# Abstract class to browse
class Browsable:  
    def moveFirst(self):
        raise NotImplementedError
        
    def movePrev(self):
        raise NotImplementedError
        
    def moveNext(self):
        raise NotImplementedError
        
    def moveLast(self):
        raise NotImplementedError
    
    def moveTo(self, pos):
        raise NotImplementedError
        
    def getCount(self):
        raise NotImplementedError
    
    def getPos(self):
        raise NotImplementedError

#Savable
class Saveable:
    def load(self):
        raise NotImplementedError
    
    def save(self):
        raise NotImplementedError

class ItemsCollection(Browsable, Serializable, Saveable):
    def __init__(self, classe, dbfile, query):
        self.pos = -1
        self.items = []
        self.classe = classe
        self.filename = dbfile
        self.query = query
        self.changed = False
    
    def getQuery(self, nv):
        return self.query
    
    def setQuery(self):
        self.query = nv
    
    def isEmpty(self):
        return (self.pos == -1)
    
    def appendItem(self, item):
        if not isinstance(item, self.classe):
            raise TypeError
        self.items.append(item)
        self.changed = True
        if self.pos == -1:
            self.pos = 0
    
    def removeAll(self):
        self.items = []
        self.pos = 0
        
    def removeAt(self, idx):
        if (idx >= 0) and (idx < len(self.items)):
            del self.items[idx]
            if self.pos >= idx:
                self.pos -= 1
            self.changed = True
    
    def serialize(self):
        arr = []
        
        for it in self.items:
            arr.append(it.serialize())
        
        return arr
    
    def deserialize(self, arr):
        self.items = []
        
        for it in arr:
            obj = self.classe()
            obj.deserialize(it)
            self.items.append(obj)
        
        if self.isEmpty(): 
            self.pos = -1
        else:
            self.pos = 0
            
    def hasChanged(self):
        return self.changed
    
    def getCount(self):
        return len(self.items)
            
    def getData(self, idx = None):
        if idx == None: idx = self.pos 
        if (idx >= 0) and (idx < len(self.items)): return self.items[idx]
        return None
    
    def setData(self, data, idx = None):
        if idx == None: idx = self.pos 
        if (idx >= 0) and (idx < len(self.items)):
            if data != self.items[idx]:
                self.items[idx] = data 
                self.changed = True
        
    def getPos(self):
        return self.pos
    
    def moveFirst(self):
        self.pos = 0
            
    def moveNext(self):
        if (self.pos + 1 < len(self.items)):
            self.pos += 1
            
    def movePrev(self):
        if (self.pos > 0):
            self.pos -= 1
            
    def moveLast(self):
        self.pos = len(self.items) - 1
        
    def moveTo(self, pos):
        if pos < 0: pos = 0
        elif pos >= len(self.items) : pos = len(self.items) - 1
        
        self.pos = pos
    
    def deleteAll(self, c):
        None
        
    def insert(self, c, items):
        None
        
    def save(self):
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        
        self.deleteAll(c)
        conn.commit()
        
        self.insert(c, self.items)
        
        conn.commit()
        conn.close()
        self.changed = False
    
    def load(self):
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        try:
            c.execute(self.query)
            self.deserialize(c.fetchall())
        except:
            print "Erreur :", self.query
            raise
        conn.close()
        self.changed = False
        
    def __iter__(self):
        for v in self.villes:
            yield v

class QueryUtility:
    def __init__(self, dbfile):
        self.filename = dbfile

    def queryArray(self, query):
        arr = []
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        try:
            c.execute(query)
            for row in c:
                arr.append(row[0])
        except:
            print "Erreur :", self.query
        conn.close()
        
        return arr
    
    def queryOneObject(self, query, classe):
        conn = sqlite3.connect(self.filename)
        obj = classe()
        c = conn.cursor()
        try:
            c.execute(query)
            obj.deserialize(c.fetchone())
        except:
            print "Erreur :", query
        conn.close()
        
        return obj
    
    def queryOne(self, query):
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        try:
            c.execute(query)
            return c.fetchone()
        except:
            print "Erreur :", query
        conn.close()
        
        return None
    
