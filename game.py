import pygame
import math

# Variables/Constants
SIZE = 500
SCALE = 20
FPS = 10
COLORS = {
    "BACKGROUND" : (25,1,33),
    "SNAKE" : (70,4,121),
    "FOOD" : (140,45,143),
    "GRID": (16, 22, 63)
}

# Snake Class
class Snake:
    def __init__(self, x=0, y=0, xspeed=0, yspeed=1):
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
    
    def update(self):
        self.x += self.xspeed * SCALE
        self.y += self.yspeed * SCALE

        if self.x < 0:
            self.x = SIZE - SCALE
        if self.x >= SIZE:
            self.x = 0
        
        if self.y < 0:
            self.y = SIZE - SCALE
        if self.y >= SIZE:
            self.y = 0
    
    def draw(self):
        pygame.draw.rect(window, COLORS["SNAKE"], [self.x,self.y, SCALE,SCALE])

# Setup
pygame.init()
window = pygame.display.set_mode((SIZE,SIZE))
window.fill(COLORS["BACKGROUND"])
clock = pygame.time.Clock()
pygame.display.set_caption("Snake 🐍")

# Get middle of the Screen, Subtract half a snake length from it, place snake in that position
snake = Snake(round(SIZE/SCALE) / 2 * SCALE - SCALE /2,round(SIZE/SCALE) / 2 * SCALE - SCALE /2,0,0)

def drawGrid():
    for x in range(0,SIZE,SCALE):
        for y in range(0,SIZE,SCALE):
            rect = pygame.Rect(x, y, SCALE, SCALE)
            pygame.draw.rect(window, COLORS["GRID"], rect, 1)
# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit game when window is closed
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.xspeed = -1
                snake.yspeed = 0
            if event.key == pygame.K_RIGHT:
                snake.xspeed = 1
                snake.yspeed = 0
            if event.key == pygame.K_UP:
                snake.xspeed = 0
                snake.yspeed = -1
            if event.key == pygame.K_DOWN:
                snake.xspeed = 0
                snake.yspeed = 1
    drawGrid()
    snake.update()
    snake.draw()
    pygame.display.update()
    window.fill(COLORS["BACKGROUND"])
    clock.tick(FPS)