#Boa:Dialog:DlgSettings

import wx
import libitl
import copy

def create(parent):
    return DlgSettings(parent)

[wxID_DLGSETTINGS, wxID_DLGSETTINGSBTN_CANCEL, wxID_DLGSETTINGSBTN_OK, 
 wxID_DLGSETTINGSCALC_STATIC_BOX, wxID_DLGSETTINGSDST, 
 wxID_DLGSETTINGSGEO_STATIC_BOX, wxID_DLGSETTINGSGMT, 
 wxID_DLGSETTINGSLATITUDE_DEG, wxID_DLGSETTINGSLATITUDE_MIN, 
 wxID_DLGSETTINGSLBL_GMT, wxID_DLGSETTINGSLBL_LATITUDE, 
 wxID_DLGSETTINGSLBL_LATITUDE_DEG, wxID_DLGSETTINGSLBL_LATITUDE_MIN, 
 wxID_DLGSETTINGSLBL_LONGITUDE, wxID_DLGSETTINGSLBL_LONGITUDE_DEG, 
 wxID_DLGSETTINGSLBL_LONGITUDE_MIN, wxID_DLGSETTINGSLBL_PAYS, 
 wxID_DLGSETTINGSLBL_PRESSURE, wxID_DLGSETTINGSLBL_SEA_LEVEL, 
 wxID_DLGSETTINGSLBL_TEMPERATURE, wxID_DLGSETTINGSLBL_VILLE, 
 wxID_DLGSETTINGSLONGITUDE_DEG, wxID_DLGSETTINGSLONGITUDE_MIN, 
 wxID_DLGSETTINGSMETHODS, wxID_DLGSETTINGSPAYS, wxID_DLGSETTINGSPRESSURE, 
 wxID_DLGSETTINGSSEA_LEVEL, wxID_DLGSETTINGSTEMPERATURE, 
 wxID_DLGSETTINGSVILLE, 
] = [wx.NewId() for _init_ctrls in range(29)]

