#Boa:Dialog:PrayersEditDialog

import wx
from Prayers import *

def create(parent):
    return PrayersEditDialog(parent)

[wxID_PRAYERSEDITDIALOG, wxID_PRAYERSEDITDIALOGBTNCANCEL, 
 wxID_PRAYERSEDITDIALOGBTNVALIDER, wxID_PRAYERSEDITDIALOGEDTASR, 
 wxID_PRAYERSEDITDIALOGEDTFAJR, wxID_PRAYERSEDITDIALOGEDTISHAA, 
 wxID_PRAYERSEDITDIALOGEDTJOUR, wxID_PRAYERSEDITDIALOGEDTMAGHREB, 
 wxID_PRAYERSEDITDIALOGEDTSHURUQ, wxID_PRAYERSEDITDIALOGEDTTHUHR, 
 wxID_PRAYERSEDITDIALOGSTATICLINE1, wxID_PRAYERSEDITDIALOGSTATICTEXT10, 
 wxID_PRAYERSEDITDIALOGSTATICTEXT11, wxID_PRAYERSEDITDIALOGSTATICTEXT12, 
 wxID_PRAYERSEDITDIALOGSTATICTEXT13, wxID_PRAYERSEDITDIALOGSTATICTEXT14, 
 wxID_PRAYERSEDITDIALOGSTATICTEXT7, wxID_PRAYERSEDITDIALOGSTATICTEXT9, 
] = [wx.NewId() for _init_ctrls in range(18)]

