import pygame
import sys
import random

pygame.init()

game_font = pygame.font.Font(None, 30)
game_over_font = pygame.font.Font(None, 120)

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Shooter game")

fighter_image = pygame.image.load('images/fighter.png')
fighter_width, fighter_height = fighter_image.get_size()
fighter_x, fighter_y = (screen_width - fighter_width) / 2, screen_height - fighter_height
fighter_step = 1.1
fighter_is_moving_left, fighter_is_moving_right = False, False

rocket_image = pygame.image.load('images/rocket.png')
rocket_width, rocket_height = rocket_image.get_size()
rocket_x, rocket_y = 0, 0
rocket_fired = False
rocket_step = 1.5

alien_image = pygame.image.load('images/alien.png')
alien_width, alien_height = alien_image.get_size()
alien_killed = False
ALIEN_STEP = 0.2
alien_speed = ALIEN_STEP
alien_x, alien_y = random.randint(0, screen_width - alien_width), 0

fill_color = (32, 52, 71)
game_score = 0
run_game = True

while run_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = True
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = True
            if event.key == pygame.K_SPACE:
                rocket_fired = True
                rocket_x = fighter_x + (fighter_width - rocket_width) / 2
                rocket_y = fighter_y - rocket_height
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = False
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = False

    if fighter_is_moving_left and fighter_x >= fighter_step:
        fighter_x -= fighter_step

    if fighter_is_moving_right and fighter_x <= screen_width - fighter_width - fighter_step:
        fighter_x += fighter_step
    alien_y += ALIEN_STEP
    # if rocket_fired and rocket_y <= screen_width - rocket_width - rocket_step:
    #     rocket_y -= rocket_step

    if rocket_fired and rocket_y + rocket_height < 0:
        rocket_fired = False

    if rocket_fired and rocket_y <= screen_width - rocket_width - rocket_step:
        rocket_y -= rocket_step

    screen.fill(fill_color)
    screen.blit(fighter_image, (fighter_x, fighter_y))
    screen.blit(alien_image, (alien_x, alien_y))

    if rocket_fired:
        screen.blit(rocket_image, (rocket_x, rocket_y))

    game_score_text = game_font.render(f"score: {game_score}", True, 'yellow')
    screen.blit(game_score_text, (700, 20))
    pygame.display.update()

    if alien_y + alien_height > fighter_y:
        run_game = False

    if rocket_fired and \
            alien_x < rocket_x < alien_x + alien_width + rocket_width and \
            alien_y < rocket_y < alien_y + alien_height - rocket_height:
        rocket_fired = False
        alien_x, alien_y = random.randint(0, screen_width - alien_width), 0
        alien_speed += ALIEN_STEP / 2
        game_score += 1

game_over_text = game_over_font.render("Game over!", True, 'yellow')
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (screen_width / 2, screen_height / 2)
screen.blit(game_over_text, game_over_rect)
pygame.display.update()
pygame.time.wait(5000)

pygame.quit()
