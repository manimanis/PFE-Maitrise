import libitl
from xml.dom import minidom

class Locations:
    def __init__(self, fileName):
        self.parseFile(fileName)
    
    def __getValue(self, tagName, node):
        node = node.getElementsByTagName(tagName)[0]
        if node.hasAttribute("value"):
            return node.getAttribute("value")
        return u''
    
    def __getDecimal(self, text):
        if text.index(',') >= 0:
            deg, min = text.split(',')
            deg = int(deg)
            min = int(min)
            return libitl.dms2Decimal(deg, min, 0)
        
        return float(text)
    
    def parseFile(self, fileName):
        self.__fileName = fileName
        self.__doc = minidom.parse(self.__fileName)
        self.__currNode = self.__doc.documentElement
        self.__places = []
        
        self.handlePlaces(self.__currNode.getElementsByTagName("place"))
        
        self.__currNode = None
        self.__doc.unlink()
    
    def saveFile(self):
        pass
    
    def handlePlaces(self, placeNodes):
        for placeNode in placeNodes:
            place = self.handlePlace(placeNode)
            
            self.__places.append(place)
    
    def handlePlace(self, placeNode):
        return { 'loc' : self.handleLocation(placeNode.getElementsByTagName("loc")[0]),
                 'conf' : self.handleConf(placeNode.getElementsByTagName("method")[0])}
    
    def handleLocation(self, locationNode):
        loc = libitl.Location()
        for node in locationNode.childNodes:
            if node.nodeName == "country":
                loc.setCountryName(self.__getValue("country", locationNode))
            elif node.nodeName == "town":
                loc.setTownName(self.__getValue("town", locationNode))
            elif node.nodeName == "longitude":
                lStr = self.__getValue("longitude", locationNode)
                loc.setLongitude(self.__getDecimal(lStr))
            elif node.nodeName == "latitude":
                lStr = self.__getValue("latitude", locationNode)
                loc.setLatitude(self.__getDecimal(lStr))
            elif node.nodeName == "gmt":
                loc.setGmt(float(self.__getValue("gmt", locationNode)))
            elif node.nodeName == "dst":
                if self.__getValue("dst", locationNode) == 'True':
                    val = 1
                else:
                    val = 0
                loc.setDST(val)
            elif node.nodeName == "pressure":
                loc.setPressure(float(self.__getValue("pressure", locationNode)))
            elif node.nodeName == "sealevel":
                loc.setSeaLevel(float(self.__getValue("sealevel", locationNode)))
            elif node.nodeName == "temperature":
                loc.setTemperature(float(self.__getValue("temperature", locationNode)))
            
        return loc
    
    def handleConf(self, confNode):
        conf = libitl.Method()
        conf.setMethod(int(self.__getValue("index", confNode)))
        return conf
    
    def __len__(self):
        return len(self.__places)
    
    def __getitem__(self, idx):
        return self.__places[idx]
    
    def __setitem__(self, idx, value):
        self.__places[idx] = value
    
    def append(self, location = None, method = None):
        self.__places.append({'loc' : location, 'conf' : method})
    
    def delete(self, idx):
        del self.__places[idx]
    
if __name__ == '__main__':
    l = Locations('locations.xml')
    print len(l)
    l[1] = l[0]
    print l[0]['loc']
    print l[0]['conf']
    print l[1]['loc']
    print l[1]['conf']
    