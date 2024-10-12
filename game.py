import pygame
import os
import random

# Initialize pygame
pygame.init()

# Set window dimensions
WIDTH, HEIGHT = 2000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship Game")

# Define a border in the middle of the screen
BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

# Load images
GREY_SPACE_SHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_c.png'))
RED_SPACE_SHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'SpaceshipR.png'))
BACKGROUND_IMAGE = pygame.image.load(os.path.join('Assets', 'background.jpg'))

# Scale background to cover full screen
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))

# Load sounds
GUNSHOT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+silencer.mp3'))
DEATH_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
  # Load background music

# Set velocities, FPS, and bullet properties
VEL = 5
FPS = 60
MAX_BULLETS = 3
BULLET_VEL = 10
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 200, 150

# Lives
GREY_LIVES = 3
RED_LIVES = 3

# Fonts
FONT = pygame.font.SysFont('comicsans', 50)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

# Transform images (scale and rotate)
GREY_SPACE_SHIP = pygame.transform.rotate(
    pygame.transform.scale(GREY_SPACE_SHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
RED_SPACE_SHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACE_SHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

# Particle class for explosions
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(5, 10)
        self.color = (255, 165, 0)  # Orange
        self.lifetime = random.randint(30, 60)

    def draw(self):
        pygame.draw.circle(WIN, self.color, (self.x, self.y), self.size)

    def update(self):
        self.y -= random.randint(1, 3)  # Move particles up
        self.size -= 0.1  # Decrease size
        self.lifetime -= 1  # Decrease lifetime

def draw_window(red, grey, greybullets, redbullets, grey_lives, red_lives, particles):
    WIN.blit(BACKGROUND, (0, 0))  # Draw background
    pygame.draw.rect(WIN, (0, 0, 0), BORDER)  # Draw the border
    WIN.blit(GREY_SPACE_SHIP, (grey.x, grey.y))  # Draw grey spaceship
    WIN.blit(RED_SPACE_SHIP, (red.x, red.y))  # Draw red spaceship

    # Display lives
    grey_lives_text = FONT.render("Lives: " + str(grey_lives), 1, (255, 255, 255))
    red_lives_text = FONT.render("Lives: " + str(red_lives), 1, (255, 255, 255))
    WIN.blit(grey_lives_text, (10, 10))
    WIN.blit(red_lives_text, (WIDTH - red_lives_text.get_width() - 10, 10))

    # Draw bullets
    for bullet in greybullets:
        pygame.draw.rect(WIN, (255, 0, 0), bullet)
    for bullet in redbullets:
        pygame.draw.rect(WIN, (0, 0, 255), bullet)

    # Draw particles
    for particle in particles:
        particle.draw()

    pygame.display.update()  # Update the display


def grey_handle_movement(keys_pressed, grey):
    if keys_pressed[pygame.K_a] and grey.x - VEL > 0:  # left
        grey.x -= VEL
    if keys_pressed[pygame.K_d] and grey.x + VEL < BORDER.x - SPACESHIP_WIDTH:  # right
        grey.x += VEL
    if keys_pressed[pygame.K_w] and grey.y - VEL > 0:  # up
        grey.y -= VEL
    if keys_pressed[pygame.K_s] and grey.y + VEL < HEIGHT - SPACESHIP_HEIGHT:  # down
        grey.y += VEL


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL < WIDTH - SPACESHIP_WIDTH:  # right
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # up
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL < HEIGHT - SPACESHIP_HEIGHT:  # down
        red.y += VEL


def handle_bullets(greybullets, redbullets, grey, red, particles):
    for bullet in greybullets:
        bullet.x += BULLET_VEL
        if bullet.x > WIDTH:  # Remove bullet if off-screen
            greybullets.remove(bullet)
        elif red.colliderect(bullet):  # Collision with red spaceship
            pygame.event.post(pygame.event.Event(RED_HIT))
            greybullets.remove(bullet)

    for bullet in redbullets:
        bullet.x -= BULLET_VEL
        if bullet.x < 0:  # Remove bullet if off-screen
            redbullets.remove(bullet)
        elif grey.colliderect(bullet):  # Collision with grey spaceship
            pygame.event.post(pygame.event.Event(GREY_HIT))
            redbullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, (255, 255, 255))
    WIN.blit(draw_text, (WIDTH // 2 - draw_text.get_width() // 2, HEIGHT // 2 - draw_text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(5000)  # Pause for 5 seconds before closing

# Define custom events for spaceship hits
GREY_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

def main():
   
    red = pygame.Rect(1500, 750, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    grey = pygame.Rect(100, 750, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    greybullets = []
    redbullets = []
    grey_lives = GREY_LIVES
    red_lives = RED_LIVES
    particles = []

    clock = pygame.time.Clock()
    run = True  # Game loop condition

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():  # Handle events
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(greybullets) < MAX_BULLETS:
                    bullet = pygame.Rect(grey.x + grey.width, grey.y + grey.height // 2 - 2, 10, 5)
                    greybullets.append(bullet)
                    GUNSHOT_SOUND.play()  # Play gunshot sound

                if event.key == pygame.K_RCTRL and len(redbullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                    redbullets.append(bullet)
                    GUNSHOT_SOUND.play()  # Play gunshot sound

            if event.type == GREY_HIT:
                grey_lives -= 1
                DEATH_SOUND.play()  # Play death sound
                particles.append(Particle(grey.x + SPACESHIP_WIDTH // 2, grey.y + SPACESHIP_HEIGHT // 2))

            if event.type == RED_HIT:
                red_lives -= 1
                DEATH_SOUND.play()  # Play death sound
                particles.append(Particle(red.x + SPACESHIP_WIDTH // 2, red.y + SPACESHIP_HEIGHT // 2))

        # Update particles
        for particle in particles[:]:
            particle.update()
            if particle.lifetime <= 0 or particle.size <= 0:  # Remove if lifetime is over or size is too small
                particles.remove(particle)

        winner_text = ""
        if grey_lives <= 0:
            winner_text = "Red Wins!"

        if red_lives <= 0:
            winner_text = "Grey Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        grey_handle_movement(keys_pressed, grey)
        red_handle_movement(keys_pressed, red)

        handle_bullets(greybullets, redbullets, grey, red, particles)

        draw_window(red, grey, greybullets, redbullets, grey_lives, red_lives, particles)

    pygame.quit()

if __name__ == "__main__":
    main()
