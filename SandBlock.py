import pygame

import BaseBlock


class SandBlock(BaseBlock.BaseBlock):
    def __init__(self, x, y, type):
        super().__init__(x, y, (222, 186, 69),type)
        self.temp = 20



    def update(self,matrix):
        if self.list_y < len(matrix) - 1:
            if matrix[int(self.list_y + 1)][int(self.list_x)].type == 0:
                self.list_y += 1
                self.y += 20
                self.rect.topleft = (self.x, self.y)

            elif matrix[int(self.list_y + 1)][int(self.list_x - 1)].type == 0:**
                self.list_y += 1
                self.y += 20
                self.list_x -= 1
                self.x -= 20
                self.rect.topleft = (self.x, self.y)
            elif matrix[int(self.list_y + 1)][int(self.list_x + 1)].type == 0:
                self.list_y += 1
                self.y += 20
                self.list_x += 1
                self.x += 20
                self.rect.topleft = (self.x, self.y)


    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self.rect)

