import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
GROUND_HEIGHT = SCREEN_HEIGHT - 70
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Endless Runner')

# Load images
dino_img = pygame.image.load('dino.png')
cactus_img = pygame.image.load('cactus.png')
background_img = pygame.image.load('background.png')

# Dino class
class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = dino_img
        self.rect = self.image.get_rect()
        self.rect.y = GROUND_HEIGHT
        self.jumping = False
        self.jump_speed = 20
        self.gravity = 1
        self.speed = self.jump_speed

    def update(self):
        if self.jumping:
            self.rect.y -= self.speed
            self.speed -= self.gravity
            if self.speed < -self.jump_speed:
                self.jumping = False
                self.rect.y = GROUND_HEIGHT
                self.speed = self.jump_speed

    def jump(self):
        if not self.jumping:
            self.jumping = True

# Cactus class
class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = cactus_img
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = GROUND_HEIGHT

    def update(self):
        self.rect.x -= 10
        if self.rect.x < -self.rect.width:
            self.rect.x = SCREEN_WIDTH + random.randint(0, 1000)

# Sprite groups
all_sprites = pygame.sprite.Group()
cacti = pygame.sprite.Group()

dino = Dino()
all_sprites.add(dino)

for _ in range(5):
    cactus = Cactus()
    all_sprites.add(cactus)
    cacti.add(cactus)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                dino.jump()

    all_sprites.update()

    # Check for collisions
    if pygame.sprite.spritecollideany(dino, cacti):
        running = False

    # Draw everything
    screen.fill(WHITE)
    screen.blit(background_img, (0, 0))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS) 

pygame.quit()
