'''
Created on 07.02.2011

@author: simon
'''
import ressourceLoader

class Symbol(object):
    '''
    classdocs
    '''


    def __init__(self, imageFileName, valid):
        '''
        Constructor
        '''
        self.image = ressourceLoader.RessourceLoader.load_graphic(imageFileName)
        self.valid = valid