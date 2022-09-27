import pygame
import random

# Variables/Constants
SIZE = 400
SCALE = 20
FPS = 10
COLORS = {
    "BACKGROUND" : (25,1,33),
    "SNAKE" : (70,4,121),
    "FOOD" : (179, 18, 45),
    "GRID": (16, 22, 63)
}
tiles = round(SIZE/SCALE)

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

# Food Class
class Food:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(window, COLORS["FOOD"], [self.x,self.y, SCALE,SCALE])
    
    def eat(self,snake):
        if self.x == snake.x and self.y == snake.y:
            self.x = random.randrange(0,tiles) * SCALE
            self.y = random.randrange(0,tiles) * SCALE
# Setup
pygame.init()
window = pygame.display.set_mode((SIZE,SIZE))
window.fill(COLORS["BACKGROUND"])
clock = pygame.time.Clock()
pygame.display.set_caption("Snake 🐍")

# Place Snake on a random tile
snake = Snake(random.randrange(0,tiles) * SCALE, random.randrange(0,tiles) * SCALE,0,0)

# Place Food on a random tile, TODO: Check if the tile is free
food = Food(random.randrange(0,tiles) * SCALE, random.randrange(0,tiles) * SCALE)

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
    food.draw()
    snake.update()
    food.eat(snake)
    snake.draw()
    pygame.display.update()
    window.fill(COLORS["BACKGROUND"])
    clock.tick(FPS)