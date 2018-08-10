#Boa:FramePanel:BoussoleFrame

#-----------------------------------------------------------------------------
# Name:        boussole.py
# Purpose:     
#
# Author:      MANI Mohamed Anis
#
# Created:     2007/09/04
# RCS-ID:      $Id: boussole.py $
# Copyright:   (c) 2006
# Licence:     GPL
#-----------------------------------------------------------------------------

import wx
import libitl
import math

[wxID_BOUSSOLEFRAME] = [wx.NewId() for _init_ctrls in range(1)]

class BoussoleFrame(wx.Panel):
    def _init_ctrls(self, prnt, id, pos, size, style, name):
        # generated method, don't edit
        wx.Panel.__init__(self, id=id, name=name,
              parent=prnt, pos=pos, size=size, style=style)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnBoussoleFrameEraseBackground)

    def __init__(self, parent, id, pos, size, style, name):
        self.bitmap = wx.Bitmap("qibla.png", wx.BITMAP_TYPE_PNG)
        self._init_ctrls(parent, id, pos, size, style, name)
        self.setQiblaDirection(0.0)
        
    def setQiblaDirection(self, value):
        self.qiblaDir = value
        deg, min, sec = libitl.decimal2Dms(self.qiblaDir)
        self.qiblaText = u'\u0627\u0644\u0642\u0628\u0644\u0629 : %d\xb0 %d" \u0627' % (deg, min)
        self.angle = libitl.deg_to_rad((-self.qiblaDir - 90))
        self.Refresh()
        self.Update()

    def OnBoussoleFrameEraseBackground(self, event):
        dc = event.GetDC()
        
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        
        dc.DrawBitmap(self.bitmap, 5, 15)
        
        sz = self.GetSize()
        
        dc.SetFont(self.GetFont())
        
        cPt = (59, 66)
        
        dc.DrawLabel(self.qiblaText, wx.Rect(0, 0, sz[0], 15), wx.ALIGN_CENTER)
        
        xPos = cPt[0] + ((sz[0] / 2) - 1) * math.cos(self.angle)
        yPos = cPt[1] + ((sz[1] / 2) - 1) * math.sin(self.angle)        
        dc.SetPen(wx.Pen(wx.BLACK, 4))
        dc.DrawLine(cPt[0], cPt[1], xPos, yPos)
        dc.SetPen(wx.Pen(wx.RED, 4))
        dc.DrawLine(cPt[0] + 2, cPt[1] + 2, xPos + 2, yPos + 2)
        