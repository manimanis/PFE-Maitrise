import pygame
import wx
import threading

class Mixer:
    def __init__(self):
        pygame.mixer.init()

    def destroy(self):
        pygame.mixer.quit()

class Sound:
    def __init__(self, frame, fileName):
        self.__frame = frame
        self.__fileName = fileName
        self.__isPlaying = False
        self.__snd = None
        
        self.__sndTimer = None
        
    def setFileName(self, fileName):
        self.__fileName = fileName
        
    def getFileName(self):
        return self.__fileName
    
    def play(self):
        if self.__isPlaying:
            return
        
        self.__isPlaying = True
        self.__snd = pygame.mixer.Sound(self.__fileName)
        self.__snd.play()
        self.__sndTimer =  threading.Timer(self.__snd.get_length() + 1, self.OnTimer)
        self.__sndTimer.start()
        
    def stop(self):
        self.__sndTimer.cancel()
        self.__sndTimer = None
        self.__isPlaying = False
        if self.__snd == None:
            return
        self.__snd.stop()
        self.__snd = None

    def OnTimer(self):
        self.stop()
        
    def isPlaying(self):
        return self.__isPlaying