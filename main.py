import pygame
import AirBlock
import StoneBlock

class Button:
    def __init__(self, x, y, width, height, variable, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.original_color = color
        self.variable = variable

    def draw(self, surface):
        self.color = self.original_color if self.variable else (255, 255, 255)
        pygame.draw.rect(surface, self.color, self.rect)

    def is_over(self, pos):
        return self.rect.collidepoint(pos)

class Simulation:
    def __init__(self, screen, width, height, speed, matrix):
        self.screen = screen
        self.width = width
        self.height = height
        self.speed = speed
        self.matrix = matrix
        self.button = Button(0, 0, 40, 40, True, (120, 120, 120))
        self.button1 = Button(100, 0, 40, 40, True, (120, 120, 120))
        self.button2 = Button(200, 0, 40, 40, True, (120, 120, 120))

    def update(self):
        if self.button.variable:
            n = len(self.matrix)
            for i in range(n, -1, -1):
                for j in range(n):
                    block = self.matrix[i][j]
                    block.update(self.matrix)

    def draw(self, surface, b1, b2):
        surface.fill((0, 0, 0))
        if self.button.variable:
            #original screen
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[1])):
                    block = self.matrix[i][j]
                    block.draw(surface)
        else:
            self.button1.draw(surface)
            self.button2.draw(surface)

        self.button.draw(surface)

    def add_block(self, b_type, pos):
        list_x = pos[0]
        list_y = pos[1]
        if b_type == 1:
            self.matrix[list_y][list_x] = StoneBlock.StoneBlock(list_x * 20, list_y * 20, b_type)

    @staticmethod
    def get_mouse_index(mouse_pos):
        return int(mouse_pos[0]/20), int(mouse_pos[1]/20)

    def run(self):
        running = True
        while running:
            self.draw(self.screen, self.button1, self.button2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.button.is_over(pygame.mouse.get_pos()):
                            self.button.variable = not self.button.variable
                        if self.button.variable:
                            self.add_block(1, self.get_mouse_index(pygame.mouse.get_pos()))

            pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    matrix =  [[AirBlock.AirBlock(i*20, j*20, (0, 0, 0), 0) for i in range(40)] for j in range(40)]

    sim = Simulation(screen, 800, 800, 0.1, matrix)
    sim.run()

main()
