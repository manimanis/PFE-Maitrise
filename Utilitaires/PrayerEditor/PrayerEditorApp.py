#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import MainFrame

modules ={u'EventEditDialog': [0, u'*', u'EventEditDialog.py'],
 u'Events': [0, u'*', u'Events.py'],
 u'EventsDialog': [0, u'*', u'EventsDialog.py'],
 u'LcdMsgDialog': [0, u'u', u'LcdMsgDialog.py'],
 u'MainFrame': [1, u'Fenetre Principale', u'MainFrame.py'],
 u'Messages': [0, u'u', u'Messages.py'],
 u'Prayers': [0, u'**', u'Prayers.py'],
 u'PrayersEditDialog': [0, u'**', u'PrayersEditDialog.py'],
 u'PrayersTimesDialog': [0, u'**', u'PrayersTimesDialog.py'],
 u'Progression': [0, '', u'Progression.txt'],
 u'TownsSelectDialog': [0, u'*', u'TownsSelectDialog.py'],
 u'VilleChoiceDialog': [0, u'*', u'VilleChoiceDialog.py'],
 u'VilleEditDialog': [0, u'*', u'VilleEditDialog.py'],
 u'Villes': [0, u'*', u'Villes.py'],
 u'VillesDialog': [0, u'*', u'VillesDialog.py'],
 u'WorldTowns': [0, u'inutile', u'WorldTowns.py'],
 u'abstracts': [0, u'*', u'abstracts.py'],
 u'hexcodec': [0, u'*', u'hexcodec.py'],
 u'setup': [0, '', u'setup.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = MainFrame.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
