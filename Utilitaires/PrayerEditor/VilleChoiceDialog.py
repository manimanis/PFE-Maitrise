import wx
import Villes

class VilleChoiceDialog(wx.SingleChoiceDialog):
    def __init__(self, parent):
        self.villes = Villes.SelectedVillesCollection()
        self.villes.load()
        
        vin = []
        for i in range(0, self.villes.getCount()):
            self.villes.moveTo(i)
            data = self.villes.getData()
            if data.getLongitude().getFloat() != 0 and data.getLatitude().getFloat() != 0:
                vin.append("%s - %s - %s" % (data.getCountry().capitalize(), data.getRegion(), data.getVille()))
                
        wx.SingleChoiceDialog.__init__(self, parent, 'S\xe9lectionner une ville', 'Villes', vin, wx.CHOICEDLG_STYLE)
        
    def GetData(self):
        if self.GetSelection() != -1:
            self.villes.moveTo(self.GetSelection())
            return self.villes.getData()
    
    def GetPos(self):
        return self.villes.getPos()
    