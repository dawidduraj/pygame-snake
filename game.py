import pygame

# Variables/Constants
SIZE = 500
FPS = 10
COLORS = {
    "BACKGROUND" : (25,1,33),
    "SNAKE" : (70,4,121),
    "FOOD" : (140,45,143)
}


# Setup
pygame.init()
window = pygame.display.set_mode((SIZE,SIZE))
window.fill(COLORS["BACKGROUND"])
clock = pygame.time.Clock()
pygame.display.set_caption("Snake 🐍")


# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit game when window is closed
            pygame.quit()
            quit()
    pygame.display.update()
    clock.tick(FPS)