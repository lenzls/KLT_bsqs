import pygame
import os

class RessourceLoader():
    basepath = os.path.join(os.path.dirname(__file__), "..")

    def __init__(self, basepath):
        pass

    @classmethod
    def load_graphic(RessourceLoader, filename):
        path = os.path.join(RessourceLoader.basepath, 'data',  filename)
        return pygame.image.load(path).convert_alpha()
    
    @classmethod
    def load_font(RessourceLoader, filename, size):
        path = os.path.join(RessourceLoader.basepath,'data',filename)
        font_object = None
        try:
            font_object = pygame.font.Font(path, size)
        except:
            print "Error while loading font: ", filename, " in: ", path
        return font_object
