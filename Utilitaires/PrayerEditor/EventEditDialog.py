#Boa:Dialog:EventEditDialog

import wx
import wx.lib.masked.timectrl
import wx.lib.masked.textctrl

import Events

def create(parent):
    return EventEditDialog(parent)

[wxID_EVENTEDITDIALOG, wxID_EVENTEDITDIALOGBTNCANCEL, 
 wxID_EVENTEDITDIALOGBTNVALIDER, wxID_EVENTEDITDIALOGCKCHQASR, 
 wxID_EVENTEDITDIALOGCKCHQCHOUROUK, wxID_EVENTEDITDIALOGCKCHQDHOHR, 
 wxID_EVENTEDITDIALOGCKCHQDIM, wxID_EVENTEDITDIALOGCKCHQFAJR, 
 wxID_EVENTEDITDIALOGCKCHQISHAA, wxID_EVENTEDITDIALOGCKCHQJEU, 
 wxID_EVENTEDITDIALOGCKCHQJOUR, wxID_EVENTEDITDIALOGCKCHQLUN, 
 wxID_EVENTEDITDIALOGCKCHQMAGHREB, wxID_EVENTEDITDIALOGCKCHQMAR, 
 wxID_EVENTEDITDIALOGCKCHQMER, wxID_EVENTEDITDIALOGCKCHQPRIERE, 
 wxID_EVENTEDITDIALOGCKCHQSAM, wxID_EVENTEDITDIALOGCKCHQSEM, 
 wxID_EVENTEDITDIALOGCKCHQVEN, wxID_EVENTEDITDIALOGENDDATE, 
 wxID_EVENTEDITDIALOGHEUREDEBUT, wxID_EVENTEDITDIALOGHEUREFIN, 
 wxID_EVENTEDITDIALOGSTARTDATE, wxID_EVENTEDITDIALOGSTATICBOX1, 
 wxID_EVENTEDITDIALOGSTATICLINE1, wxID_EVENTEDITDIALOGSTATICTEXT1, 
 wxID_EVENTEDITDIALOGSTATICTEXT2, wxID_EVENTEDITDIALOGSTATICTEXT3, 
 wxID_EVENTEDITDIALOGSTATICTEXT4, wxID_EVENTEDITDIALOGSTATICTEXT5, 
 wxID_EVENTEDITDIALOGSTATICTEXT6, wxID_EVENTEDITDIALOGTXTHEURE, 
 wxID_EVENTEDITDIALOGTXTMESSAGE, 
] = [wx.NewId() for _init_ctrls in range(33)]

