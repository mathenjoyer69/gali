import pygame
import BaseBlock
import AirBlock


class GlassBlock(BaseBlock.BaseBlock):
    def __init__(self, x, y,  type):
        super().__init__(x, y, (255,255,255), type)


    def update(self, matrix):
            max_y = len(matrix) - 1
            x = self.list_x
            y = self.list_y

            def move_to(nx, ny):
                # swap objects in matrix
                matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x]
                # update this sand block’s indices/coords/rect
                self.list_x, self.list_y = nx, ny
                self.x, self.y = nx * 20, ny * 20
                self.rect.topleft = (self.x, self.y)

            if y < max_y and matrix[y + 1][x].type == 0:
                move_to(x, y + 1)
                return matrix
            elif matrix[y - 1][x].type == 2 and matrix[y - 1][x].moving == False and  matrix[y - 2][x].type == 2 and matrix[y - 2][x].moving == False and matrix[y - 3][x].type == 2 and matrix[y - 3][x].moving == False:
                matrix[y][x] = AirBlock.AirBlock(self.x, self.y, (0,0,0), 0)

            return matrix
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
