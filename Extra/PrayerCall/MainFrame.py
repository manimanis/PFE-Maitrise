#Boa:Frame:MainFrame

#-----------------------------------------------------------------------------
# Name:        MainFrame.py
# Purpose:     
#
# Author:      MANI Mohamed Anis
#
# Created:     2007/09/04
# RCS-ID:      $Id: MainFrame.py $
# Copyright:   (c) 2006
# Licence:     GPL
#-----------------------------------------------------------------------------

import wx
import wx.lib.analogclock
import libitl
import datetime
import pygame
import boussole
import AlertFrame
import settings_dialog
import sounds

import pickle

def create(parent):
    return MainFrame(parent)

[wxID_MAINFRAME, wxID_MAINFRAMEANALOGCLOCK, wxID_MAINFRAMEASSR, 
 wxID_MAINFRAMEFAJR, wxID_MAINFRAMEIMSAAK, wxID_MAINFRAMEISHAA, 
 wxID_MAINFRAMELATITUDE, wxID_MAINFRAMELONGITUDE, wxID_MAINFRAMEMAGHREB, 
 wxID_MAINFRAMENEXT_SALAT, wxID_MAINFRAMESHURUQ, wxID_MAINFRAMETHUHR, 
 wxID_MAINFRAMETIME_TO_NEXT, wxID_MAINFRAMETODAY_DATE, 
 wxID_MAINFRAMETODAY_DATE_HIJRI, wxID_MAINFRAMEVILLE, 
] = [wx.NewId() for _init_ctrls in range(16)]

class NotificationIcon(wx.TaskBarIcon):
    TBMENU_RESTORE = wx.NewId()
    TBMENU_CLOSE   = wx.NewId()
    TBMENU_STOP_SOUND = wx.NewId()
    TBMENU_PARAMETERS = wx.NewId()
    
    def __init__(self, frame):
        wx.TaskBarIcon.__init__(self)
        self.frame = frame

        # Set the image
        self.icon = wx.Icon('icon.ico', wx.BITMAP_TYPE_ICO )
        self.SetIcon(self.icon, u'Prayer Call')
        
        self.closeIcon = wx.Bitmap('close.png', wx.BITMAP_TYPE_PNG)
        self.restoreIcon = wx.Bitmap('rest.png', wx.BITMAP_TYPE_PNG)
        self.minimIcon = wx.Bitmap('min.png', wx.BITMAP_TYPE_PNG)
        self.stopIcon = wx.Bitmap('stop_sound.png', wx.BITMAP_TYPE_PNG)
        
        # bind some events
        self.Bind(wx.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarActivate)
        self.Bind(wx.EVT_MENU, self.OnTaskBarActivate, id=self.TBMENU_RESTORE)
        self.Bind(wx.EVT_MENU, self.OnTaskBarClose, id=self.TBMENU_CLOSE)
        self.Bind(wx.EVT_MENU, self.OnStopSound, id=self.TBMENU_STOP_SOUND)
        self.Bind(wx.EVT_MENU, self.OnParameters, id=self.TBMENU_PARAMETERS)

    def CreatePopupMenu(self):
        """
        This method is called by the base class when it needs to popup
        the menu for the default EVT_RIGHT_DOWN event.  Just create
        the menu how you want it and return it from this function,
        the base class takes care of the rest.
        """
        menu = wx.Menu()
        if self.frame.isAthanPlaying():
            stopSndMenu = wx.MenuItem(menu, self.TBMENU_STOP_SOUND, u'Arr\xeater le son')
            stopSndMenu.SetBitmap(self.stopIcon)
            menu.AppendItem(stopSndMenu)
            
            menu.AppendSeparator()
        
        menu.Append(self.TBMENU_PARAMETERS, "Changer les param\xe8tres...")
        menu.AppendSeparator()
        
        restoreText = u"Restaurer"
        icon = self.restoreIcon
        if self.frame.IsShown():
            restoreText = u"R\xe9duire"
            icon = self.minimIcon
        restoreMenu = wx.MenuItem(menu, self.TBMENU_RESTORE, restoreText)
        restoreMenu.SetBitmap(icon)
        menu.AppendItem(restoreMenu)
        
        closeMenu = wx.MenuItem(menu, self.TBMENU_CLOSE, u"Fermer")
        closeMenu.SetBitmap(self.closeIcon)
        menu.AppendItem(closeMenu)
        return menu
    
    def setTip(self, texttip):
        self.SetIcon(self.icon, texttip)
        
    def OnTaskBarActivate(self, evt):
        if not self.frame.IsShown():
            self.frame.Show(True)
            self.frame.Raise()
        else:
            self.frame.Show(False)

    def OnTaskBarClose(self, evt):
        self.frame.Close()
        
    def OnStopSound(self, evt):
        self.frame.stopAthan()
        
    def OnParameters(self, evt):
        self.frame.changeSettings()