class EventEditDialog(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_EVENTEDITDIALOG, name='', parent=prnt,
              pos=wx.Point(442, 264), size=wx.Size(648, 365),
              style=wx.DEFAULT_DIALOG_STYLE,
              title=u'Edition des Ev\xe8nements')
        self.SetClientSize(wx.Size(640, 331))

        self.ckChqJour = wx.CheckBox(id=wxID_EVENTEDITDIALOGCKCHQJOUR,
              label=u'Tous les jours', name='ckChqJour', parent=self,
              pos=wx.Point(24, 32), size=wx.Size(560, 13), style=0)
        self.ckChqJour.SetValue(True)
        self.ckChqJour.Bind(wx.EVT_CHECKBOX, self.OnCkChqJourCheckbox,
              id=wxID_EVENTEDITDIALOGCKCHQJOUR)

        self.ckChqDim = wx.CheckBox(id=wxID_EVENTEDITDIALOGCKCHQDIM,
              label=u'Dimanche', name='ckChqDim', parent=self, pos=wx.Point(24,
              56), size=wx.Size(70, 13), style=0)
        self.ckChqDim.SetValue(True)
        self.ckChqDim.Bind(wx.EVT_CHECKBOX, self.OnCkChqJournee,
              id=wxID_EVENTEDITDIALOGCKCHQDIM)

        self.ckChqLun = wx.CheckBox(id=wxID_EVENTEDITDIALOGCKCHQLUN,
              label=u'Lundi', name='ckChqLun', parent=self, pos=wx.Point(104,
              56), size=wx.Size(70, 13), style=0)
        self.ckChqLun.SetValue(True)
        self.ckChqLun.Bind(wx.EVT_CHECKBOX, self.OnCkChqJournee,
              id=wxID_EVENTEDITDIALOGCKCHQLUN)

        self.ckChqMar = wx.CheckBox(id=wxID_EVENTEDITDIALOGCKCHQMAR,
              label=u'Mardi', name='ckChqMar', parent=self, pos=wx.Point(184,
              56), size=wx.Size(70, 13), style=0)
        self.ckChqMar.SetValue(True)
        self.ckChqMar.Bind(wx.EVT_CHECKBOX, self.OnCkChqJournee,
              id=wxID_EVENTEDITDIALOGCKCHQMAR)

        self.ckChqMer = wx.CheckBox(id=wxID_EVENTEDITDIALOGCKCHQMER,
              label=u'Mercredi', name='ckChqMer', parent=self, pos=wx.Point(264,
              56), size=wx.Size(70, 13), style=0)
        self.ckChqMer.SetValue(True)
        self.ckChqMer.Bind(wx.EVT_CHECKBOX, self.OnCkChqJournee,
              id=wxID_EVENTEDITDIALOGCKCHQMER)

        self.ckChqJeu = wx.CheckBox(id=wxID_EVENTEDITDIALOGCKCHQJEU,
              label=u'Jeudi', name='ckChqJeu', parent=self, pos=wx.Point(344,
              56), size=wx.Size(70, 13), style=0)
        self.ckChqJeu.SetValue(True)
        self.ckChqJeu.Bind(wx.EVT_CHECKBOX, self.OnCkChqJournee,
              id=wxID_EVENTEDITDIALOGCKCHQJEU)

        self.ckChqVen = wx.CheckBox(id=wxID_EVENTEDITDIALOGCKCHQVEN,
              label=u'Vendredi', name='ckChqVen', parent=self, pos=wx.Point(424,
              56), size=wx.Size(70, 13), style=0)
        self.ckChqVen.SetValue(True)
        self.ckChqVen.Bind(wx.EVT_CHECKBOX, self.OnCkChqJournee,
              id=wxID_EVENTEDITDIALOGCKCHQVEN)

        self.ckChqSam = wx.CheckBox(id=wxID_EVENTEDITDIALOGCKCHQSAM,
              label=u'Samedi', name='ckChqSam', parent=self, pos=wx.Point(504,
              56), size=wx.Size(70, 13), style=0)
        self.ckChqSam.SetValue(True)
        self.ckChqSam.Bind(wx.EVT_CHECKBOX, self.OnCkChqJournee,
              id=wxID_EVENTEDITDIALOGCKCHQSAM)

        self.ckChqPriere = wx.CheckBox(id=wxID_EVENTEDITDIALOGCKCHQPRIERE,
              label=u'Toutes les pri\xe8res', name='ckChqPriere', parent=self,
              pos=wx.Point(24, 80), size=wx.Size(560, 13), style=0)
        self.ckChqPriere.SetValue(True)
        self.ckChqPriere.Bind(wx.EVT_CHECKBOX, self.OnCkChqPriereCheckbox,
              id=wxID_EVENTEDITDIALOGCKCHQPRIERE)

        self.ckChqFajr = wx.CheckBox(id=wxID_EVENTEDITDIALOGCKCHQFAJR,
              label=u'Fajr', name='ckChqFajr', parent=self, pos=wx.Point(24,
              104), size=wx.Size(76, 13), style=0)
        self.ckChqFajr.SetValue(True)
        self.ckChqFajr.Bind(wx.EVT_CHECKBOX, self.OnCkChqSalat,
              id=wxID_EVENTEDITDIALOGCKCHQFAJR)

        self.ckChqChourouk = wx.CheckBox(id=wxID_EVENTEDITDIALOGCKCHQCHOUROUK,
              label=u'Chourouk', name='ckChqChourouk', parent=self,
              pos=wx.Point(104, 104), size=wx.Size(76, 13), style=0)
        self.ckChqChourouk.SetValue(True)
        self.ckChqChourouk.Bind(wx.EVT_CHECKBOX, self.OnCkChqSalat,
              id=wxID_EVENTEDITDIALOGCKCHQCHOUROUK)

        self.ckChqDhohr = wx.CheckBox(id=wxID_EVENTEDITDIALOGCKCHQDHOHR,
              label=u'Dhohr', name='ckChqDhohr', parent=self, pos=wx.Point(184,
              104), size=wx.Size(76, 13), style=0)
        self.ckChqDhohr.SetValue(True)
        self.ckChqDhohr.Bind(wx.EVT_CHECKBOX, self.OnCkChqSalat,
              id=wxID_EVENTEDITDIALOGCKCHQDHOHR)

        self.ckChqAsr = wx.CheckBox(id=wxID_EVENTEDITDIALOGCKCHQASR,
              label=u'ASR', name='ckChqAsr', parent=self, pos=wx.Point(264,
              104), size=wx.Size(76, 13), style=0)
        self.ckChqAsr.SetValue(True)
        self.ckChqAsr.Bind(wx.EVT_CHECKBOX, self.OnCkChqSalat,
              id=wxID_EVENTEDITDIALOGCKCHQASR)

        self.ckChqMaghreb = wx.CheckBox(id=wxID_EVENTEDITDIALOGCKCHQMAGHREB,
              label=u'Maghreb', name='ckChqMaghreb', parent=self,
              pos=wx.Point(344, 104), size=wx.Size(76, 13), style=0)
        self.ckChqMaghreb.SetValue(True)
        self.ckChqMaghreb.Bind(wx.EVT_CHECKBOX, self.OnCkChqSalat,
              id=wxID_EVENTEDITDIALOGCKCHQMAGHREB)

        self.ckChqIshaa = wx.CheckBox(id=wxID_EVENTEDITDIALOGCKCHQISHAA,
              label=u'Ishaa', name='ckChqIshaa', parent=self, pos=wx.Point(424,
              104), size=wx.Size(76, 13), style=0)
        self.ckChqIshaa.SetValue(True)
        self.ckChqIshaa.Bind(wx.EVT_CHECKBOX, self.OnCkChqSalat,
              id=wxID_EVENTEDITDIALOGCKCHQISHAA)

        self.ckChqSem = wx.CheckBox(id=wxID_EVENTEDITDIALOGCKCHQSEM,
              label=u'Chaque semaine', name='ckChqSem', parent=self,
              pos=wx.Point(24, 128), size=wx.Size(152, 13), style=0)
        self.ckChqSem.SetValue(True)

        self.startDate = wx.lib.masked.textctrl.TextCtrl(id=wxID_EVENTEDITDIALOGSTARTDATE,
              name='startDate', parent=self, pos=wx.Point(88, 176),
              size=wx.Size(78, 22), style=0, value=u'    /  /  ')
        self.startDate.SetAutoformat('EUDATEYYYYMMDD/')
        self.startDate.SetExcludeChars('')

        self.endDate = wx.lib.masked.textctrl.TextCtrl(id=wxID_EVENTEDITDIALOGENDDATE,
              name='endDate', parent=self, pos=wx.Point(248, 176),
              size=wx.Size(78, 22), style=0, value=u'    /  /  ')
        self.endDate.SetAutoformat('EUDATEYYYYMMDD/')
        self.endDate.SetExcludeChars('')

        self.txtHeure = wx.lib.masked.timectrl.TimeCtrl(display_seconds=True,
              fmt24hr=False, id=wxID_EVENTEDITDIALOGTXTHEURE, name='txtHeure',
              oob_color=wx.NamedColour('Yellow'), parent=self, pos=wx.Point(88,
              208), size=wx.Size(43, 22), style=0, useFixedWidthFont=True,
              value='12:00:00 AM')
        self.txtHeure.SetFormat('24HHMM')

        self.heureDebut = wx.SpinCtrl(id=wxID_EVENTEDITDIALOGHEUREDEBUT,
              initial=0, max=99, min=-99, name='heureDebut', parent=self,
              pos=wx.Point(248, 208), size=wx.Size(58, 21),
              style=wx.SP_ARROW_KEYS)

        self.heureFin = wx.SpinCtrl(id=wxID_EVENTEDITDIALOGHEUREFIN, initial=0,
              max=100, min=0, name='heureFin', parent=self, pos=wx.Point(384,
              208), size=wx.Size(58, 21), style=wx.SP_ARROW_KEYS)
        self.heureFin.SetRange(-99, 99)

        self.txtMessage = wx.TextCtrl(id=wxID_EVENTEDITDIALOGTXTMESSAGE,
              name='txtMessage', parent=self, pos=wx.Point(88, 240),
              size=wx.Size(352, 48),
              style=wx.TE_PROCESS_ENTER | wx.TE_MULTILINE, value=u'')
        self.txtMessage.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Courier New'))

        self.staticBox1 = wx.StaticBox(id=wxID_EVENTEDITDIALOGSTATICBOX1,
              label=u'Type \xe9v\xe8nement', name='staticBox1', parent=self,
              pos=wx.Point(8, 8), size=wx.Size(624, 152), style=0)

        self.staticText1 = wx.StaticText(id=wxID_EVENTEDITDIALOGSTATICTEXT1,
              label=u'Date d\xe9but', name='staticText1', parent=self,
              pos=wx.Point(16, 176), size=wx.Size(54, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_EVENTEDITDIALOGSTATICTEXT2,
              label=u'Date fin', name='staticText2', parent=self,
              pos=wx.Point(200, 176), size=wx.Size(38, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_EVENTEDITDIALOGSTATICTEXT3,
              label=u'Heure', name='staticText3', parent=self, pos=wx.Point(16,
              216), size=wx.Size(29, 13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_EVENTEDITDIALOGSTATICTEXT4,
              label=u'D\xe9but', name='staticText4', parent=self,
              pos=wx.Point(200, 216), size=wx.Size(29, 13), style=0)

        self.staticText5 = wx.StaticText(id=wxID_EVENTEDITDIALOGSTATICTEXT5,
              label=u'Fin', name='staticText5', parent=self, pos=wx.Point(352,
              216), size=wx.Size(14, 13), style=0)

        self.staticText6 = wx.StaticText(id=wxID_EVENTEDITDIALOGSTATICTEXT6,
              label=u'Message', name='staticText6', parent=self,
              pos=wx.Point(16, 248), size=wx.Size(42, 13), style=0)

        self.btnValider = wx.Button(id=wxID_EVENTEDITDIALOGBTNVALIDER,
              label=u'Valider', name=u'btnValider', parent=self,
              pos=wx.Point(460, 300), size=wx.Size(80, 23), style=0)
        self.btnValider.Bind(wx.EVT_BUTTON, self.OnBtnValiderButton,
              id=wxID_EVENTEDITDIALOGBTNVALIDER)

        self.btnCancel = wx.Button(id=wxID_EVENTEDITDIALOGBTNCANCEL,
              label=u'Annuler', name=u'btnCancel', parent=self,
              pos=wx.Point(548, 300), size=wx.Size(80, 23), style=0)
        self.btnCancel.Bind(wx.EVT_BUTTON, self.OnBtnCancelButton,
              id=wxID_EVENTEDITDIALOGBTNCANCEL)

        self.staticLine1 = wx.StaticLine(id=wxID_EVENTEDITDIALOGSTATICLINE1,
              name='staticLine1', parent=self, pos=wx.Point(8, 292),
              size=wx.Size(624, 2), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.event = Events.Event()
        self.initUIFromData()
        
    def setEvent(self, ev):
        self.event.deserialize(ev.serialize())
        self.initUIFromData()
        
    def getEvent(self):
        return self.event

    def initUIFromData(self):
        data = self.event
        
        self.ckChqDim.SetValue(data.getType() & Events.TYPE_CHQ_DIM)
        self.ckChqLun.SetValue(data.getType() & Events.TYPE_CHQ_LUN)
        self.ckChqMar.SetValue(data.getType() & Events.TYPE_CHQ_MAR)
        self.ckChqMer.SetValue(data.getType() & Events.TYPE_CHQ_MER)
        self.ckChqJeu.SetValue(data.getType() & Events.TYPE_CHQ_JEU)
        self.ckChqVen.SetValue(data.getType() & Events.TYPE_CHQ_VEN)
        self.ckChqSam.SetValue(data.getType() & Events.TYPE_CHQ_SAM)
        
        self.ckChqJour.SetValue(data.getType() & Events.TYPE_CHQ_JOUR == Events.TYPE_CHQ_JOUR)
        
        self.ckChqFajr.SetValue(data.getType() & Events.TYPE_CHQ_FAJR)
        self.ckChqChourouk.SetValue(data.getType() & Events.TYPE_CHQ_CHOUROUK)
        self.ckChqDhohr.SetValue(data.getType() & Events.TYPE_CHQ_DHOHR)
        self.ckChqAsr.SetValue(data.getType() & Events.TYPE_CHQ_ASR)
        self.ckChqMaghreb.SetValue(data.getType() & Events.TYPE_CHQ_MAGHREB)
        self.ckChqIshaa.SetValue(data.getType() & Events.TYPE_CHQ_ISHAA)
        
        self.ckChqPriere.SetValue(data.getType() & Events.TYPE_CHQ_SALAT == Events.TYPE_CHQ_SALAT)
        
        self.ckChqSem.SetValue(data.getType() & Events.TYPE_CHQ_SEMAINE)
        
        dt = data.getStartDate()
        self.startDate.SetValue("%04d/%02d/%02d" % (dt.getAnnee() + 2000, dt.getMois(), dt.getJour()))
        
        dt = data.getEndDate()
        self.endDate.SetValue("%04d/%02d/%02d" % (dt.getAnnee() + 2000, dt.getMois(), dt.getJour()))
        
        tm = data.getTime()
        self.txtHeure.SetValue("%02d:%02d" % (tm.getHeure(), tm.getMinute()))
        
        self.heureDebut.SetValue(data.getStartInterval())
        self.heureFin.SetValue(data.getEndInterval())
        
        self.txtMessage.SetLabel(data.getMessage())
        
    def initDataFromUI(self):
        data = self.event
        
        val = int(self.ckChqDim.GetValue()) * Events.TYPE_CHQ_DIM | \
            int(self.ckChqLun.GetValue()) * Events.TYPE_CHQ_LUN | \
            int(self.ckChqMar.GetValue()) * Events.TYPE_CHQ_MAR | \
            int(self.ckChqMer.GetValue()) * Events.TYPE_CHQ_MER | \
            int(self.ckChqJeu.GetValue()) * Events.TYPE_CHQ_JEU | \
            int(self.ckChqVen.GetValue()) * Events.TYPE_CHQ_VEN | \
            int(self.ckChqSam.GetValue()) * Events.TYPE_CHQ_SAM | \
            int(self.ckChqFajr.GetValue()) * Events.TYPE_CHQ_FAJR | \
            int(self.ckChqChourouk.GetValue()) * Events.TYPE_CHQ_CHOUROUK | \
            int(self.ckChqDhohr.GetValue()) * Events.TYPE_CHQ_DHOHR | \
            int(self.ckChqAsr.GetValue()) * Events.TYPE_CHQ_ASR | \
            int(self.ckChqMaghreb.GetValue()) * Events.TYPE_CHQ_MAGHREB | \
            int(self.ckChqIshaa.GetValue()) * Events.TYPE_CHQ_ISHAA | \
            int(self.ckChqSem.GetValue()) * Events.TYPE_CHQ_SEMAINE
        data.setType(val)       
        
        
        data.getStartDate().parseString(self.startDate.GetValue())
        data.getEndDate().parseString(self.endDate.GetValue())
        
        data.getTime().parseString(self.txtHeure.GetValue())
        
        data.setStartInterval(self.heureDebut.GetValue())
        data.setEndInterval(self.heureFin.GetValue())
        data.setMessage(self.txtMessage.GetLabel())
    
    def OnCkChqJourCheckbox(self, event):
        self.ckChqDim.SetValue(self.ckChqJour.GetValue())
        self.ckChqLun.SetValue(self.ckChqJour.GetValue())
        self.ckChqMar.SetValue(self.ckChqJour.GetValue())
        self.ckChqMer.SetValue(self.ckChqJour.GetValue())
        self.ckChqJeu.SetValue(self.ckChqJour.GetValue())
        self.ckChqVen.SetValue(self.ckChqJour.GetValue())
        self.ckChqSam.SetValue(self.ckChqJour.GetValue())

    def OnCkChqJournee(self, event):
        self.ckChqJour.SetValue(self.ckChqDim.GetValue() &
                            self.ckChqLun.GetValue() &
                            self.ckChqMar.GetValue() &
                            self.ckChqMer.GetValue() &
                            self.ckChqJeu.GetValue() &
                            self.ckChqVen.GetValue() &
                            self.ckChqSam.GetValue())
        
    def OnCkChqPriereCheckbox(self, event):
        self.ckChqFajr.SetValue(self.ckChqPriere.GetValue())
        self.ckChqChourouk.SetValue(self.ckChqPriere.GetValue())
        self.ckChqDhohr.SetValue(self.ckChqPriere.GetValue())
        self.ckChqAsr.SetValue(self.ckChqPriere.GetValue())
        self.ckChqMaghreb.SetValue(self.ckChqPriere.GetValue())
        self.ckChqIshaa.SetValue(self.ckChqPriere.GetValue())
        
    def OnCkChqSalat(self, event):
        self.ckChqPriere.SetValue(self.ckChqFajr.GetValue() &
                            self.ckChqChourouk.GetValue() &
                            self.ckChqDhohr.GetValue() &
                            self.ckChqAsr.GetValue() &
                            self.ckChqMaghreb.GetValue() &
                            self.ckChqIshaa.GetValue())

    def OnBtnValiderButton(self, event):
        self.initDataFromUI()
        self.EndModal(wx.ID_OK)

    def OnBtnCancelButton(self, event):
        self.EndModal(wx.ID_CANCEL)
    
