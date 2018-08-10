#Boa:Dialog:PrayersTimesDialog

import wx
import wx.lib.masked.textctrl
import Prayers
from Events import *
import libitl
import PrayersEditDialog

def create(parent):
    return PrayersTimesDialog(parent)

[wxID_PRAYERSTIMESDIALOG, wxID_PRAYERSTIMESDIALOGBTNGENERER, 
 wxID_PRAYERSTIMESDIALOGBTNQUITTER, wxID_PRAYERSTIMESDIALOGEDTGMT, 
 wxID_PRAYERSTIMESDIALOGEDTLATITUDE, wxID_PRAYERSTIMESDIALOGEDTLONGITUDE, 
 wxID_PRAYERSTIMESDIALOGEDTMETHOD, wxID_PRAYERSTIMESDIALOGEDTPAYS, 
 wxID_PRAYERSTIMESDIALOGEDTREGION, wxID_PRAYERSTIMESDIALOGEDTVILLE, 
 wxID_PRAYERSTIMESDIALOGLSTPRAYERS, wxID_PRAYERSTIMESDIALOGSTATICLINE1, 
 wxID_PRAYERSTIMESDIALOGSTATICLINE2, wxID_PRAYERSTIMESDIALOGSTATICTEXT1, 
 wxID_PRAYERSTIMESDIALOGSTATICTEXT2, wxID_PRAYERSTIMESDIALOGSTATICTEXT3, 
 wxID_PRAYERSTIMESDIALOGSTATICTEXT4, wxID_PRAYERSTIMESDIALOGSTATICTEXT5, 
 wxID_PRAYERSTIMESDIALOGSTATICTEXT6, wxID_PRAYERSTIMESDIALOGSTATICTEXT8, 
] = [wx.NewId() for _init_ctrls in range(20)]

