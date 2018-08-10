from abstracts import *

class Message(Serializable):
    def __init__(self):
        self.items = []
        for i in range(0, 4):
            self.items.append('')
        
    def getMessage(self, idx):
        return self.items[idx]
    
    def setMessage(self, idx, nv):
        self.items[idx] = nv
    
    def serializable(self):
        return self.items
    
    def deserilizable(self, arr):
        self.items = arr
        
    def __cmp__(self, obj):
        for i in range(0, 4):
            if self.items[i] > obj.items[i]:
                return 1
            elif self.items[i] < obj.items[i]:
                return -1
        return 0
        
        
class MessagesCollection(Serializable, Browsable):
    def __init__(self):
        self.pos = 0
        self.items = []
        for i in range(0, 63):
            self.items.append(Message())
    
    def getLabel(self):    
        if self.pos < 3:
            return 'Menu Principal %d' % (self.pos + 1,)
        elif self.pos >= 3 and self.pos < 15:
            return 'Sous Menu %d' % (self.pos - 2,)
        elif self.pos >= 15 and self.pos < 64:
            return 'Sous Menu %d.%d' % ((self.pos - 15) / 4 + 1, (self.pos - 15) % 4 + 1)
        return ''
    
    def getCount(self):
        return len(self.items)
    
    def getPos(self):
        return self.pos
    
    def getData(self):
        return self.items[self.pos]
    
    def setData(self, data):
        if data != self.items[self.pos]:
            self.items[self.pos] = data
            
    def moveFirst(self):
        self.pos = 0
        
    def movePrev(self):
        if self.pos > 0:
            self.pos -= 1
            
    def moveNext(self):
        if self.pos + 1 < len(self.items):
            self.pos += 1
            
    def moveLast(self):
        self.pos = len(self.items) - 1
    
    def moveTo(self, pos):
        if (pos >= 0) and (pos < len(self.items)):
            self.pos = pos