class DlgSettings(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DLGSETTINGS, name=u'DlgSettings',
              parent=prnt, pos=wx.Point(408, 292), size=wx.Size(487, 276),
              style=wx.DEFAULT_DIALOG_STYLE,
              title=u'\u062a\u0639\u062f\u064a\u0644\u0627\u062a \u0628\u0631\u0646\u0627\u0645\u062c \u0627\u0644\u0622\u0630\u0627\u0646')
        self.SetClientSize(wx.Size(479, 249))
        self.CenterOnScreen(wx.BOTH)
        self.Bind(wx.EVT_INIT_DIALOG, self.OnDlgSettingsInitDialog)

        self.ville = wx.TextCtrl(id=wxID_DLGSETTINGSVILLE, name=u'ville',
              parent=self, pos=wx.Point(231, 17), size=wx.Size(160, 21),
              style=wx.TE_RIGHT, value=u'')

        self.pays = wx.TextCtrl(id=wxID_DLGSETTINGSPAYS, name=u'pays',
              parent=self, pos=wx.Point(24, 17), size=wx.Size(160, 21),
              style=wx.TE_RIGHT, value=u'')

        self.longitude_deg = wx.TextCtrl(id=wxID_DLGSETTINGSLONGITUDE_DEG,
              name=u'longitude_deg', parent=self, pos=wx.Point(343, 44),
              size=wx.Size(48, 21), style=wx.TE_CENTER, value=u'')

        self.longitude_min = wx.TextCtrl(id=wxID_DLGSETTINGSLONGITUDE_MIN,
              name=u'longitude_min', parent=self, pos=wx.Point(275, 44),
              size=wx.Size(48, 21), style=wx.TE_CENTER, value=u'')

        self.latitude_deg = wx.TextCtrl(id=wxID_DLGSETTINGSLATITUDE_DEG,
              name=u'latitude_deg', parent=self, pos=wx.Point(136, 43),
              size=wx.Size(48, 21), style=wx.TE_CENTER, value=u'')

        self.latitude_min = wx.TextCtrl(id=wxID_DLGSETTINGSLATITUDE_MIN,
              name=u'latitude_min', parent=self, pos=wx.Point(69, 43),
              size=wx.Size(48, 21), style=wx.TE_CENTER, value=u'')

        self.gmt = wx.Choice(choices=[], id=wxID_DLGSETTINGSGMT, name=u'gmt',
              parent=self, pos=wx.Point(293, 72), size=wx.Size(100, 21),
              style=wx.ALIGN_RIGHT)

        self.sea_level = wx.TextCtrl(id=wxID_DLGSETTINGSSEA_LEVEL,
              name=u'sea_level', parent=self, pos=wx.Point(23, 72),
              size=wx.Size(160, 21), style=wx.TE_RIGHT, value=u'')

        self.pressure = wx.TextCtrl(id=wxID_DLGSETTINGSPRESSURE,
              name=u'pressure', parent=self, pos=wx.Point(293, 99),
              size=wx.Size(100, 21), style=wx.TE_RIGHT, value=u'')

        self.temperature = wx.TextCtrl(id=wxID_DLGSETTINGSTEMPERATURE,
              name=u'temperature', parent=self, pos=wx.Point(83, 99),
              size=wx.Size(100, 21), style=wx.TE_RIGHT, value=u'')

        self.dst = wx.CheckBox(id=wxID_DLGSETTINGSDST,
              label=u'\u0627\u0644\u062a\u0648\u0642\u064a\u062a \u0627\u0644\u0635\u0651\u064a\u0641\u064a',
              name=u'dst', parent=self, pos=wx.Point(170, 128), size=wx.Size(96,
              13), style=0)
        self.dst.SetValue(False)

        self.methods = wx.Choice(choices=[], id=wxID_DLGSETTINGSMETHODS,
              name=u'methods', parent=self, pos=wx.Point(193, 184),
              size=wx.Size(272, 21), style=0)

        self.geo_static_box = wx.StaticBox(id=wxID_DLGSETTINGSGEO_STATIC_BOX,
              label=u'\u0627\u0644\u0645\u0648\u0642\u0639 \u0627\u0644\u062c\u063a\u0631\u0627\u0641\u064a',
              name=u'geo_static_box', parent=self, pos=wx.Point(7, 1),
              size=wx.Size(469, 159), style=0)

        self.lbl_ville = wx.StaticText(id=wxID_DLGSETTINGSLBL_VILLE,
              label=u'\u0627\u0644\u0645\u062f\u064a\u0646\u0629',
              name=u'lbl_ville', parent=self, pos=wx.Point(402, 21),
              size=wx.Size(32, 13), style=wx.ALIGN_RIGHT)

        self.lbl_pays = wx.StaticText(id=wxID_DLGSETTINGSLBL_PAYS,
              label=u'\u0627\u0644\u0628\u0644\u062f', name=u'lbl_pays',
              parent=self, pos=wx.Point(195, 21), size=wx.Size(20, 13),
              style=wx.ALIGN_RIGHT)

        self.lbl_longitude = wx.StaticText(id=wxID_DLGSETTINGSLBL_LONGITUDE,
              label=u'\u062e\u0637\u0651 \u0627\u0644\u0637\u0648\u0644',
              name=u'lbl_longitude', parent=self, pos=wx.Point(402, 48),
              size=wx.Size(44, 13), style=wx.ALIGN_RIGHT)

        self.lbl_longitude_deg = wx.StaticText(id=wxID_DLGSETTINGSLBL_LONGITUDE_DEG,
              label=u'\xb0', name=u'lbl_longitude_deg', parent=self,
              pos=wx.Point(330, 48), size=wx.Size(5, 13), style=0)

        self.lbl_latitude = wx.StaticText(id=wxID_DLGSETTINGSLBL_LATITUDE,
              label=u'\u062e\u0637\u0651 \u0627\u0644\u0639\u0631\u0636',
              name=u'lbl_latitude', parent=self, pos=wx.Point(195, 47),
              size=wx.Size(48, 13), style=wx.ALIGN_RIGHT)

        self.lbl_longitude_min = wx.StaticText(id=wxID_DLGSETTINGSLBL_LONGITUDE_MIN,
              label=u'"', name=u'lbl_longitude_min', parent=self,
              pos=wx.Point(262, 48), size=wx.Size(4, 13), style=0)

        self.lbl_latitude_deg = wx.StaticText(id=wxID_DLGSETTINGSLBL_LATITUDE_DEG,
              label=u'\xb0', name=u'lbl_latitude_deg', parent=self,
              pos=wx.Point(124, 47), size=wx.Size(5, 13), style=0)

        self.lbl_latitude_min = wx.StaticText(id=wxID_DLGSETTINGSLBL_LATITUDE_MIN,
              label=u'"', name=u'lbl_latitude_min', parent=self,
              pos=wx.Point(56, 47), size=wx.Size(4, 13), style=0)

        self.lbl_gmt = wx.StaticText(id=wxID_DLGSETTINGSLBL_GMT,
              label=u'\u0641\u0627\u0631\u0642 \u0627\u0644\u062a\u0648\u0642\u064a\u062a',
              name=u'lbl_gmt', parent=self, pos=wx.Point(402, 76),
              size=wx.Size(59, 13), style=wx.ALIGN_RIGHT)

        self.lbl_sea_level = wx.StaticText(id=wxID_DLGSETTINGSLBL_SEA_LEVEL,
              label=u'\u0645\u0633\u062a\u0648\u0649 \u0633\u0637\u062d \u0627\u0644\u0628\u062d\u0631',
              name=u'lbl_sea_level', parent=self, pos=wx.Point(195, 68),
              size=wx.Size(57, 28), style=0)

        self.lbl_pressure = wx.StaticText(id=wxID_DLGSETTINGSLBL_PRESSURE,
              label=u'\u0627\u0644\u0636\u063a\u0637 \u0627\u0644\u062c\u0648\u0651\u064a',
              name=u'lbl_pressure', parent=self, pos=wx.Point(403, 103),
              size=wx.Size(60, 13), style=wx.ALIGN_RIGHT)

        self.lbl_temperature = wx.StaticText(id=wxID_DLGSETTINGSLBL_TEMPERATURE,
              label=u'\u062f\u0631\u062c\u0629 \u0627\u0644\u062d\u0631\u0627\u0631\u0629',
              name=u'lbl_temperature', parent=self, pos=wx.Point(199, 103),
              size=wx.Size(55, 13), style=wx.ALIGN_RIGHT)

        self.calc_static_box = wx.StaticBox(id=wxID_DLGSETTINGSCALC_STATIC_BOX,
              label=u'\u0637\u0631\u064a\u0642\u0629 \u062d\u0633\u0627\u0628 \u0627\u0644\u0648\u0642\u062a',
              name=u'calc_static_box', parent=self, pos=wx.Point(8, 164),
              size=wx.Size(469, 48), style=0)

        self.btn_ok = wx.Button(id=wx.ID_OK,
              label=u'\u0645\u0648\u0627\u0641\u0642', name=u'btn_ok',
              parent=self, pos=wx.Point(400, 220), size=wx.Size(75, 23),
              style=0)
        self.btn_ok.Bind(wx.EVT_BUTTON, self.OnBtn_okButton)

        self.btn_cancel = wx.Button(id=wx.ID_CANCEL,
              label=u'\u0625\u0644\u063a\u0627\u0621', name=u'btn_cancel',
              parent=self, pos=wx.Point(316, 220), size=wx.Size(75, 23),
              style=0)
        self.btn_cancel.Bind(wx.EVT_BUTTON, self.OnBtn_cancelButton)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBtn_okButton(self, event):
        #loc struct
        self.loc.setLatitude(libitl.dms2Decimal(int(self.latitude_deg.GetValue()), int(self.latitude_min.GetValue()), 0))
        self.loc.setLongitude(libitl.dms2Decimal(int(self.longitude_deg.GetValue()), int(self.longitude_min.GetValue()), 0))
        
        self.loc.setTownName(self.ville.GetValue())
        self.loc.setCountryName(self.pays.GetValue())
        
        self.loc.setPressure(float(self.pressure.GetValue()))
        self.loc.setTemperature(float(self.temperature.GetValue()))
        
        self.loc.setDST(self.dst.GetValue())
        
        self.loc.setSeaLevel(float(self.sea_level.GetValue()))
        self.loc.setGmt(self.gmt.GetClientData(self.gmt.GetSelection()))
        
        #conf struct
        self.conf.setMethod(self.methods.GetClientData(self.methods.GetSelection()))
        event.Skip()

    def OnBtn_cancelButton(self, event):
        event.Skip()

    def OnDlgSettingsInitDialog(self, event):
        gmt = -12.0
        
        while gmt <= 12.0:
            self.gmt.Append(u'%+0.1f   GMT' % gmt, gmt)
            gmt += 0.5
        methodes = [(libitl.NONE, u'\u0644\u0627 \u0634\u064a\u0621'),
                (libitl.EGYPT_SURVEY, u'\u0627\u0644\u0637\u0631\u064a\u0642\u0629 \u0627\u0644\u0645\u0635\u0631\u064a\u0651\u0629'),
                (libitl.KARACHI_SHAF, u'\u0627\u0644\u0637\u0631\u064a\u0642\u0629 \u0627\u0644\u0634\u0651\u0627\u0641\u0639\u064a\u0629'),
                (libitl.KARACHI_HANAF, u'\u0627\u0644\u0637\u0631\u064a\u0642\u0629 \u0627\u0644\u062d\u0646\u0641\u064a\u0651\u0629'),
                (libitl.NORTH_AMERICA, u'\u0627\u0644\u0637\u0631\u064a\u0642\u0629 \u0627\u0644\u0623\u0645\u0631\u064a\u0643\u064a\u0629'),
                (libitl.MUSLIM_LEAGUE, u'\u0637\u0631\u064a\u0642\u0629 \u0627\u0644\u0645\u0646\u0638\u0651\u0645\u0629 \u0627\u0644\u0625\u0633\u0644\u0627\u0645\u064a\u0651\u0629'),
                (libitl.UMM_ALQURRA, u'\u0637\u0631\u064a\u0642\u0629 \u0623\u0645\u0651 \u0627\u0644\u0642\u0631\u0649'),
                (libitl.FIXED_ISHAA, u'\u0637\u0631\u064a\u0642\u0629 \u0627\u0644\u0648\u0642\u062a \u0627\u0644\u062b\u0651\u0627\u0628\u062a')]
        
        for met in methodes:
            self.methods.Append(met[1], met[0])
        
        i = 0
        count = self.gmt.GetCount()
        idx = wx.NOT_FOUND
        while i < count:
            val = self.gmt.GetClientData(i)
            if val == self.loc.getGmt():
                idx = i
            i += 1
        self.gmt.SetSelection(idx)
        
        
        i = 0
        count = self.methods.GetCount()
        idx = wx.NOT_FOUND
        while i < count:
            val = self.methods.GetClientData(i)
            if val == self.conf.getMethod():
                idx = i
            i += 1
        self.methods.SetSelection(idx)
    
    def initLocation(self, loc):
        self.loc = copy.deepcopy(loc)
        deg, min, sec = libitl.decimal2Dms(self.loc.getLatitude())
        self.latitude_deg.SetLabel(str(deg))
        self.latitude_min.SetLabel(str(min))
        
        deg, min, sec = libitl.decimal2Dms(self.loc.getLongitude())
        self.longitude_deg.SetLabel(str(deg))
        self.longitude_min.SetLabel(str(min))
        
        self.ville.SetLabel(self.loc.getTownName())
        self.pays.SetLabel(self.loc.getCountryName())
        
        self.pressure.SetLabel(str(self.loc.getPressure()))
        self.temperature.SetLabel(str(self.loc.getTemperature()))
        
        self.dst.SetValue(self.loc.getDST() != 0)
        
        self.sea_level.SetValue(str(self.loc.getSeaLevel()))
        
    def initMethod(self, conf):
        self.conf = copy.deepcopy(conf)
    
    def getLocation(self):
        return self.loc
    
    def getMethod(self):
        return self.conf
