from abstracts import *
from Villes import *
import sqlite3

class WorldTown(Ville, Serializable):
    def __init__(self):
        Ville.__init__(self)
    
    def serialize(self):
        arr = []
        arr.append(self.ville)
        arr.append(self.region)
        arr.append(self.latitude.getFloat())
        arr.append(self.longitude.getFloat())
        arr.append(self.gmt)
        arr.append(self.DST)
        arr.append(self.country)
        
        return arr
    
    def deserialize(self, arr):
        self.ville = arr[1]
        self.region = arr[0]
        self.latitude.parseFloat(arr[2])
        self.longitude.parseFloat(arr[3])
        self.gmt = arr[4]
        self.DST = arr[5]
        self.country = arr[6].capitalize()
        
    def getVilleObject(self):
        v = Ville()
        v.deserialize([self.country, self.region, self.ville, self.longitude.getFloat(),
                    self.latitude.getFloat(), self.gmt, self.DST, self.method])
        return v

class WorldTownsCollection(ItemsCollection):
    def __init__(self):
        ItemsCollection.__init__(self, WorldTown, 'all.arr')
        self.load()
    
    def queryCountryNames(self, startWith):
        countries = []
        startWith = startWith.lower()
        for ville in self.items:
            if ville.country[0:len(startWith)].lower() == startWith:
                if not ville.country in countries:countries.append(ville.country)
        
        countries.sort()
        
        return countries
    
    def queryRegionsNames(self, country, startwith):
        arr = []
        startwith = startwith.lower()
        
        for ville in self.items:
            if ville.country == country:
                if ville.region[0:len(startwith)].lower() == startwith:
                    if not ville.region in arr:arr.append(ville.region)
        
        arr.sort()
        
        return arr
    
    def queryVillesNames(self, country, region, startwith):
        arr = []
        startwith = startwith.lower()
        
        for ville in self.items:
            if ville.country == country:
                if ville.region == region:
                    if ville.ville[0:len(startwith)].lower() == startwith:
                        if not ville.ville in arr:arr.append(ville.ville)
        
        arr.sort()
        
        return arr
    
    def queryWorldTown(self, country, region, town):
        arr = []
        
        for ville in self.items:
            if ville.country == country:
                if ville.region == region:
                    if ville.ville == town:
                        return ville
        
        return None
    
if __name__ == "__main__":
    wt = WorldTownsCollection()
    print wt.queryCountryNames('tu')
    print wt.queryRegionsNames('tunisia', 'Su')
    print wt.queryVillesNames('tunisia',  'Susah', 'A')
    print wt.queryWorldTown('tunisia', 'Susah', 'Akouda')
    
    conn = sqlite3.connect('towns.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE ville (id_ville int, pays text, region text, 
                ville text, longitude text, latitude text, gmt text, dst int, method int)''')
    c.execute('''CREATE TABLE prayers_times (id_ville int, journee text, fajr text, 
                shuruq text, thuhr text, asr text, maghreb text)''')
    c.execute('''CREATE TABLE selected_ville (id int, id_ville int, pays text, region text, 
                ville text, longitude text, latitude text, gmt text, dst int, method int)''')
    conn.commit()
    
    c.execute("""DELETE FROM ville""")
    for i in range(1, wt.getCount() + 1):
        wt.moveTo(i)
        ville = wt.getData()
        try:
            c.execute("""INSERT INTO ville VALUES (%d,
                    "%s", "%s", "%s", "%f", "%f", '%1.1f', %d, %d)""" % (i,
                    ville.getCountry(), ville.getRegion(), ville.getVille(),
                    ville.getLongitude().getFloat(), ville.getLatitude().getFloat(), ville.getGMT(),
                    ville.getDST(), ville.getMethod()))
        except:
            print """INSERT INTO ville VALUES (%d, "%s", "%s", "%s", '%f', '%f', '%1.1f', %d, %d)""" % (i,
                ville.getCountry(), ville.getRegion(), ville.getVille(),
                ville.getLongitude().getFloat(), ville.getLatitude().getFloat(), ville.getGMT(),
                ville.getDST(), ville.getMethod())
            conn.commit()
    conn.commit()
    
    c.close()
    conn.close()
    

    