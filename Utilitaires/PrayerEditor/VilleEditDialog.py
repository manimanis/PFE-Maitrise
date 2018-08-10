#Boa:Dialog:VilleEditDialog

import wx
import wx.lib.masked.textctrl
import libitl
import thread
import datetime
import hexcodec
import Villes
import Prayers
import PrayersTimesDialog

def create(parent):
    return VilleEditDialog(parent)

[wxID_VILLEEDITDIALOG, wxID_VILLEEDITDIALOGBTNCANCEL, 
 wxID_VILLEEDITDIALOGBTNOK, wxID_VILLEEDITDIALOGEDTDST, 
 wxID_VILLEEDITDIALOGEDTGMT, wxID_VILLEEDITDIALOGEDTLATITUDE, 
 wxID_VILLEEDITDIALOGEDTLONGITUDE, wxID_VILLEEDITDIALOGEDTMETHOD, 
 wxID_VILLEEDITDIALOGEDTPAYS, wxID_VILLEEDITDIALOGEDTREGION, 
 wxID_VILLEEDITDIALOGEDTVILLE, wxID_VILLEEDITDIALOGSTATICLINE1, 
 wxID_VILLEEDITDIALOGSTATICTEXT1, wxID_VILLEEDITDIALOGSTATICTEXT2, 
 wxID_VILLEEDITDIALOGSTATICTEXT3, wxID_VILLEEDITDIALOGSTATICTEXT4, 
 wxID_VILLEEDITDIALOGSTATICTEXT5, wxID_VILLEEDITDIALOGSTATICTEXT6, 
 wxID_VILLEEDITDIALOGSTATICTEXT8, 
] = [wx.NewId() for _init_ctrls in range(19)]

