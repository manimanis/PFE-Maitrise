#Boa:Dialog:VillesDialog

import wx
import wx.lib.masked.textctrl
import libitl
import thread
import datetime
import hexcodec
from Villes import *
import Prayers
import PrayersTimesDialog
import VilleEditDialog

def create(parent):
    return VillesDialog(parent)

[wxID_VILLESDIALOG, wxID_VILLESDIALOGBTNENREGISTRER, 
 wxID_VILLESDIALOGBTNMODIFIER, wxID_VILLESDIALOGBTNQUITTER, 
 wxID_VILLESDIALOGLSTVILLES, wxID_VILLESDIALOGSTATICLINE1, 
] = [wx.NewId() for _init_ctrls in range(6)]

class VillesDialog(wx.Dialog):
    def _init_coll_lstVilles_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading=u'Pays',
              width=90)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading=u'R\xe9gion', width=90)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading=u'Ville',
              width=120)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_RIGHT,
              heading=u'Longitude', width=-1)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_RIGHT,
              heading=u'Latitude', width=-1)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_RIGHT, heading=u'GMT',
              width=45)
        parent.InsertColumn(col=6, format=wx.LIST_FORMAT_LEFT, heading=u'DST',
              width=45)
        parent.InsertColumn(col=7, format=wx.LIST_FORMAT_LEFT,
              heading=u'M\xe9thode', width=100)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_VILLESDIALOG, name=u'VillesDialog',
              parent=prnt, pos=wx.Point(387, 306), size=wx.Size(680, 307),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'Emplacement des Villes')
        self.SetClientSize(wx.Size(672, 273))

        self.btnQuitter = wx.Button(id=wxID_VILLESDIALOGBTNQUITTER,
              label=u'Quitter...', name=u'btnQuitter', parent=self,
              pos=wx.Point(584, 240), size=wx.Size(80, 23), style=0)
        self.btnQuitter.Bind(wx.EVT_BUTTON, self.OnBtnQuitterButton,
              id=wxID_VILLESDIALOGBTNQUITTER)

        self.staticLine1 = wx.StaticLine(id=wxID_VILLESDIALOGSTATICLINE1,
              name='staticLine1', parent=self, pos=wx.Point(8, 232),
              size=wx.Size(656, 2), style=0)
        self.staticLine1.SetMaxSize(wx.Size(1, 2))
        self.staticLine1.SetMinSize(wx.Size(1, 2))

        self.lstVilles = wx.ListCtrl(id=wxID_VILLESDIALOGLSTVILLES,
              name=u'lstVilles', parent=self, pos=wx.Point(8, 8),
              size=wx.Size(656, 216), style=wx.LC_SINGLE_SEL | wx.LC_REPORT)
        self._init_coll_lstVilles_Columns(self.lstVilles)
        self.lstVilles.Bind(wx.EVT_LEFT_DCLICK, self.OnLstVillesLeftDclick)
        self.lstVilles.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnLstVillesListItemSelected, id=wxID_VILLESDIALOGLSTVILLES)
        self.lstVilles.Bind(wx.EVT_LIST_ITEM_DESELECTED,
              self.OnLstVillesListItemDeselected,
              id=wxID_VILLESDIALOGLSTVILLES)

        self.btnEnregistrer = wx.Button(id=wxID_VILLESDIALOGBTNENREGISTRER,
              label=u'Enregistrer', name=u'btnEnregistrer', parent=self,
              pos=wx.Point(496, 240), size=wx.Size(80, 23), style=0)
        self.btnEnregistrer.Bind(wx.EVT_BUTTON, self.OnBtnEnregistrerButton,
              id=wxID_VILLESDIALOGBTNENREGISTRER)

        self.btnModifier = wx.Button(id=wxID_VILLESDIALOGBTNMODIFIER,
              label=u'Modifier', name=u'btnModifier', parent=self,
              pos=wx.Point(8, 240), size=wx.Size(75, 23), style=0)
        self.btnModifier.Bind(wx.EVT_BUTTON, self.OnBtnModifierButton,
              id=wxID_VILLESDIALOGBTNMODIFIER)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.CenterOnParent()
        
        self.villes = SelectedVillesCollection()
        
        self.initUIFromData()
        self.updateButtons()
        
    def initUIFromData(self):
        for i in range(0, self.villes.getCount()):
            data = self.villes.getData(i)
            
            idx = self.lstVilles.InsertStringItem(i, data.getCountry())
            self.lstVilles.SetStringItem(i, 1, data.getRegion())
            self.lstVilles.SetStringItem(i, 2, data.getVille())
            self.lstVilles.SetStringItem(i, 3, str(data.getLongitude()))
            self.lstVilles.SetStringItem(i, 4, str(data.getLatitude()))
            self.lstVilles.SetStringItem(i, 5, "%1.1f" % (data.getGMT(),))
            self.lstVilles.SetStringItem(i, 6, ["Non", "Oui"][data.getDST()])
            self.lstVilles.SetStringItem(i, 7, libitl.methods[data.getMethod()])
        
        self.cur_sel = -1
        
    def updateButtons(self):
        self.btnModifier.Enable(self.cur_sel != -1)
    
    def updateListItem(self, idx):
        data = self.villes.getData(idx)
        
        self.lstVilles.SetStringItem(idx, 0, data.getCountry())
        self.lstVilles.SetStringItem(idx, 1, data.getRegion())
        self.lstVilles.SetStringItem(idx, 2, data.getVille())
        self.lstVilles.SetStringItem(idx, 3, str(data.getLongitude()))
        self.lstVilles.SetStringItem(idx, 4, str(data.getLatitude()))
        self.lstVilles.SetStringItem(idx, 5, "%1.1f" % (data.getGMT(),))
        self.lstVilles.SetStringItem(idx, 6, ["Non", "Oui"][data.getDST()])
        self.lstVilles.SetStringItem(idx, 7, libitl.methods[data.getMethod()])

    def OnBtnQuitterButton(self, event):
        if self.villes.hasChanged():
            rep = wx.MessageBox("Enregistrer les modifications avant de quitter",
                "Gestion des horaires de priere", wx.YES_NO | wx.CANCEL | wx.YES_DEFAULT, self)
            if (rep == wx.YES):
                self.villes.save()
                self.EndModal(wx.OK)
            elif (rep == wx.NO):
                self.EndModal(wx.OK)
        else:
            self.EndModal(wx.OK)

    def editVille(self, idx):
        dlg = VilleEditDialog.create(self)
        self.villes.moveTo(idx)
        dlg.setVille(self.villes.getData())
        dlg.initUIFromData()
        if dlg.ShowModal() == wx.ID_OK:
            if self.villes.getData() != dlg.getVille():
                self.villes.setData(dlg.getVille())
                self.updateListItem(idx)

    def OnLstVillesLeftDclick(self, event):
        if self.cur_sel != -1:
            self.editVille(self.cur_sel)

    def OnLstVillesListItemSelected(self, event):
        self.cur_sel = event.m_itemIndex
        self.updateButtons()
        
    def OnLstVillesListItemDeselected(self, event):
        self.cur_sel = -1
        self.updateButtons()

    def OnBtnEnregistrerButton(self, event):
        self.villes.save()

    def OnBtnModifierButton(self, event):
        self.editVille(self.cur_sel)

        
        
