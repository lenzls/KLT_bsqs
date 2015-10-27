# -*- coding: utf-8 -*-
#
# KLT_bsqs
# Programm zur Vorbereitung auf den Konzentrationsleistungstest B2
#
# Copyright 2011 Simon Lenz
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
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
