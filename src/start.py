'''
Created on 07.02.2011

@author: simon
'''

import klt
import pygame

if __name__ == '__main__':
    screen = pygame.display.set_mode((1024,768), pygame.FULLSCREEN)
    klt.klt(screen).start()