[wxID_MAINFRAMEMYTIMER, wxID_MAINFRAMESNDTIMER, 
] = [wx.NewId() for _init_utils in range(2)]

class MainFrame(wx.Frame):
    def _init_utils(self):
        # generated method, don't edit
        self.Mytimer = wx.Timer(id=wxID_MAINFRAMEMYTIMER, owner=self)
        self.Mytimer.SetEvtHandlerEnabled(True)
        self.Bind(wx.EVT_TIMER, self.OnMytimerTimer, id=wxID_MAINFRAMEMYTIMER)

        self.menuBar = wx.MenuBar()

        self.sndTimer = wx.Timer(id=wxID_MAINFRAMESNDTIMER, owner=self)
        self.sndTimer.SetEvtHandlerEnabled(True)
        self.Bind(wx.EVT_TIMER, self.OnSndTimerTimer, id=wxID_MAINFRAMESNDTIMER)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_MAINFRAME, name=u'MainFrame',
              parent=prnt, pos=wx.Point(325, 243), size=wx.Size(640, 373),
              style=wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION,
              title=u'Prayer Call - \u0627\u0644\u0645\u0624\u0630\u0651\u0646')
        self._init_utils()
        self.SetClientSize(wx.Size(632, 346))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.Center(wx.BOTH)
        self.SetMenuBar(self.menuBar)
        self.SetIcon(wx.Icon(u'icon.ico',wx.BITMAP_TYPE_ICO))
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnMainFrameEraseBackground)
        self.Bind(wx.EVT_ICONIZE, self.OnMainFrameIconize)
        self.Bind(wx.EVT_CLOSE, self.OnMainFrameClose)
        self.Bind(wx.EVT_ACTIVATE, self.OnMainFrameActivate)
        self.Bind(wx.EVT_LEFT_DCLICK, self.OnMainFrameLeftDclick)

        self.ishaa = wx.StaticText(id=wxID_MAINFRAMEISHAA, label=u'99:99:99',
              name=u'ishaa', parent=self, pos=wx.Point(8, 313), size=wx.Size(77,
              21),
              style=wx.TRANSPARENT_WINDOW | wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)
        self.ishaa.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.shuruq = wx.StaticText(id=wxID_MAINFRAMESHURUQ, label=u'99:99:99',
              name=u'shuruq', parent=self, pos=wx.Point(364, 313),
              size=wx.Size(77, 21),
              style=wx.TRANSPARENT_WINDOW | wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)
        self.shuruq.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.thuhr = wx.StaticText(id=wxID_MAINFRAMETHUHR, label=u'99:99:99',
              name=u'thuhr', parent=self, pos=wx.Point(275, 313),
              size=wx.Size(77, 21),
              style=wx.TRANSPARENT_WINDOW | wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)
        self.thuhr.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.fajr = wx.StaticText(id=wxID_MAINFRAMEFAJR, label=u'99:99:99',
              name=u'fajr', parent=self, pos=wx.Point(454, 313),
              size=wx.Size(77, 21),
              style=wx.TRANSPARENT_WINDOW | wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)
        self.fajr.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.assr = wx.StaticText(id=wxID_MAINFRAMEASSR, label=u'99:99:99',
              name=u'assr', parent=self, pos=wx.Point(185, 313),
              size=wx.Size(77, 21),
              style=wx.TRANSPARENT_WINDOW | wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)
        self.assr.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.maghreb = wx.StaticText(id=wxID_MAINFRAMEMAGHREB,
              label=u'99:99:99', name=u'maghreb', parent=self, pos=wx.Point(95,
              313), size=wx.Size(77, 21),
              style=wx.TRANSPARENT_WINDOW | wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)
        self.maghreb.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.next_salat = wx.StaticText(id=wxID_MAINFRAMENEXT_SALAT, label=u'',
              name=u'next_salat', parent=self, pos=wx.Point(194, 195),
              size=wx.Size(115, 24),
              style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)
        self.next_salat.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))

        self.imsaak = wx.StaticText(id=wxID_MAINFRAMEIMSAAK, label=u'99:99:99',
              name=u'imsaak', parent=self, pos=wx.Point(544, 313),
              size=wx.Size(77, 21),
              style=wx.TRANSPARENT_WINDOW | wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)
        self.imsaak.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.analogClock = wx.lib.analogclock.analogclock.AnalogClock(id=wxID_MAINFRAMEANALOGCLOCK,
              name=u'analogClock', parent=self, pos=wx.Point(20, 16),
              size=wx.Size(162, 162), style=0)
        self.analogClock.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.analogClock.SetFaceFillColour(wx.Colour(255, 255, 255))

        self.time_to_next = wx.StaticText(id=wxID_MAINFRAMETIME_TO_NEXT,
              label=u'2 \u0633\u0627\u0639\u0629 \u0648 53 \u062f\u0642',
              name=u'time_to_next', parent=self, pos=wx.Point(194, 165),
              size=wx.Size(115, 24),
              style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)

        self.today_date = wx.StaticText(id=wxID_MAINFRAMETODAY_DATE, label=u'',
              name=u'today_date', parent=self, pos=wx.Point(20, 186),
              size=wx.Size(162, 20),
              style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)

        self.today_date_hijri = wx.StaticText(id=wxID_MAINFRAMETODAY_DATE_HIJRI,
              label=u'', name=u'today_date_hijri', parent=self, pos=wx.Point(20,
              212), size=wx.Size(162, 20),
              style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)

        self.longitude = wx.StaticText(id=wxID_MAINFRAMELONGITUDE, label=u'',
              name=u'longitude', parent=self, pos=wx.Point(373, 172),
              size=wx.Size(122, 23),
              style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)

        self.latitude = wx.StaticText(id=wxID_MAINFRAMELATITUDE, label=u'',
              name=u'latitude', parent=self, pos=wx.Point(373, 212),
              size=wx.Size(122, 21),
              style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)

        self.ville = wx.StaticText(id=wxID_MAINFRAMEVILLE, label=u'',
              name=u'ville', parent=self, pos=wx.Point(195, 109),
              size=wx.Size(227, 26),
              style=wx.ST_NO_AUTORESIZE | wx.ALIGN_CENTRE)
        self.ville.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        self.mixer = sounds.Mixer()
        
        self.currTime = libitl.Prayer()
        
        self.lastDiff = -1
        
        self.imageFond = wx.Bitmap("interface.png", wx.BITMAP_TYPE_PNG)
        self.bous = boussole.BoussoleFrame(self, id = wx.NewId(), 
            pos=wx.Point(508, 107), size=wx.Size(119, 120), style = wx.TAB_TRAVERSAL,
            name = u'bous')
        self.alertFrame = AlertFrame.AlertFrame(None)
        self.toolTip = wx.ToolTip(u'')
        self.remainText = u''
        self.tbicon = NotificationIcon(self)
        
        pygame.mixer.init()
        bism = sounds.Sound(self, 'bismilleh.ogg')
        bism.play()
        self.athan = sounds.Sound(self,'athan.ogg')
        self.bip = sounds.Sound(self, 'ding.ogg')
        
        self.nextSalFont = wx.Font(13, wx.SWISS, wx.NORMAL, wx.FONTWEIGHT_BOLD, False, u'Tahoma')
        self.salFont = wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Tahoma')
        self.nextSalColour = wx.Colour(255, 0, 0)
        self.salColour = wx.Colour(0, 0, 0)
        
        self.conf = wx.GetApp().conf
        self.loc = wx.GetApp().loc
        
        self.newDay()
        
        self.Mytimer.Start(1000)
        
        self.startUp = True
        
    def newDay(self):
        self.currPray = -1
        self.calcPrayersTimes()
        self.initCtrls()
    
    def prayerChanged(self):
        self.initCtrls()
    
    def playAthan(self):
        if self.currPray == libitl.FAJR:
            self.athan.setFileName("athan_fajr.ogg")
        else:
            self.athan.setFileName("athan.ogg")
        self.athan.play()
        
    def stopAthan(self):
        self.athan.stop()
        
    def isAthanPlaying(self):
        return self.athan.isPlaying()
        
    def bipSound(self):
        self.bip.play()
    
    def calcPrayersTimes(self):
        self.date = libitl.Date()
        
        self.ptimes = libitl.PrayersTimes(self.loc, self.conf, self.date)
        
        self.next_day = libitl.Date()
        self.next_day.nextDay()
        
        self.next_ptimes = libitl.PrayersTimes(self.loc, self.conf, self.date)
        
        self.getCurrentPrayer()
        
    def initCtrls(self):
        self.bous.setQiblaDirection(self.ptimes.getQiblaDirection())
        self.imsaak.SetLabel(str(self.ptimes.getImsaak()))
        
        self.fajr.SetLabel(str(self.ptimes.getFajr()))
        self.fajr.SetFont(self.nextSalFont if self.currPray == libitl.FAJR else self.salFont)
        self.fajr.SetForegroundColour(self.nextSalColour if self.currPray == libitl.FAJR else self.salColour)
        
        self.shuruq.SetLabel(str(self.ptimes.getShuruq()))
        
        self.thuhr.SetLabel(str(self.ptimes.getThuhr()))
        self.thuhr.SetFont(self.nextSalFont if self.currPray == libitl.THUHR else self.salFont)
        self.thuhr.SetForegroundColour(self.nextSalColour if self.currPray == libitl.THUHR else self.salColour)
        
        self.assr.SetLabel(str(self.ptimes.getAssr()))
        self.assr.SetFont(self.nextSalFont if self.currPray == libitl.ASSR else self.salFont)
        self.assr.SetForegroundColour(self.nextSalColour if self.currPray == libitl.ASSR else self.salColour)
        
        self.maghreb.SetLabel(str(self.ptimes.getMaghreb()))
        self.maghreb.SetFont(self.nextSalFont if self.currPray == libitl.MAGHRIB else self.salFont)
        self.maghreb.SetForegroundColour(self.nextSalColour if self.currPray == libitl.MAGHRIB else self.salColour)
        
        self.ishaa.SetLabel(str(self.ptimes.getIshaa()))
        self.ishaa.SetFont(self.nextSalFont if self.currPray == libitl.ISHAA else self.salFont)
        self.ishaa.SetForegroundColour(self.nextSalColour if self.currPray == libitl.ISHAA else self.salColour)
        
        self.today_date.SetLabel(self.date.getDayArabName() + u' ' + \
            str(self.date.getDay()) + u' ' + \
            self.date.getMonthArabName() + u' ' + str(self.date.getYear()))
        self.today_date_hijri.SetLabel(self.date.getDayArabName() + u' ' + \
            str(self.date.getDay()) + u' ' + \
            self.date.getMonthArabName() + u' ' + str(self.date.getYear()))
        
        deg, min, sec = libitl.decimal2Dms(self.loc.getLongitude())
        self.longitude.SetLabel(u'%d\xb0 %d"' % (deg, min))
        
        deg, min, sec = libitl.decimal2Dms(self.loc.getLatitude())
        self.latitude.SetLabel(u'%d\xb0 %d"' % (deg, min))
        
        self.ville.SetLabel(self.loc.getTownName() + u' - ' + self.loc.getCountryName())
        
        self.Refresh()
    
    def calcRemainingTime(self, tme):
        self.remainText = u''
        diff = (self.currPrayTime.getHour() - tme.hour) * 60 + self.currPrayTime.getMinute() - tme.minute
        if diff < 0:
            diff += 24 * 60
        
        if self.lastDiff < 0:
            self.initCtrls()
        
        if self.lastDiff <> diff:
            self.lastDiff = diff
            self.remainText = u'%d \u0633\u0627\u0639\u0629 \u0648 %d \u062f\u0642' % (diff / 60, diff % 60)
            self.time_to_next.SetLabel(u'\u0641\u0642\u0637 ' + self.remainText)
            
            self.remainText = u'\u0628\u0631\u0646\u0627\u0645\u062c \u0627\u0644\u0645\u0624\u0630\u0651\u0646\n\u0628\u0642\u064a %d \u0633\u0627\u0639\u0629 \u0648 %d \u062f\u0642 \u0644\u0635\u0644\u0627\u0629 %s' % (diff / 60, diff % 60, self.currPrayTime.getArabName())
            self.toolTip.SetTip(self.remainText)
            self.SetToolTip(self.toolTip)
            self.tbicon.setTip(self.remainText)
        
            if diff <= 15:
                self.bipSound()
                self.alertFrame.setTip(self.remainText)
                if not self.alertFrame.IsShown():
                    self.alertFrame.showWindow()
            
            if diff == 0:
                self.playAthan()
                
    def getCurrentPrayer(self):
        tme = libitl.time()
        if self.ptimes.getFajr().getTime() >= tme:
            currPray = libitl.FAJR
            self.currPrayTime = self.ptimes.getFajr()
        elif self.ptimes.getThuhr().getTime() >= tme:
            currPray = libitl.THUHR
            self.currPrayTime = self.ptimes.getThuhr()
        elif self.ptimes.getAssr().getTime() >= tme:
            currPray = libitl.ASSR
            self.currPrayTime = self.ptimes.getAssr()
        elif self.ptimes.getMaghreb().getTime() >= tme:
            currPray = libitl.MAGHRIB
            self.currPrayTime = self.ptimes.getMaghreb()
        elif self.ptimes.getIshaa().getTime() >= tme:
            currPray = libitl.ISHAA
            self.currPrayTime =  self.ptimes.getIshaa()
        else:
            currPray = libitl.NEXTFAJR
            self.currPrayTime = self.next_ptimes.getFajr()
        self.next_salat.SetLabel(self.currPrayTime.getArabName())
        
        if self.currPray != currPray:
            if currPray == libitl.FAJR and self.currPray == libitl.NEXTFAJR:
                self.currPray = currPray
                self.newDay()
            else:
                self.currPray = currPray
                self.prayerChanged()
        
        self.calcRemainingTime(tme)

    def iconizeToNotification(self):
        self.Show(False)
        
    def OnMainFrameEraseBackground(self, event):
        dc = event.GetDC()
        
        startPoint = (13 - 2 , 213 - 2)
        cellSize = wx.Size(91 - 12, 77 - 48)
        
        dc.Clear()
        dc.DrawBitmap(self.imageFond, 0, 0)
        #event.Skip()

    def OnMytimerTimer(self, event):
        self.getCurrentPrayer()

    def OnButton1Button(self, event):
        self.playAthan()

    def OnButton2Button(self, event):
        self.stopAthan()

    def OnMainFrameIconize(self, event):
        self.iconizeToNotification()

    def OnMainFrameClose(self, event):
        self.mixer.destroy()
        self.Mytimer.Stop()
        if self.tbicon is not None:
            self.tbicon.Destroy()
        self.Destroy()
        self.alertFrame.Destroy()
        wx.GetApp().ExitMainLoop()

    def OnMainFrameActivate(self, event):
        if self.startUp:
            self.startUp = False
            if event.GetActive():
                self.iconizeToNotification()

    def OnMainFrameLeftDclick(self, event):
        self.changeSettings()
    
    def changeSettings(self):
        dlg = settings_dialog.DlgSettings(self)
        dlg.initLocation(self.loc)
        dlg.initMethod(self.conf)
        ret = dlg.ShowModal()
        if ret == wx.ID_OK:
            self.loc = dlg.getLocation()
            self.conf = dlg.getMethod()
            
            wx.GetApp().saveConfig(self.loc, self.conf)
            
            self.Mytimer.Stop()
            self.calcPrayersTimes()
            self.initCtrls()
            self.Mytimer.Start(1000)
            
        dlg.Destroy()

    def OnSndTimerTimer(self, event):
        self.stopAthan()
        
