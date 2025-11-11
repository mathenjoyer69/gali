import pygame
import BaseBlock


class AirBlock(BaseBlock):
    def __init__(self, x, y, size):
        super.__init__(self,x,y,size, 0)
