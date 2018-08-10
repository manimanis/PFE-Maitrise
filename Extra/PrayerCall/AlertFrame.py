#Boa:MiniFrame:AlertFrame

#-----------------------------------------------------------------------------
# Name:        AlertFrame.py
# Purpose:     
#
# Author:      MANI Mohamed Anis
#
# Created:     2007/09/04
# RCS-ID:      $Id: AlertFrame.py $
# Copyright:   (c) 2006
# Licence:     GPL
#-----------------------------------------------------------------------------

import wx

def create(parent):
    return AlertFrame(parent)

[wxID_ALERTFRAME, wxID_ALERTFRAMETIPS, 
] = [wx.NewId() for _init_ctrls in range(2)]

[wxID_ALERTFRAMETIMER] = [wx.NewId() for _init_utils in range(1)]

class AlertFrame(wx.MiniFrame):
    WINDOW_SHOWING = 1
    WINDOW_VISIBLE = 2
    WINDOW_HIDING = 3
    
    def _init_utils(self):
        # generated method, don't edit
        self.timer = wx.Timer(id=wxID_ALERTFRAMETIMER, owner=self)
        self.Bind(wx.EVT_TIMER, self.OnTimerTimer, id=wxID_ALERTFRAMETIMER)


    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.MiniFrame.__init__(self, id=wxID_ALERTFRAME, name=u'AlertFrame',
              parent=prnt, pos=wx.Point(397, 331), size=wx.Size(200, 89),
              style=wx.STAY_ON_TOP, title=u'')
        self._init_utils()
        self.SetClientSize(wx.Size(192, 62))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))

        self.tips = wx.StaticText(id=wxID_ALERTFRAMETIPS, label=u'1\n2\n3',
              name=u'tips', parent=self, pos=wx.Point(0, 0), size=wx.Size(192,
              62), style=wx.ALIGN_RIGHT | wx.ST_NO_AUTORESIZE)
        self.tips.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))
        self.tips.Bind(wx.EVT_LEFT_UP, self.OnTipsLeftUp)
        self.tips.Bind(wx.EVT_RIGHT_UP, self.OnTipsRightUp)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.wid = wx.SystemSettings_GetMetric(wx.SYS_SCREEN_X)
        self.hei = wx.SystemSettings_GetMetric(wx.SYS_SCREEN_Y)
        self.timer.Stop()
        
    def setTip(self, texttip):
        self.tips.SetLabel(texttip)

    def OnTipsLeftUp(self, event):
        self.showWindow(False)

    def OnTipsRightUp(self, event):
        self.showWindow(False)
    
    def showWindow(self, value = True):
        if not value:
            self.isShowing = self.WINDOW_HIDING
            self.timer.Start(10)
        else:
            sz = self.GetSize()
            self.posX = self.wid - sz[0] - 2
            self.posY = self.hei - sz[1] - 40
            self.SetPosition(wx.Point(self.wid, self.posY))
            self.isShowing = self.WINDOW_SHOWING
            self.Show(value)
            self.timer.Start(10)

    def OnTimerTimer(self, event):
        if self.isShowing == self.WINDOW_SHOWING:
            pos = self.GetPosition()
            if pos[0] > self.posX:
                pos[0] -= 10
                self.SetPosition(wx.Point(pos[0], self.posY))
            else:
                self.isShowing = self.WINDOW_VISIBLE
                self.counter = 1000
        elif self.isShowing == self.WINDOW_HIDING:
            pos = self.GetPosition()
            if pos[0] < self.wid:
                pos[0] += 10
                self.SetPosition(wx.Point(pos[0], self.posY))
            else:
                self.timer.Stop()
                self.Show(False)
        else:
            self.counter -= 1
            if self.counter <= 0:
                self.isShowing = self.WINDOW_HIDING
