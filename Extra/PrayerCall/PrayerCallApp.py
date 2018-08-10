#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import MainFrame
import libitl
import pickle

modules ={u'AlertFrame': [0, '', u'AlertFrame.py'],
 u'MainFrame': [1, 'Main frame of Application', u'MainFrame.py'],
 u'boussole': [0, '', u'boussole.py'],
 u'location_parser': [0, '', u'location_parser.py'],
 u'settings_dialog': [0, '', u'settings_dialog.py'],
 u'setup': [0, '', u'setup.py'],
 u'sounds': [0, '', u'sounds.py']}

class BoaApp(wx.App):
    def loadConfig(self):
        self.loc = libitl.Location()
        self.loc.setLatitude(libitl.dms2Decimal(35, 50, 0, 'N'))
        self.loc.setLongitude(libitl.dms2Decimal(10, 38, 0, 'N'))
        self.loc.setGmt(1.0)
        self.loc.setDST(0.0)
        self.loc.setSeaLevel(0)
        self.loc.setPressure(1010)
        self.loc.setTemperature(10)
        self.loc.setCountryName(u'Tunisie')
        self.loc.setTownName(u'Sousse')
        location = self.toHex(pickle.dumps(self.loc))

        self.conf = libitl.Method(libitl.EGYPT_SURVEY)
        self.conf.setRoundMethod(0)
        config = self.toHex(pickle.dumps(self.conf))
        
        cfg = wx.Config(self.GetAppName())
        if cfg.HasEntry('loc') and cfg.HasEntry('conf'):  
          location = cfg.Read('loc')
          config = cfg.Read('conf')
        else:
          self.saveConfig(location, config)
        
        self.loc = pickle.loads(self.fromHex(location))
        self.conf = pickle.loads(self.fromHex(config))
        
    def saveConfig(self, loc, conf):
        cfg = wx.Config(self.GetAppName())
        cfg.Write('loc', self.toHex(pickle.dumps(loc)))
        cfg.Write('conf', self.toHex(pickle.dumps(conf)))
        
    def toHex(self, ch):
      s = ""
      for c in ch:
        s += "\\x%02x" % (ord(c),)
      return s
      
    def fromHex(self, ch):
      return eval('"'+ch+'"')
        
    def OnInit(self):
        self.SetAppName('Prayer Call')
        self.SetClassName('ManiSoft')
        self.SetVendorName('ManiSoft')
        
        self.loadConfig()
        
        return True
    
    def createWindow(self):
        self.main = MainFrame.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)

def main():
    app = BoaApp(0)
    
    m_check = wx.SingleInstanceChecker(app.GetAppName())
    if (m_check.IsAnotherRunning()):
        wx.MessageBox('Only one instance of this application can run at once.', app.GetAppName(), wx.ICON_INFORMATION)            
        del m_check
        app.Destroy()
        return False
    
    app.createWindow()
    app.MainLoop()

if __name__ == '__main__':
    main()
