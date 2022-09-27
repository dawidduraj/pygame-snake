from os import TMP_MAX
import pygame
import random

# Variables/Constants
SIZE = 400
SCALE = 20
FPS = 20
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
        self.xspeed = xspeed
        self.yspeed = yspeed

        # for easier position updating we seperate the snakes body and head
        self.head = [x,y]
        self.body = []
    
    def update(self):
        if len(self.body) > 0:
            for i in range(len(self.body) - 1):
                # set piece position to position of the piece before it
                self.body[i][0] = self.body[i+1][0]
                self.body[i][1] = self.body[i+1][1]

            # set first piece position to head position
            self.body[len(self.body) - 1][0] = self.head[0]
            self.body[len(self.body) - 1][1] = self.head[1]
        
        self.head[0] += self.xspeed * SCALE
        self.head[1] += self.yspeed * SCALE
        if self.head[0] < 0:
            self.head[0] = SIZE - SCALE
        if self.head[0] >= SIZE:
            self.head[0] = 0
        
        if self.head[1] < 0:
            self.head[1] = SIZE - SCALE
        if self.head[1] >= SIZE:
            self.head[1] = 0
    
    def draw(self):
        pygame.draw.rect(window, COLORS["SNAKE"], [self.head[0],self.head[1], SCALE,SCALE])
        for part in self.body:
            pygame.draw.rect(window, COLORS["SNAKE"], [part[0],part[1], SCALE,SCALE])

# Food Class
class Food:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(window, COLORS["FOOD"], [self.x,self.y, SCALE,SCALE])
    
    def eat(self,snake):
        if self.x == snake.head[0] and self.y == snake.head[1]:
            snake.body.insert(0,[self.x,self.y])
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
    food.eat(snake)
    snake.update()
    snake.draw()
    pygame.display.update()
    window.fill(COLORS["BACKGROUND"])
    clock.tick(FPS)