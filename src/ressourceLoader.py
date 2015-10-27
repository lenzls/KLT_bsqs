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
