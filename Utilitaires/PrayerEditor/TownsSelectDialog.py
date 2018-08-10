#Boa:Dialog:TownsSelectDialog

import wx
from Villes import *
import VilleEditDialog

UPDATE_COUNTRY_LIST = 1
UPDATE_REGIONS_LIST = 2
UPDATE_VILLES_LIST  = 4
UPDATE_ALL_LISTS    = 7

def create(parent):
    return TownsSelectDialog(parent)

[wxID_TOWNSSELECTDIALOG, wxID_TOWNSSELECTDIALOGBTNAJOUTER, 
 wxID_TOWNSSELECTDIALOGBTNDESCENDRE, wxID_TOWNSSELECTDIALOGBTNENREGISTRER, 
 wxID_TOWNSSELECTDIALOGBTNMONTER, wxID_TOWNSSELECTDIALOGBTNQUITTER, 
 wxID_TOWNSSELECTDIALOGBTNSUPPRIMER, wxID_TOWNSSELECTDIALOGEDTCOUNTRY, 
 wxID_TOWNSSELECTDIALOGEDTINFO, wxID_TOWNSSELECTDIALOGEDTREGION, 
 wxID_TOWNSSELECTDIALOGEDTVILLE, wxID_TOWNSSELECTDIALOGLSTCOUNTRIES, 
 wxID_TOWNSSELECTDIALOGLSTFINALE, wxID_TOWNSSELECTDIALOGLSTREGIONS, 
 wxID_TOWNSSELECTDIALOGLSTVILLES, wxID_TOWNSSELECTDIALOGSTATICLINE1, 
 wxID_TOWNSSELECTDIALOGSTATICTEXT1, wxID_TOWNSSELECTDIALOGSTATICTEXT2, 
 wxID_TOWNSSELECTDIALOGSTATICTEXT3, wxID_TOWNSSELECTDIALOGSTATICTEXT4, 
] = [wx.NewId() for _init_ctrls in range(20)]