class PrayersTimesDialog(wx.Dialog):
    def _init_coll_lstPrayers_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading=u'Journ\xe9e', width=-1)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading=u'Fajr',
              width=-1)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT,
              heading=u'Shuruq', width=-1)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT, heading=u'Thuhr',
              width=-1)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT, heading=u'Asr',
              width=-1)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_LEFT,
              heading=u'Maghreb', width=-1)
        parent.InsertColumn(col=6, format=wx.LIST_FORMAT_LEFT, heading=u'Ishaa',
              width=-1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_PRAYERSTIMESDIALOG,
              name=u'PrayersTimesDialog', parent=prnt, pos=wx.Point(507, 230),
              size=wx.Size(692, 505), style=wx.DEFAULT_DIALOG_STYLE,
              title=u'Heures de pri\xe8res')
        self.SetClientSize(wx.Size(684, 471))

        self.btnQuitter = wx.Button(id=wxID_PRAYERSTIMESDIALOGBTNQUITTER,
              label=u'Quitter...', name=u'btnQuitter', parent=self,
              pos=wx.Point(596, 432), size=wx.Size(75, 23), style=0)
        self.btnQuitter.Bind(wx.EVT_BUTTON, self.OnBtnQuitterButton,
              id=wxID_PRAYERSTIMESDIALOGBTNQUITTER)

        self.staticLine1 = wx.StaticLine(id=wxID_PRAYERSTIMESDIALOGSTATICLINE1,
              name='staticLine1', parent=self, pos=wx.Point(8, 424),
              size=wx.Size(668, 2), style=0)
        self.staticLine1.SetMaxSize(wx.Size(1, 2))
        self.staticLine1.SetMinSize(wx.Size(1, 2))

        self.staticLine2 = wx.StaticLine(id=wxID_PRAYERSTIMESDIALOGSTATICLINE2,
              name='staticLine2', parent=self, pos=wx.Point(8, 70),
              size=wx.Size(668, 2), style=0)
        self.staticLine2.SetMaxSize(wx.Size(1, 2))
        self.staticLine2.SetMinSize(wx.Size(1, 2))

        self.staticText1 = wx.StaticText(id=wxID_PRAYERSTIMESDIALOGSTATICTEXT1,
              label=u'Pays', name='staticText1', parent=self, pos=wx.Point(8,
              8), size=wx.Size(56, 13),
              style=wx.ALIGN_RIGHT | wx.ST_NO_AUTORESIZE)
        self.staticText1.SetForegroundColour(wx.Colour(64, 0, 128))
        self.staticText1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'MS Shell Dlg 2'))

        self.staticText2 = wx.StaticText(id=wxID_PRAYERSTIMESDIALOGSTATICTEXT2,
              label=u'Ville', name='staticText2', parent=self, pos=wx.Point(456,
              8), size=wx.Size(56, 16),
              style=wx.ALIGN_RIGHT | wx.ST_NO_AUTORESIZE)
        self.staticText2.SetForegroundColour(wx.Colour(64, 0, 128))
        self.staticText2.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'MS Shell Dlg 2'))

        self.staticText3 = wx.StaticText(id=wxID_PRAYERSTIMESDIALOGSTATICTEXT3,
              label=u'R\xe9gion', name='staticText3', parent=self,
              pos=wx.Point(232, 8), size=wx.Size(56, 13),
              style=wx.ALIGN_RIGHT | wx.ST_NO_AUTORESIZE)
        self.staticText3.SetForegroundColour(wx.Colour(64, 0, 128))
        self.staticText3.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'MS Shell Dlg 2'))

        self.staticText4 = wx.StaticText(id=wxID_PRAYERSTIMESDIALOGSTATICTEXT4,
              label=u'Longitude', name='staticText4', parent=self,
              pos=wx.Point(8, 28), size=wx.Size(56, 13),
              style=wx.ALIGN_RIGHT | wx.ST_NO_AUTORESIZE)
        self.staticText4.SetForegroundColour(wx.Colour(64, 0, 128))
        self.staticText4.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'MS Shell Dlg 2'))

        self.staticText5 = wx.StaticText(id=wxID_PRAYERSTIMESDIALOGSTATICTEXT5,
              label=u'Latitude', name='staticText5', parent=self,
              pos=wx.Point(232, 28), size=wx.Size(56, 13),
              style=wx.ALIGN_RIGHT | wx.ST_NO_AUTORESIZE)
        self.staticText5.SetForegroundColour(wx.Colour(64, 0, 128))
        self.staticText5.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'MS Shell Dlg 2'))

        self.staticText6 = wx.StaticText(id=wxID_PRAYERSTIMESDIALOGSTATICTEXT6,
              label=u'GMT', name='staticText6', parent=self, pos=wx.Point(8,
              48), size=wx.Size(56, 13),
              style=wx.ALIGN_RIGHT | wx.ST_NO_AUTORESIZE)
        self.staticText6.SetForegroundColour(wx.Colour(64, 0, 128))
        self.staticText6.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'MS Shell Dlg 2'))

        self.staticText8 = wx.StaticText(id=wxID_PRAYERSTIMESDIALOGSTATICTEXT8,
              label=u'M\xe9thode', name='staticText8', parent=self,
              pos=wx.Point(232, 48), size=wx.Size(56, 13),
              style=wx.ALIGN_RIGHT | wx.ST_NO_AUTORESIZE)
        self.staticText8.SetForegroundColour(wx.Colour(64, 0, 128))
        self.staticText8.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'MS Shell Dlg 2'))

        self.edtRegion = wx.StaticText(id=wxID_PRAYERSTIMESDIALOGEDTREGION,
              label=u'', name=u'edtRegion', parent=self, pos=wx.Point(296, 8),
              size=wx.Size(150, 13), style=wx.ST_NO_AUTORESIZE)

        self.edtVille = wx.StaticText(id=wxID_PRAYERSTIMESDIALOGEDTVILLE,
              label=u'', name=u'edtVille', parent=self, pos=wx.Point(520, 8),
              size=wx.Size(150, 13), style=wx.ST_NO_AUTORESIZE)

        self.edtGMT = wx.StaticText(id=wxID_PRAYERSTIMESDIALOGEDTGMT, label=u'',
              name=u'edtGMT', parent=self, pos=wx.Point(72, 48),
              size=wx.Size(150, 13), style=wx.ST_NO_AUTORESIZE)

        self.edtLatitude = wx.StaticText(id=wxID_PRAYERSTIMESDIALOGEDTLATITUDE,
              label=u'', name=u'edtLatitude', parent=self, pos=wx.Point(296,
              28), size=wx.Size(150, 13), style=wx.ST_NO_AUTORESIZE)

        self.edtPays = wx.StaticText(id=wxID_PRAYERSTIMESDIALOGEDTPAYS,
              label=u'', name=u'edtPays', parent=self, pos=wx.Point(72, 8),
              size=wx.Size(150, 13), style=wx.ST_NO_AUTORESIZE)

        self.edtMethod = wx.StaticText(id=wxID_PRAYERSTIMESDIALOGEDTMETHOD,
              label=u'', name=u'edtMethod', parent=self, pos=wx.Point(296, 48),
              size=wx.Size(150, 13), style=wx.ST_NO_AUTORESIZE)

        self.edtLongitude = wx.StaticText(id=wxID_PRAYERSTIMESDIALOGEDTLONGITUDE,
              label=u'', name=u'edtLongitude', parent=self, pos=wx.Point(72,
              28), size=wx.Size(150, 13), style=wx.ST_NO_AUTORESIZE)

        self.lstPrayers = wx.ListCtrl(id=wxID_PRAYERSTIMESDIALOGLSTPRAYERS,
              name=u'lstPrayers', parent=self, pos=wx.Point(12, 80),
              size=wx.Size(660, 332),
              style=wx.LC_EDIT_LABELS | wx.LC_SINGLE_SEL | wx.LC_REPORT)
        self._init_coll_lstPrayers_Columns(self.lstPrayers)
        self.lstPrayers.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnLstPrayersListItemSelected,
              id=wxID_PRAYERSTIMESDIALOGLSTPRAYERS)
        self.lstPrayers.Bind(wx.EVT_LEFT_DCLICK, self.OnLstPrayersLeftDclick)

        self.btnGenerer = wx.Button(id=wxID_PRAYERSTIMESDIALOGBTNGENERER,
              label=u'R\xe9g\xe9n\xe9rer...', name=u'btnGenerer', parent=self,
              pos=wx.Point(12, 432), size=wx.Size(90, 23), style=0)
        self.btnGenerer.Bind(wx.EVT_BUTTON, self.OnBtnGenererButton,
              id=wxID_PRAYERSTIMESDIALOGBTNGENERER)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.CenterOnParent()
        
        self.cur_sel = -1

    def setVille(self, ville):
        self.ville = ville
        
    def setFilename(self, filename):
        self.filename = filename
        
    def loadData(self):
        self.prayers = Prayers.YearPrayersTimes(self.ville)
        self.initUIFromData()
        
    def initPrayersList(self):
        self.lstPrayers.DeleteAllItems()
        for i in range(0, self.prayers.getCount()):
            self.prayers.moveTo(i)
            data = self.prayers.getData()
            
            self.lstPrayers.InsertStringItem(i, data.getDay())
            self.lstPrayers.SetStringItem(i, 1, str(data.getFajr()))
            self.lstPrayers.SetStringItem(i, 2, str(data.getShuruq()))
            self.lstPrayers.SetStringItem(i, 3, str(data.getDhohr()))
            self.lstPrayers.SetStringItem(i, 4, str(data.getAsr()))
            self.lstPrayers.SetStringItem(i, 5, str(data.getMaghreb()))
            self.lstPrayers.SetStringItem(i, 6, str(data.getIshaa()))         
    
    def updatePrayersList(self, idx):
        data = self.prayers.getData(idx)
        
        self.lstPrayers.SetStringItem(idx, 0, data.getDay())
        self.lstPrayers.SetStringItem(idx, 1, str(data.getFajr()))
        self.lstPrayers.SetStringItem(idx, 2, str(data.getShuruq()))
        self.lstPrayers.SetStringItem(idx, 3, str(data.getDhohr()))
        self.lstPrayers.SetStringItem(idx, 4, str(data.getAsr()))
        self.lstPrayers.SetStringItem(idx, 5, str(data.getMaghreb()))
        self.lstPrayers.SetStringItem(idx, 6, str(data.getIshaa()))
                
    def initUIFromData(self):
        self.edtPays.SetLabel(self.ville.getCountry())
        self.edtRegion.SetLabel(self.ville.getRegion())
        self.edtVille.SetLabel(self.ville.getVille())
        self.edtLongitude.SetLabel(str(self.ville.getLongitude()))
        self.edtLatitude.SetLabel(str(self.ville.getLatitude()))
        self.edtGMT.SetLabel(str(self.ville.getGMT()) + " " + ("NODST", "DST")[self.ville.getDST()])
        self.edtMethod.SetLabel(libitl.methods[self.ville.getMethod()])
                
        self.initPrayersList()

    def OnBtnQuitterButton(self, event):
        if self.prayers.hasChanged():
            rep = wx.MessageBox("Enregistrer les modifications avant de quitter",
                "Heures de priere", wx.YES_NO | wx.CANCEL | wx.YES_DEFAULT, self)
            if (rep == wx.YES):
                self.prayers.save()
                self.EndModal(wx.OK)
            elif (rep == wx.NO):
                self.EndModal(wx.OK)
        else:
            self.EndModal(wx.OK)

    def OnBtnGenererButton(self, event):
        rep = wx.MessageBox("Les donn\xe9es vont \xeatre \xe9cras\xe9s. Continuer ?",
                "Heures de pri\xe9res", wx.YES_NO | wx.NO_DEFAULT, self)
        if rep == wx.YES:
            self.prayers.generate()
            self.prayers.save()
            self.initPrayersList()

    def OnEdtJourChar(self, event):
        if event.GetKeyCode() == wx.WXK_RETURN:
            pos = self.prayers.searchByDay(self.edtJour.GetLabel())
            if pos != -1:
                self.initDataFromUI()
                self.prayers.moveTo(pos)
            self.initUIFromData()
        else:
            event.Skip()
            
    def editPrayersTimes(self, idx):
        dlg = PrayersEditDialog.create(self)
        dlg.setPrayersTimes(self.prayers.getData(idx))
        dlg.initUIFromData()

        if dlg.ShowModal() == wx.ID_OK:
            if self.prayers.getData() != dlg.getPrayersTimes():
                self.prayers.setData(dlg.getPrayersTimes(), idx)
                
                self.updatePrayersList(idx)

    def OnLstPrayersListItemSelected(self, event):
        self.cur_sel = event.m_itemIndex

    def OnLstPrayersLeftDclick(self, event):
        if self.cur_sel != -1:
            self.editPrayersTimes(self.cur_sel)
