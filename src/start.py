'''
Created on 07.02.2011

@author: simon
'''

import klt
import pygame
import constants

if __name__ == '__main__':
    if constants.FULLSCREEN:
    	screen = pygame.display.set_mode(constants.RESOLUTION, pygame.FULLSCREEN)
    else:
	screen = pygame.display.set_mode(constants.RESOLUTION)
    klt.klt(screen).start()