class TownsSelectDialog(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_TOWNSSELECTDIALOG,
              name=u'TownsSelectDialog', parent=prnt, pos=wx.Point(323, 196),
              size=wx.Size(682, 437), style=wx.DEFAULT_DIALOG_STYLE,
              title=u'S\xe9lection des Villes')
        self.SetClientSize(wx.Size(674, 403))

        self.lstCountries = wx.ListBox(choices=[],
              id=wxID_TOWNSSELECTDIALOGLSTCOUNTRIES, name=u'lstCountries',
              parent=self, pos=wx.Point(8, 56), size=wx.Size(112, 320),
              style=0)
        self.lstCountries.Bind(wx.EVT_LISTBOX, self.OnLstCountriesListbox,
              id=wxID_TOWNSSELECTDIALOGLSTCOUNTRIES)

        self.edtCountry = wx.TextCtrl(id=wxID_TOWNSSELECTDIALOGEDTCOUNTRY,
              name=u'edtCountry', parent=self, pos=wx.Point(8, 32),
              size=wx.Size(112, 21), style=0, value=u'')
        self.edtCountry.Bind(wx.EVT_TEXT, self.OnEdtCountryText,
              id=wxID_TOWNSSELECTDIALOGEDTCOUNTRY)

        self.edtVille = wx.TextCtrl(id=wxID_TOWNSSELECTDIALOGEDTVILLE,
              name=u'edtVille', parent=self, pos=wx.Point(248, 32),
              size=wx.Size(112, 21), style=0, value=u'')
        self.edtVille.Bind(wx.EVT_TEXT, self.OnEdtVilleText,
              id=wxID_TOWNSSELECTDIALOGEDTVILLE)

        self.lstVilles = wx.ListBox(choices=[],
              id=wxID_TOWNSSELECTDIALOGLSTVILLES, name=u'lstVilles',
              parent=self, pos=wx.Point(248, 56), size=wx.Size(112, 320),
              style=0)
        self.lstVilles.Bind(wx.EVT_LISTBOX, self.OnLstVillesListbox,
              id=wxID_TOWNSSELECTDIALOGLSTVILLES)

        self.staticText1 = wx.StaticText(id=wxID_TOWNSSELECTDIALOGSTATICTEXT1,
              label=u'Pays', name='staticText1', parent=self, pos=wx.Point(8,
              8), size=wx.Size(23, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_TOWNSSELECTDIALOGSTATICTEXT2,
              label=u'Ville', name='staticText2', parent=self, pos=wx.Point(248,
              8), size=wx.Size(19, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_TOWNSSELECTDIALOGSTATICTEXT3,
              label=u'R\xe9gion', name='staticText3', parent=self,
              pos=wx.Point(128, 8), size=wx.Size(33, 13), style=0)

        self.edtRegion = wx.TextCtrl(id=wxID_TOWNSSELECTDIALOGEDTREGION,
              name=u'edtRegion', parent=self, pos=wx.Point(128, 32),
              size=wx.Size(112, 21), style=0, value=u'')
        self.edtRegion.Bind(wx.EVT_TEXT, self.OnEdtRegionText,
              id=wxID_TOWNSSELECTDIALOGEDTREGION)

        self.lstRegions = wx.ListBox(choices=[],
              id=wxID_TOWNSSELECTDIALOGLSTREGIONS, name=u'lstRegions',
              parent=self, pos=wx.Point(128, 56), size=wx.Size(112, 320),
              style=0)
        self.lstRegions.Bind(wx.EVT_LISTBOX, self.OnLstRegionsListbox,
              id=wxID_TOWNSSELECTDIALOGLSTREGIONS)

        self.lstFinale = wx.ListBox(choices=[],
              id=wxID_TOWNSSELECTDIALOGLSTFINALE, name=u'lstFinale',
              parent=self, pos=wx.Point(368, 104), size=wx.Size(296, 192),
              style=0)
        self.lstFinale.Bind(wx.EVT_LISTBOX, self.OnLstFinaleListbox,
              id=wxID_TOWNSSELECTDIALOGLSTFINALE)

        self.btnSupprimer = wx.Button(id=wxID_TOWNSSELECTDIALOGBTNSUPPRIMER,
              label=u'Supprimer', name=u'btnSupprimer', parent=self,
              pos=wx.Point(440, 56), size=wx.Size(72, 24), style=0)
        self.btnSupprimer.Bind(wx.EVT_BUTTON, self.OnBtnSupprimerButton,
              id=wxID_TOWNSSELECTDIALOGBTNSUPPRIMER)

        self.btnAjouter = wx.Button(id=wxID_TOWNSSELECTDIALOGBTNAJOUTER,
              label=u'Ajouter', name=u'btnAjouter', parent=self,
              pos=wx.Point(368, 56), size=wx.Size(72, 24), style=0)
        self.btnAjouter.Bind(wx.EVT_BUTTON, self.OnBtnAjouterButton,
              id=wxID_TOWNSSELECTDIALOGBTNAJOUTER)

        self.staticText4 = wx.StaticText(id=wxID_TOWNSSELECTDIALOGSTATICTEXT4,
              label=u'Liste des villes retenues', name='staticText4',
              parent=self, pos=wx.Point(368, 88), size=wx.Size(114, 13),
              style=0)

        self.edtInfo = wx.StaticText(id=wxID_TOWNSSELECTDIALOGEDTINFO,
              label=u'', name=u'edtInfo', parent=self, pos=wx.Point(368, 8),
              size=wx.Size(296, 40), style=wx.ST_NO_AUTORESIZE)

        self.btnEnregistrer = wx.Button(id=wxID_TOWNSSELECTDIALOGBTNENREGISTRER,
              label=u'Enregistrer', name=u'btnEnregistrer', parent=self,
              pos=wx.Point(368, 352), size=wx.Size(80, 23), style=0)
        self.btnEnregistrer.Bind(wx.EVT_BUTTON, self.OnBtnEnregistrerButton,
              id=wxID_TOWNSSELECTDIALOGBTNENREGISTRER)

        self.btnMonter = wx.Button(id=wxID_TOWNSSELECTDIALOGBTNMONTER,
              label=u'Monter', name=u'btnMonter', parent=self, pos=wx.Point(368,
              304), size=wx.Size(72, 23), style=0)
        self.btnMonter.Bind(wx.EVT_BUTTON, self.OnBtnMonterButton,
              id=wxID_TOWNSSELECTDIALOGBTNMONTER)

        self.btnDescendre = wx.Button(id=wxID_TOWNSSELECTDIALOGBTNDESCENDRE,
              label=u'Descendre', name=u'btnDescendre', parent=self,
              pos=wx.Point(440, 304), size=wx.Size(72, 23), style=0)
        self.btnDescendre.Bind(wx.EVT_BUTTON, self.OnBtnDescendreButton,
              id=wxID_TOWNSSELECTDIALOGBTNDESCENDRE)

        self.staticLine1 = wx.StaticLine(id=wxID_TOWNSSELECTDIALOGSTATICLINE1,
              name='staticLine1', parent=self, pos=wx.Point(368, 346),
              size=wx.Size(296, 2), style=0)

        self.btnQuitter = wx.Button(id=wxID_TOWNSSELECTDIALOGBTNQUITTER,
              label=u'Quitter', name=u'btnQuitter', parent=self,
              pos=wx.Point(584, 352), size=wx.Size(80, 23), style=0)
        self.btnQuitter.Bind(wx.EVT_BUTTON, self.OnBtnQuitterButton,
              id=wxID_TOWNSSELECTDIALOGBTNQUITTER)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.CenterOnParent()
        
        self.villes = VillesUtility()
        self.country_names = self.villes.getCountryList()
        self.regions_names = []
        self.villes_names = []
        self.updateLists()
        
        self.criteria = []
        self.seltown = []
        self.updateButtons()
        
        self.curville = Ville()
        self.updateInfo()
        
        self.loadData()
        
    def updateLists(self, l = UPDATE_ALL_LISTS):
        if (l & UPDATE_COUNTRY_LIST) != 0:
            self.lstCountries.Clear()
            for value in self.country_names:
                self.lstCountries.Append(value)
        
        if (l & UPDATE_REGIONS_LIST) != 0:
            self.lstRegions.Clear()
            for value in self.regions_names:
                self.lstRegions.Append(value)
        
        if (l & UPDATE_VILLES_LIST) != 0:
            self.lstVilles.Clear()    
            for value in self.villes_names:
                self.lstVilles.Append(value)
    
    def updateButtons(self):
        self.btnAjouter.Enable((len(self.criteria) == 3) and (self.lstFinale.GetCount() != 13))
        self.btnSupprimer.Enable(self.lstFinale.GetSelection() != -1)
        self.btnMonter.Enable(self.lstFinale.GetSelection() > 0)
        self.btnDescendre.Enable((self.lstFinale.GetSelection() >= 0) and (self.lstFinale.GetSelection() < self.lstFinale.GetCount() - 1))
        
    def updateInfo(self):
        if (len(self.seltown) != 3):
            self.edtInfo.SetLabel('S\xe9lectionner une ville')
            return
                
        ville = self.villes.searchVille(self.seltown[0], self.seltown[1], self.seltown[2])
        self.curville = ville
        self.edtInfo.SetLabel("Ville : %s - %s - %s\r\n" \
                    "Longitude : %s - Latitude : %s\n\r" \
                    "GMT : %1.1f - DST : %s" % (ville.getCountry(), ville.getRegion(), ville.getVille(), 
                    str(ville.getLongitude()), str(ville.getLatitude()), 
                    ville.getGMT(), ("Non","Oui")[ville.getDST()]))
        
    def loadData(self):
        self.svc = SelectedVillesCollection()
        self.lstFinale.Clear()
        for i in range(0, self.svc.getCount()):
            self.svc.moveTo(i)
            ville = self.svc.getData()
            pos = self.lstFinale.Append("%s - %s - %s" % (ville.getCountry(), ville.getRegion(), ville.getVille()))
            self.lstFinale.SetClientData(pos, [ville.getCountry(), ville.getRegion(), ville.getVille()])
    
    def saveData(self):
        self.svc.removeAll()
        for i in range(0, self.lstFinale.GetCount()):
            arr = self.lstFinale.GetClientData(i)
            ville = self.villes.searchVille(arr[0], arr[1], arr[2])
            self.svc.appendItem(ville)
        self.svc.save()
            
    def permuterVilles(self, i, j):
        vam = self.lstFinale.GetString(i)
        vs = self.lstFinale.GetString(j)
        
        self.lstFinale.SetString(i, vs)
        self.lstFinale.SetString(j, vam)
        
        vam = self.lstFinale.GetClientData(i)
        vs = self.lstFinale.GetClientData(j)
        
        self.lstFinale.SetClientData(i, vs)
        self.lstFinale.SetClientData(j, vam)

    def OnEdtCountryText(self, event):
        self.edtRegion.SetLabel('')
        self.edtVille.SetLabel('')
        
        self.country_names = self.villes.getCountryList(self.edtCountry.GetLabel())
        self.regions_names = []
        self.villes_names = []
        
        self.updateLists()
        self.updateButtons()
    
    def OnEdtRegionText(self, event):
        self.edtVille.SetLabel('')
        
        self.regions_names = self.villes.getRegionsList(self.edtCountry.GetLabel(), self.edtRegion.GetLabel())
        self.villes_names = []
        
        self.updateLists(UPDATE_REGIONS_LIST | UPDATE_VILLES_LIST)
        self.updateButtons()    
    
    def OnEdtVilleText(self, event):
        self.villes_names = self.villes.getVillesList(self.edtCountry.GetLabel(), self.edtRegion.GetLabel(), self.edtVille.GetLabel())
        self.updateLists(UPDATE_VILLES_LIST)

    def OnLstCountriesListbox(self, event):
        self.edtCountry.SetLabel(event.GetString())
        self.edtRegion.SetLabel('')
        
        self.regions_names = self.villes.getRegionsList(event.GetString(), self.edtRegion.GetLabel())
        self.villes_names = []
        
        self.criteria = [self.edtCountry.GetLabel()]
        self.updateLists(UPDATE_REGIONS_LIST | UPDATE_VILLES_LIST)
        self.updateButtons()
        
    def OnLstRegionsListbox(self, event):
        self.edtRegion.SetLabel(event.GetString())
        self.edtVille.SetLabel('')
        
        self.villes_names = self.villes.getVillesList(self.edtCountry.GetLabel(), self.edtRegion.GetLabel(), '')
        
        self.criteria = [self.edtCountry.GetLabel(), self.edtRegion.GetLabel()]
        
        self.updateLists(UPDATE_VILLES_LIST)
        self.updateButtons()

    def OnLstVillesListbox(self, event):
        self.edtVille.SetLabel(event.GetString())
        
        self.criteria = [self.edtCountry.GetLabel(), self.edtRegion.GetLabel(), self.edtVille.GetLabel()]
        self.seltown = self.criteria
        
        self.updateButtons()
        self.updateInfo()

    def OnLstFinaleListbox(self, event):
        if self.lstFinale.GetSelection() == -1: return
        self.seltown = self.lstFinale.GetClientData(self.lstFinale.GetSelection())
        self.updateButtons()
        self.updateInfo()

    def OnBtnAjouterButton(self, event):
        pos = self.lstFinale.Append("%s - %s - %s" % (self.criteria[0], self.criteria[1], self.criteria[2]))
        self.lstFinale.SetClientData(pos, self.criteria)
        self.svc.appendItem(self.curville)
        self.updateButtons()
        
    def OnBtnSupprimerButton(self, event):
        if self.lstFinale.GetSelection() != -1:
            self.lstFinale.Delete(self.lstFinale.GetSelection())
        
        self.updateButtons()    

    def OnBtnEnregistrerButton(self, event):
        self.saveData()

    def OnBtnMonterButton(self, event):
        sel = self.lstFinale.GetSelection()
        if sel <= 0: return
        
        self.permuterVilles(sel, sel - 1)
        
        self.lstFinale.SetSelection(sel - 1)
        
        self.updateButtons()
    
    def OnBtnDescendreButton(self, event):
        sel = self.lstFinale.GetSelection()
        if sel < 0 or sel >= self.lstFinale.GetCount(): return
        
        self.permuterVilles(sel, sel + 1)
        
        self.lstFinale.SetSelection(sel + 1)
        
        self.updateButtons()

    def OnBtnQuitterButton(self, event):
        rep = wx.MessageBox("Enregistrer les modifications avant de quitter",
                "Gestion des horaires de priere", wx.YES_NO | wx.CANCEL | wx.YES_DEFAULT, self)
        if (rep == wx.YES):
            self.saveData()
            self.EndModal(wx.ID_OK)
        elif (rep == wx.NO):
            self.EndModal(wx.ID_OK)
        
        