class PrayersEditDialog(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_PRAYERSEDITDIALOG,
              name=u'PrayersEditDialog', parent=prnt, pos=wx.Point(431, 204),
              size=wx.Size(333, 161), style=wx.DEFAULT_DIALOG_STYLE,
              title=u'Editer horaires')
        self.SetClientSize(wx.Size(325, 127))

        self.btnValider = wx.Button(id=wxID_PRAYERSEDITDIALOGBTNVALIDER,
              label=u'Valider', name=u'btnValider', parent=self,
              pos=wx.Point(156, 96), size=wx.Size(75, 23), style=0)
        self.btnValider.Bind(wx.EVT_BUTTON, self.OnBtnValiderButton,
              id=wxID_PRAYERSEDITDIALOGBTNVALIDER)

        self.staticLine1 = wx.StaticLine(id=wxID_PRAYERSEDITDIALOGSTATICLINE1,
              name='staticLine1', parent=self, pos=wx.Point(4, 88),
              size=wx.Size(312, 2), style=0)
        self.staticLine1.SetMaxSize(wx.Size(1, 2))
        self.staticLine1.SetMinSize(wx.Size(1, 2))

        self.staticText7 = wx.StaticText(id=wxID_PRAYERSEDITDIALOGSTATICTEXT7,
              label=u'Jour', name='staticText7', parent=self, pos=wx.Point(8,
              8), size=wx.Size(48, 21), style=wx.ST_NO_AUTORESIZE)
        self.staticText7.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))
        self.staticText7.SetHelpText(u'')
        self.staticText7.SetForegroundColour(wx.Colour(64, 0, 64))

        self.staticText9 = wx.StaticText(id=wxID_PRAYERSEDITDIALOGSTATICTEXT9,
              label=u'Fajr', name='staticText9', parent=self, pos=wx.Point(8,
              36), size=wx.Size(48, 21), style=wx.ST_NO_AUTORESIZE)

        self.edtFajr = wx.TextCtrl(id=wxID_PRAYERSEDITDIALOGEDTFAJR,
              name=u'edtFajr', parent=self, pos=wx.Point(60, 36),
              size=wx.Size(48, 21), style=0, value=u'')

        self.staticText10 = wx.StaticText(id=wxID_PRAYERSEDITDIALOGSTATICTEXT10,
              label=u'Shuruq', name='staticText10', parent=self,
              pos=wx.Point(112, 36), size=wx.Size(48, 21),
              style=wx.ST_NO_AUTORESIZE)

        self.edtShuruq = wx.TextCtrl(id=wxID_PRAYERSEDITDIALOGEDTSHURUQ,
              name=u'edtShuruq', parent=self, pos=wx.Point(164, 36),
              size=wx.Size(48, 21), style=0, value=u'')

        self.staticText11 = wx.StaticText(id=wxID_PRAYERSEDITDIALOGSTATICTEXT11,
              label=u'Thuhr', name='staticText11', parent=self,
              pos=wx.Point(216, 36), size=wx.Size(48, 21),
              style=wx.ST_NO_AUTORESIZE)

        self.edtThuhr = wx.TextCtrl(id=wxID_PRAYERSEDITDIALOGEDTTHUHR,
              name=u'edtThuhr', parent=self, pos=wx.Point(268, 36),
              size=wx.Size(48, 21), style=0, value=u'')

        self.staticText12 = wx.StaticText(id=wxID_PRAYERSEDITDIALOGSTATICTEXT12,
              label=u'Asr', name='staticText12', parent=self, pos=wx.Point(8,
              58), size=wx.Size(48, 21), style=wx.ST_NO_AUTORESIZE)

        self.edtAsr = wx.TextCtrl(id=wxID_PRAYERSEDITDIALOGEDTASR,
              name=u'edtAsr', parent=self, pos=wx.Point(60, 60),
              size=wx.Size(48, 21), style=0, value=u'')

        self.staticText13 = wx.StaticText(id=wxID_PRAYERSEDITDIALOGSTATICTEXT13,
              label=u'Maghreb', name='staticText13', parent=self,
              pos=wx.Point(112, 58), size=wx.Size(48, 21),
              style=wx.ST_NO_AUTORESIZE)

        self.edtMaghreb = wx.TextCtrl(id=wxID_PRAYERSEDITDIALOGEDTMAGHREB,
              name=u'edtMaghreb', parent=self, pos=wx.Point(164, 60),
              size=wx.Size(48, 21), style=0, value=u'')

        self.staticText14 = wx.StaticText(id=wxID_PRAYERSEDITDIALOGSTATICTEXT14,
              label=u'Ishaa', name='staticText14', parent=self,
              pos=wx.Point(216, 62), size=wx.Size(48, 21),
              style=wx.ST_NO_AUTORESIZE)

        self.edtIshaa = wx.TextCtrl(id=wxID_PRAYERSEDITDIALOGEDTISHAA,
              name=u'edtIshaa', parent=self, pos=wx.Point(268, 60),
              size=wx.Size(48, 21), style=0, value=u'')

        self.edtJour = wx.StaticText(id=wxID_PRAYERSEDITDIALOGEDTJOUR,
              label=u'01/01', name=u'edtJour', parent=self, pos=wx.Point(60, 8),
              size=wx.Size(56, 19),
              style=wx.ST_NO_AUTORESIZE | wx.ALIGN_CENTRE)
        self.edtJour.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'MS Shell Dlg 2'))

        self.btnCancel = wx.Button(id=wxID_PRAYERSEDITDIALOGBTNCANCEL,
              label=u'Annuler', name=u'btnCancel', parent=self,
              pos=wx.Point(240, 96), size=wx.Size(75, 23), style=0)
        self.btnCancel.Bind(wx.EVT_BUTTON, self.OnBtnCancelButton,
              id=wxID_PRAYERSEDITDIALOGBTNCANCEL)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.CenterOnParent()
    
    def setPrayersTimes(self, prayers):
        self.prayers = PrayersTimes()
        self.prayers.deserialize(prayers.serialize())
        
    def getPrayersTimes(self):
        return self.prayers
        
    def initUIFromData(self):
        self.edtJour.SetLabel(self.prayers.getDay())
        self.edtFajr.SetLabel(str(self.prayers.getFajr()))
        self.edtShuruq.SetLabel(str(self.prayers.getShuruq()))
        self.edtThuhr.SetLabel(str(self.prayers.getDhohr()))
        self.edtAsr.SetLabel(str(self.prayers.getAsr()))
        self.edtMaghreb.SetLabel(str(self.prayers.getMaghreb()))
        self.edtIshaa.SetLabel(str(self.prayers.getIshaa()))

    def initDataFromUI(self):
        self.prayers.getFajr().parseString(self.edtFajr.GetLabel())
        self.prayers.getShuruq().parseString(self.edtShuruq.GetLabel())
        self.prayers.getDhohr().parseString(self.edtThuhr.GetLabel())
        self.prayers.getAsr().parseString(self.edtAsr.GetLabel())
        self.prayers.getMaghreb().parseString(self.edtMaghreb.GetLabel())
        self.prayers.getIshaa().parseString(self.edtIshaa.GetLabel())
    
    def OnBtnValiderButton(self, event):
        self.initDataFromUI()
        self.EndModal(wx.ID_OK)

    def OnBtnCancelButton(self, event):
        self.EndModal(wx.ID_CANCEL)
