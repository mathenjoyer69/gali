import pygame

class Water:
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.color = (0, 0, 255)
        self.list_x = x // 20
        self.list_y = y // 20
        self.height = height
        self.rect = pygame.Rect(x, y, self.height, self.height)
        self.type = 5
        self.positions = []

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def update(self, matrix):
        max_y = len(matrix) - 1
        max_x = len(matrix[0]) - 1
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

        elif matrix[y][x + 1].type == 0:
            move_to(x +1, y)