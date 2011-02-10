'''
Created on 07.02.2011

@author: simon
'''

from symbol import Symbol
import pygame
import random
from ressourceLoader import RessourceLoader
import time
import constants

class klt(object):
    '''
    classdocs
    '''


    def __init__(self, screen):
        '''
        Constructor
        '''
        pygame.init()
        self.screen = screen
        
        self.gameRunning = False
    
        self.currentChar = 0
        self.corC = 0
        self.wroC = 0
        self.allC = 0
        
        self.font = RessourceLoader.load_font('courier_new.ttf',15)
        self.topicFont = RessourceLoader.load_font('courier_new.ttf',35)

        #init symbols:
        self.symbolList = []
        self.symbolList.append(Symbol("b_1o.png", False))
        self.symbolList.append(Symbol("b_1u_1o.png", True))
        self.symbolList.append(Symbol("b_1u_2o.png", False))
        self.symbolList.append(Symbol("b_1u.png", False))
        self.symbolList.append(Symbol("b_2o.png", True))
        self.symbolList.append(Symbol("b_2u_1o.png", False))
        self.symbolList.append(Symbol("b_2u_2o.png", False))
        self.symbolList.append(Symbol("b_2u.png", True))

        self.symbolList.append(Symbol("q_1u_1o.png", False))
        self.symbolList.append(Symbol("q_2o.png", False))
        self.symbolList.append(Symbol("q_2u_2o.png", False))
        self.symbolList.append(Symbol("q_2u.png", False))

        #timer stuff:
        self.timer_start = 0
        self.timer_length = constants.TIMER
        self.timer_remaining = self.timer_length
        

    def render(self, curline):
        self.screen.fill((255,255,255))
        blackChar = pygame.Surface((10,32))
        blackChar.fill((0,0,0))
        x = 25
        i = 1
        for item in curline:
            if x > constants.RESOLUTION[0]:
                self.running = False
            print "too small x-resolution!!"
            if i < self.currentChar:
                self.screen.blit(blackChar, (x, constants.RESOLUTION[1]/2))
            self.screen.blit(item.image, (x, constants.RESOLUTION[1]/2))
            x += 25
            i += 1
            
        topicsurf = self.topicFont.render("KLT-rlp_2011", True, [0,0,0])
        allCsurf = self.font.render("Anzahl Symbole: "+str(self.allC), True, [0,0,0])
        CorCsurf = self.font.render("Korrekt: "+str(self.corC), True, [0,0,0])
        WroCsurf = self.font.render("Falsch: "+str(self.wroC), True, [0,0,0])
        remainsurf = self.font.render("Verbleibende Zeit [sec]: " +str(self.timer_remaining), True, [0,0,0])
        try: 
            percCor = (self.corC*100//self.allC)
        except ZeroDivisionError:
            percCor = 0
        percCorsurf = self.font.render("Korrekt [in %]: " +str(percCor), True, [0,0,0])
        try:
            corProMin = self.corC/((self.timer_length-self.timer_remaining)/60)
        except ZeroDivisionError:
            corProMin = 0
        corProMinsurf = self.font.render("Korrekt pro Minute: " +str(corProMin), True, [0,0,0])
        self.screen.blit(allCsurf, (100,100))
        self.screen.blit(CorCsurf, (100,120))
        self.screen.blit(WroCsurf, (100,140))
        self.screen.blit(remainsurf, (100,160))
        self.screen.blit(percCorsurf, (100,200))
        self.screen.blit(corProMinsurf, (100,220))
        
        self.screen.blit(topicsurf, (constants.RESOLUTION[0]-topicsurf.get_width()-100,150))
        
    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                
                elif event.key == pygame.K_SPACE:
                    if self.gameRunning:
                        self.stopRun()
                    else:
                        self.startRun()
                        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #Linke Maustaste
                if event.button == 1 and self.gameRunning:
                    self.checkSymbol(True)
                #Rechte Maustaste
                elif event.button == 3 and self.gameRunning:
                    self.checkSymbol(False)
    
    def checkSymbol(self, pressedValue):
        if self.currentLine[self.currentChar-1].valid == pressedValue:
            self.answCor()
        elif self.currentLine[self.currentChar-1].valid != pressedValue:
            self.answWro()
        else:
            print "Fehler!!"    
    
    def answCor(self):
        self.corC += 1
        self.allC += 1
        self.currentChar += 1
    
    def answWro(self):
        self.wroC += 1
        self.allC += 1
        self.currentChar +=1
    
    def startRun(self):
        self.corC = 0
        self.wroC = 0
        self.allC = 0
        self.gameRunning = True
        self.score = 0
        self.currentChar = 1
        
        self.timer_start = time.time()
        
    def stopRun(self):
        self.gameRunning = False
        self.currentChar = 0
        
        self.timer_start = 0

    def checkTimer(self):
        self.timer_remaining = (self.timer_length - (time.time()-self.timer_start))
        if time.time() - self.timer_start >= self.timer_length:
            print "zeit ist um"
            self.stopRun()
            
    def generateLine(self):
        self.currentLine = []
        for x in range(0,30):
            self.currentLine.append(self.symbolList[random.randrange(0,len(self.symbolList))])
            
    def start(self): 
        self.running = True

        self.generateLine()
        

        while self.running:
            self.handleInput()
            self.render(self.currentLine)
            
            if self.gameRunning:
                if self.currentChar > len(self.currentLine):
                    self.generateLine()
                    self.currentChar = 1
                
                self.checkTimer()
            pygame.display.update()        
