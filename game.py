import pygame

# Variables/Constants
SIZE = 500
COLORS = {
    "BACKGROUND" : (25,1,33),
    "SNAKE" : (70,4,121),
    "FOOD" : (140,45,143)
}


# setup
pygame.init()
window = pygame.display.set_mode((SIZE,SIZE))
clock = pygame.time.Clock()
pygame.display.set_caption("Snake 🐍")
