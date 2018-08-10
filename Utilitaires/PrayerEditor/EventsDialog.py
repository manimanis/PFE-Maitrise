#Boa:Dialog:EventsDialog

import wx
import wx.lib.masked.timectrl
import wx.lib.masked.textctrl

import Events
import EventEditDialog

def create(parent):
    return EventsDialog(parent)

[wxID_EVENTSDIALOG, wxID_EVENTSDIALOGBTNAJOUTER, 
 wxID_EVENTSDIALOGBTNDESCENDRE, wxID_EVENTSDIALOGBTNMODIFIER, 
 wxID_EVENTSDIALOGBTNMONTER, wxID_EVENTSDIALOGBTNQUITTER, 
 wxID_EVENTSDIALOGBTNSUPPRIMER, wxID_EVENTSDIALOGLSTEVENTS, 
 wxID_EVENTSDIALOGSTATICLINE1, wxID_EVENTSDIALOGSTATICLINE2, 
] = [wx.NewId() for _init_ctrls in range(10)]

class EventsDialog(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_EVENTSDIALOG, name='', parent=prnt,
              pos=wx.Point(677, 173), size=wx.Size(317, 489),
              style=wx.DEFAULT_DIALOG_STYLE,
              title=u'Edition des Ev\xe8nements')
        self.SetClientSize(wx.Size(309, 455))

        self.btnModifier = wx.Button(id=wxID_EVENTSDIALOGBTNMODIFIER,
              label=u'Modifier', name=u'btnModifier', parent=self,
              pos=wx.Point(8, 368), size=wx.Size(80, 23), style=0)
        self.btnModifier.Bind(wx.EVT_BUTTON, self.OnBtnModifierButton,
              id=wxID_EVENTSDIALOGBTNMODIFIER)

        self.btnQuitter = wx.Button(id=wxID_EVENTSDIALOGBTNQUITTER,
              label=u'Quitter...', name=u'btnQuitter', parent=self,
              pos=wx.Point(220, 424), size=wx.Size(80, 23), style=0)
        self.btnQuitter.Bind(wx.EVT_BUTTON, self.OnBtnQuitterButton,
              id=wxID_EVENTSDIALOGBTNQUITTER)

        self.staticLine1 = wx.StaticLine(id=wxID_EVENTSDIALOGSTATICLINE1,
              name='staticLine1', parent=self, pos=wx.Point(8, 336),
              size=wx.Size(292, 2), style=0)

        self.lstEvents = wx.ListBox(choices=[], id=wxID_EVENTSDIALOGLSTEVENTS,
              name=u'lstEvents', parent=self, pos=wx.Point(8, 8),
              size=wx.Size(292, 320), style=0)
        self.lstEvents.Bind(wx.EVT_LISTBOX, self.OnLstEventsListbox,
              id=wxID_EVENTSDIALOGLSTEVENTS)
        self.lstEvents.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnLstEventsListboxDclick, id=wxID_EVENTSDIALOGLSTEVENTS)

        self.btnAjouter = wx.Button(id=wxID_EVENTSDIALOGBTNAJOUTER,
              label=u'Ajouter', name=u'btnAjouter', parent=self, pos=wx.Point(8,
              344), size=wx.Size(80, 23), style=0)
        self.btnAjouter.Bind(wx.EVT_BUTTON, self.OnBtnAjouterButton,
              id=wxID_EVENTSDIALOGBTNAJOUTER)

        self.btnSupprimer = wx.Button(id=wxID_EVENTSDIALOGBTNSUPPRIMER,
              label=u'Supprimer', name=u'btnSupprimer', parent=self,
              pos=wx.Point(8, 392), size=wx.Size(80, 23), style=0)
        self.btnSupprimer.Bind(wx.EVT_BUTTON, self.OnBtnSupprimerButton,
              id=wxID_EVENTSDIALOGBTNSUPPRIMER)

        self.staticLine2 = wx.StaticLine(id=wxID_EVENTSDIALOGSTATICLINE2,
              name='staticLine2', parent=self, pos=wx.Point(96, 346),
              size=wx.Size(2, 66), style=wx.LI_VERTICAL)

        self.btnMonter = wx.Button(id=wxID_EVENTSDIALOGBTNMONTER,
              label=u'Monter', name=u'btnMonter', parent=self, pos=wx.Point(104,
              344), size=wx.Size(80, 23), style=0)
        self.btnMonter.Bind(wx.EVT_BUTTON, self.OnBtnMonterButton,
              id=wxID_EVENTSDIALOGBTNMONTER)

        self.btnDescendre = wx.Button(id=wxID_EVENTSDIALOGBTNDESCENDRE,
              label=u'Descendre', name=u'btnDescendre', parent=self,
              pos=wx.Point(104, 368), size=wx.Size(80, 23), style=0)
        self.btnDescendre.Bind(wx.EVT_BUTTON, self.OnBtnDescendreButton,
              id=wxID_EVENTSDIALOGBTNDESCENDRE)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.CenterOnParent()
        self.events = Events.EventsCollection()
        self.events.load()
        
        self.initUIFromData()
        self.updateButtons()

    def initUIFromData(self):
        self.lstEvents.Clear()
        for i in range(0, self.events.getCount()):
            data = self.events.getData(i)
            self.lstEvents.Append(data.getMessage())
        
    def updateButtons(self):
        self.btnAjouter.Enable(self.events.getCount() < 64)
        self.btnSupprimer.Enable(self.lstEvents.GetSelection() != -1)
        self.btnModifier.Enable(self.lstEvents.GetSelection() != -1)
        self.btnMonter.Enable(self.lstEvents.GetSelection() > 0)
        self.btnDescendre.Enable(self.lstEvents.GetSelection() != -1 and self.lstEvents.GetSelection() < self.lstEvents.GetCount() - 1)
        
    def permuteEvents(self, i, j):
        v1 = self.events.getData(i)
        v2 = self.events.getData(j)
        
        s1 = self.lstEvents.GetString(i)
        s2 = self.lstEvents.GetString(j)
        
        self.events.setData(v2, i)
        self.events.setData(v1, j)
        
        self.lstEvents.SetString(i, s2)
        self.lstEvents.SetString(j, s1)
    
    def OnBtnQuitterButton(self, event):
        if self.events.hasChanged():
            rep = wx.MessageBox("Enregidtrer ces \xe8v\xe9nements ?",
                        "\xe8v\xe9nements", wx.YES_NO | wx.CANCEL | wx.YES_DEFAULT, self)
            if (rep == wx.YES):
                self.events.save()
            elif (rep == wx.CANCEL):
                return
        self.EndModal(wx.ID_CANCEL)

    def OnBtnModifierButton(self, event):
        if self.lstEvents.GetSelection() == -1: return
        
        idx = self.lstEvents.GetSelection()
        ev = self.events.getData(idx)
        
        dlg = EventEditDialog.create(self)
        dlg.setEvent(ev)
        if dlg.ShowModal() == wx.ID_OK:
            if ev != dlg.getEvent():
                ev = dlg.getEvent()
                self.events.setData(ev, idx)
                self.lstEvents.SetString(idx, ev.getMessage())
        
        self.updateButtons()

    def OnBtnAjouterButton(self, event):
        ev = Events.Event()
        
        dlg = EventEditDialog.create(self)
        dlg.setEvent(ev)
        if dlg.ShowModal() == wx.ID_OK:
            ev = dlg.getEvent()
            ev.setIndex(self.events.getCount() + 1)
            
            self.events.appendItem(ev)
            idx = self.lstEvents.Append(ev.getMessage())
            
            self.lstEvents.SetSelection(idx)
        
        self.updateButtons()
            

    def OnBtnSupprimerButton(self, event):
        if self.lstEvents.GetSelection() == -1: return
        idx = self.lstEvents.GetSelection()
        
        rep = wx.MessageBox("Supprimer cet \xe8v\xe9nement ?",
                "\xe8v\xe9nement", wx.YES_NO | wx.YES_DEFAULT, self)
        if (rep == wx.YES):
            self.events.removeAt(idx)
            self.lstEvents.Delete(idx)
        
        self.updateButtons()

    def OnLstEventsListbox(self, event):
        self.updateButtons()

    def OnLstEventsListboxDclick(self, event):
        self.OnBtnModifierButton(None)

    def OnBtnDescendreButton(self, event):
        if self.lstEvents.GetSelection() == -1: return
        idx = self.lstEvents.GetSelection()
        
        self.permuteEvents(idx, idx + 1)
        self.lstEvents.SetSelection(idx + 1)
        self.updateButtons()

    def OnBtnMonterButton(self, event):
        if self.lstEvents.GetSelection() == -1: return
        idx = self.lstEvents.GetSelection()
        
        self.permuteEvents(idx, idx - 1)
        self.lstEvents.SetSelection(idx - 1)
        self.updateButtons()
