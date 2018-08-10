#Boa:Frame:MainFrame

import wx
import EventsDialog
import VillesDialog
import LcdMsgDialog
import Villes
import Prayers
import PrayersTimesDialog
import TownsSelectDialog
import hexcodec
from VilleChoiceDialog import *

def create(parent):
    return MainFrame(parent)

[wxID_MAINFRAME, wxID_MAINFRAMEBTNEVENTS, wxID_MAINFRAMEBTNGENPRAYERSHEX, 
 wxID_MAINFRAMEBTNPRAYERSTIMES, wxID_MAINFRAMEBTNSELECT, 
 wxID_MAINFRAMEBTNTOWNSCOORDS, wxID_MAINFRAMESTATICLINE1, 
] = [wx.NewId() for _init_ctrls in range(7)]

class MainFrame(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_MAINFRAME, name='', parent=prnt,
              pos=wx.Point(613, 294), size=wx.Size(377, 424),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Prayer Editor')
        self.SetClientSize(wx.Size(369, 390))
        self.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_BTNFACE))

        self.btnPrayersTimes = wx.Button(id=wxID_MAINFRAMEBTNPRAYERSTIMES,
              label=u'Edition des horaires de pri\xe8res...',
              name=u'btnPrayersTimes', parent=self, pos=wx.Point(16, 160),
              size=wx.Size(336, 64), style=0)
        self.btnPrayersTimes.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.btnPrayersTimes.Bind(wx.EVT_BUTTON, self.OnBtnPrayersTimesButton,
              id=wxID_MAINFRAMEBTNPRAYERSTIMES)

        self.btnEvents = wx.Button(id=wxID_MAINFRAMEBTNEVENTS,
              label=u'Gestionnaire des \xe9v\xe8nements', name=u'btnEvents',
              parent=self, pos=wx.Point(16, 232), size=wx.Size(336, 64),
              style=0)
        self.btnEvents.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.btnEvents.Bind(wx.EVT_BUTTON, self.OnBtnEventsButton,
              id=wxID_MAINFRAMEBTNEVENTS)

        self.btnGenPrayersHex = wx.Button(id=wxID_MAINFRAMEBTNGENPRAYERSHEX,
              label=u'G\xe9n\xe9rer fichier "Hex" Pri\xe8res...',
              name=u'btnGenPrayersHex', parent=self, pos=wx.Point(16, 312),
              size=wx.Size(336, 64), style=0)
        self.btnGenPrayersHex.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Tahoma'))
        self.btnGenPrayersHex.Bind(wx.EVT_BUTTON, self.OnBtnGenPrayersHexButton,
              id=wxID_MAINFRAMEBTNGENPRAYERSHEX)

        self.btnTownsCoords = wx.Button(id=wxID_MAINFRAMEBTNTOWNSCOORDS,
              label=u'Emplacement des Villes...', name=u'btnTownsCoords',
              parent=self, pos=wx.Point(16, 88), size=wx.Size(336, 64),
              style=0)
        self.btnTownsCoords.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.btnTownsCoords.Bind(wx.EVT_BUTTON, self.OnBtnTownsCoordsButton,
              id=wxID_MAINFRAMEBTNTOWNSCOORDS)

        self.staticLine1 = wx.StaticLine(id=wxID_MAINFRAMESTATICLINE1,
              name='staticLine1', parent=self, pos=wx.Point(8, 304),
              size=wx.Size(352, 2), style=0)

        self.btnSelect = wx.Button(id=wxID_MAINFRAMEBTNSELECT,
              label=u'S\xe9lection des villes...', name=u'btnSelect',
              parent=self, pos=wx.Point(16, 16), size=wx.Size(336, 64),
              style=0)
        self.btnSelect.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.btnSelect.Bind(wx.EVT_BUTTON, self.OnBtnSelectButton,
              id=wxID_MAINFRAMEBTNSELECT)

    def __init__(self, parent):
        self._init_ctrls(parent)


    def OnBtnEventsButton(self, event):
        dlg = EventsDialog.create(self)
        dlg.ShowModal()

    def OnBtnMessagesButton(self, event):
        dlg = LcdMsgDialog.create(self)
        dlg.ShowModal()

    def OnBtnPrayersTimesButton(self, event):
        choice = VilleChoiceDialog(self)
        if choice.ShowModal() == wx.ID_OK:            
            dlg = PrayersTimesDialog.create(self)
            dlg.setVille(choice.GetData())
            dlg.loadData()
            dlg.ShowModal()

    def OnBtnTownsCoordsButton(self, event):
        dlg = VillesDialog.create(self)
        dlg.ShowModal()

    def OnBtnGenPrayersHexButton(self, event):
        svc = Villes.SelectedVillesCollection()
        
        pr = ""
        for i in range(0, svc.getCount()):
            ypt = Prayers.YearPrayersTimes(svc.getData(i))
            pr += repr(ypt)
            
        f = open('prayers.hex', 'w')
        f.write(hexcodec.generateHexData(0, 0, pr))
        f.write(":00000001FF\n")
        f.close()

    def OnBtnSelectButton(self, event):
        dlg = TownsSelectDialog.create(self)
        dlg.ShowModal()
        
        