class VilleEditDialog(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_VILLEEDITDIALOG,
              name=u'VilleEditDialog', parent=prnt, pos=wx.Point(484, 244),
              size=wx.Size(303, 266), style=wx.DEFAULT_DIALOG_STYLE,
              title=u'Emplacement G\xe9ographique')
        self.SetClientSize(wx.Size(295, 232))

        self.edtPays = wx.TextCtrl(id=wxID_VILLEEDITDIALOGEDTPAYS,
              name=u'edtPays', parent=self, pos=wx.Point(96, 16),
              size=wx.Size(184, 21), style=0, value=u'Tunisie')
        self.edtPays.SetMaxLength(16)

        self.edtRegion = wx.TextCtrl(id=wxID_VILLEEDITDIALOGEDTREGION,
              name=u'edtRegion', parent=self, pos=wx.Point(96, 40),
              size=wx.Size(184, 21), style=0, value=u'Sousse')
        self.edtRegion.SetMaxLength(16)

        self.edtVille = wx.TextCtrl(id=wxID_VILLEEDITDIALOGEDTVILLE,
              name=u'edtVille', parent=self, pos=wx.Point(96, 64),
              size=wx.Size(184, 21), style=0, value=u'Hammam Sousse')
        self.edtVille.SetMaxLength(16)

        self.edtLongitude = wx.lib.masked.textctrl.TextCtrl(id=wxID_VILLEEDITDIALOGEDTLONGITUDE,
              name=u'edtLongitude', parent=self, pos=wx.Point(96, 88),
              size=wx.Size(100, 21), style=0, value=u'')
        self.edtLongitude.SetMask(u'###:##:## X')
        self.edtLongitude.SetAutoformat('')
        self.edtLongitude.SetDatestyle('MDY')
        self.edtLongitude.SetFormatcodes('')
        self.edtLongitude.SetDescription('')
        self.edtLongitude.SetExcludeChars('')
        self.edtLongitude.SetValidRegex('')

        self.edtLatitude = wx.lib.masked.textctrl.TextCtrl(id=wxID_VILLEEDITDIALOGEDTLATITUDE,
              name=u'edtLatitude', parent=self, pos=wx.Point(96, 112),
              size=wx.Size(100, 21), style=0, value=u'')
        self.edtLatitude.SetMask(u'###:##:## X')
        self.edtLatitude.SetAutoformat('')
        self.edtLatitude.SetDatestyle('MDY')
        self.edtLatitude.SetFormatcodes('')
        self.edtLatitude.SetDescription('')
        self.edtLatitude.SetExcludeChars('')
        self.edtLatitude.SetValidRegex('')

        self.edtGMT = wx.lib.masked.textctrl.TextCtrl(id=wxID_VILLEEDITDIALOGEDTGMT,
              name=u'edtGMT', parent=self, pos=wx.Point(96, 136),
              size=wx.Size(48, 21), style=0, value=u' . ')
        self.edtGMT.SetAutoformat('')
        self.edtGMT.SetMask(u'#.#')
        self.edtGMT.SetDatestyle('MDY')
        self.edtGMT.SetFormatcodes('')
        self.edtGMT.SetDescription('')
        self.edtGMT.SetExcludeChars('')
        self.edtGMT.SetValidRegex('')

        self.edtMethod = wx.Choice(choices=['None', 'Egypt Survey',
              'Karachi Shafii', 'Karachi Hanafi', 'North America',
              'Muslim League', 'Umm Alqurra', 'Fixed Ishaa'],
              id=wxID_VILLEEDITDIALOGEDTMETHOD, name=u'edtMethod', parent=self,
              pos=wx.Point(96, 160), size=wx.Size(130, 21), style=0)
        self.edtMethod.SetHelpText(u'')
        self.edtMethod.SetLabel(u'')
        self.edtMethod.SetSelection(5)

        self.edtDST = wx.CheckBox(id=wxID_VILLEEDITDIALOGEDTDST, label=u'DST',
              name=u'edtDST', parent=self, pos=wx.Point(152, 144),
              size=wx.Size(40, 13), style=0)
        self.edtDST.SetValue(False)

        self.btnOK = wx.Button(id=wxID_VILLEEDITDIALOGBTNOK, label=u'Modifier',
              name=u'btnOK', parent=self, pos=wx.Point(136, 200),
              size=wx.Size(75, 24), style=0)
        self.btnOK.Bind(wx.EVT_BUTTON, self.OnBtnOKButton,
              id=wxID_VILLEEDITDIALOGBTNOK)

        self.staticText1 = wx.StaticText(id=wxID_VILLEEDITDIALOGSTATICTEXT1,
              label=u'Pays', name='staticText1', parent=self, pos=wx.Point(16,
              16), size=wx.Size(72, 21), style=wx.ST_NO_AUTORESIZE)

        self.btnCancel = wx.Button(id=wxID_VILLEEDITDIALOGBTNCANCEL,
              label=u'Annuler', name=u'btnCancel', parent=self,
              pos=wx.Point(216, 200), size=wx.Size(75, 23), style=0)
        self.btnCancel.Bind(wx.EVT_BUTTON, self.OnBtnCancelButton,
              id=wxID_VILLEEDITDIALOGBTNCANCEL)

        self.staticText2 = wx.StaticText(id=wxID_VILLEEDITDIALOGSTATICTEXT2,
              label=u'R\xe9gion', name='staticText2', parent=self,
              pos=wx.Point(16, 40), size=wx.Size(72, 21),
              style=wx.ST_NO_AUTORESIZE)

        self.staticText3 = wx.StaticText(id=wxID_VILLEEDITDIALOGSTATICTEXT3,
              label=u'Ville', name='staticText3', parent=self, pos=wx.Point(16,
              64), size=wx.Size(72, 21), style=wx.ST_NO_AUTORESIZE)

        self.staticText4 = wx.StaticText(id=wxID_VILLEEDITDIALOGSTATICTEXT4,
              label=u'Longitude', name='staticText4', parent=self,
              pos=wx.Point(16, 88), size=wx.Size(72, 21),
              style=wx.ST_NO_AUTORESIZE)

        self.staticText5 = wx.StaticText(id=wxID_VILLEEDITDIALOGSTATICTEXT5,
              label=u'Latitude', name='staticText5', parent=self,
              pos=wx.Point(16, 112), size=wx.Size(72, 21),
              style=wx.ST_NO_AUTORESIZE)

        self.staticText6 = wx.StaticText(id=wxID_VILLEEDITDIALOGSTATICTEXT6,
              label=u'Fuseau horaire', name='staticText6', parent=self,
              pos=wx.Point(16, 136), size=wx.Size(72, 21),
              style=wx.ST_NO_AUTORESIZE)

        self.staticText8 = wx.StaticText(id=wxID_VILLEEDITDIALOGSTATICTEXT8,
              label=u'M\xe9thode calcul', name='staticText8', parent=self,
              pos=wx.Point(16, 160), size=wx.Size(72, 21),
              style=wx.ST_NO_AUTORESIZE)

        self.staticLine1 = wx.StaticLine(id=wxID_VILLEEDITDIALOGSTATICLINE1,
              name='staticLine1', parent=self, pos=wx.Point(8, 192),
              size=wx.Size(280, 2), style=0)
        self.staticLine1.SetMaxSize(wx.Size(1, 2))
        self.staticLine1.SetMinSize(wx.Size(1, 2))

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.CenterOnParent()
        self.ville = Villes.Ville()
        self.initUIFromData()
    
    def setVille(self, ville):
        self.ville.deserialize(ville.serialize())
        
    def getVille(self):
        return self.ville
    
    def initUIFromData(self):
        data = self.ville
        
        self.edtPays.SetLabel(data.getCountry())
        self.edtRegion.SetLabel(data.getRegion())
        self.edtVille.SetLabel(data.getVille())
        self.edtLongitude.SetLabel(data.getLongitude().format())
        self.edtLatitude.SetLabel(data.getLatitude().format())
        self.edtGMT.SetLabel("%1.1f" % data.getGMT())
        self.edtDST.SetValue(data.getDST())
        self.edtMethod.SetSelection(data.getMethod())
        
    def initDataFromUI(self):
        data = self.ville
        
        data.setCountry(self.edtPays.GetLabel())
        data.setRegion(self.edtRegion.GetLabel())
        data.setVille(self.edtVille.GetLabel())
        data.getLatitude().parseString(self.edtLatitude.GetLabel())
        data.getLongitude().parseString(self.edtLongitude.GetLabel())
        data.setGMT(float(self.edtGMT.GetLabel()))
        data.setDST(int(self.edtDST.GetValue()))
        data.setMethod(self.edtMethod.GetSelection())

    def OnBtnCancelButton(self, event):
        self.EndModal(wx.ID_CANCEL)

    def OnBtnOKButton(self, event):
        self.initDataFromUI()
        self.EndModal(wx.ID_OK)
