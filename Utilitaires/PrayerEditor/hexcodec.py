class HexEncoder:
    def __init__(self):
        self.linecount = 16
        self.data = ""
        
    def toString(self, value):
        if isinstance(value, str) or isinstance(value, unicode):
            return repr(value)
        
        if isinstance(value, int):
            s = ""
            while value != 0:
                s += chr(value % 256)
                value = value / 256
            return s
        
#convertir un entier au format BCD
def int2bcd(value, octets = 1):
    digits = 2 * octets
    v = str(value)
    
    while len(v) < digits: v = '0' + v
    v = v[-digits:]

    ch = ""
    i = 0
    
    while i < len(v):
        ch += chr((ord(v[i]) - 48) * 16 + (ord(v[i + 1]) - 48))
        i += 2
    
    return ch

# calculer la somme de controlr d'une ligne
def checksum(s):
    sum = 255
    for v in s:
        sum += ord(v)
    sum = (255 - sum % 256) % 256
    return sum

# generer le code hex pour une ligne d'un fichier Hex
def hexLine(offset, rectype, data):
    try:
        ns = chr(len(data)) + chr(offset / 256) + chr(offset % 256) + chr(rectype) + data
    except:
        print offset
    chksm = checksum(ns)
    ns = ns + chr(chksm)
    
    hl = ":"
    for c in ns:
        hl += "%02X" % (ord(c),)
    
    return hl

# generer le code hex pour une chaine de caracteres 
# par bloc de 16 caracteres
def generateHexData(offset, rectype, data):
    gdata = ''
    for i in range(0, len(data) / 16):
        gdata += hexLine(offset, 0, data[i*16:(i+1)*16]) + '\n'
        offset += 16
        
    if (len(data) % 16) != 0:
        gdata += hexLine(offset, 0, data[(i+1)*16:]) + '\n'
        
    return gdata

# convert an array to hex format
def convertArrToString(byte_per_data, t):
    s = []
    f = "%%0%dX" % (2 * byte_per_data)
    
    for v in t:
        if type(v).__name__ == 'int':
            ss = []
            j = byte_per_data
            while j > 0:
                ss.append(chr(v % 256))
                v = v / 256
                j -= 1
            ss.reverse()
            s += ss
        elif type(v).__name__ == 'str':
            s.append(v)
    
    ch = "".join(s)
    
    return ch

if __name__ == '__main__':
    h = HexEncoder()
    print h.hexData('anis')
    print h.hexData(2000)
    
        