import pygame, sys
pygame.init()

from settings import *
from assets import *
from game_objects import *
from ui import *

# Initialize Pygame

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conquistador")
clock = pygame.time.Clock()

def main():
    running = True
    in_menu = True
    while running:
        while in_menu:
            draw_menu(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        in_menu = False
                    elif event.key == pygame.K_t:
                        show_tutorial(screen)

        # Game variables
        player_size = AVATAR_SIZE
        player_rect = pygame.Rect(WIDTH//2 - player_size//2, HEIGHT - 60, player_size, player_size)
        enemies = []
        potions = []
        enemy_timer = 0
        score = 0
        game_over = False
        next_potion_score = 300
        potion_toggle = "blue"  # alternate blue/red

        while not game_over:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    action = pause_menu(screen)
                    if action == "resume":
                        continue
                    elif action == "restart":
                        in_menu = True
                        game_over = True

            # Player movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player_rect.left > 0:
                player_rect.x -= 7
            if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
                player_rect.x += 7

            # Spawn enemies
            enemy_timer += 1
            spawn_period = 30
            if score >= 2000:
                spawn_period = 25
            if score >= 4000:
                spawn_period = 20
            if enemy_timer > spawn_period:
                spawn_enemy(enemies, score)
                enemy_timer = 0

            move_enemies(enemies)
            enemies = [e for e in enemies if e["rect"].y < HEIGHT]

            # Spawn potions every 300 points, alternate blue/red, red 15 points after blue
            if score >= next_potion_score:
                if potion_toggle == "blue":
                    spawn_potion(potions, "blue")
                    potion_toggle = "red"
                    next_potion_score += 15
                else:
                    spawn_potion(potions, "red")
                    potion_toggle = "blue"
                    next_potion_score += 285  # 300 total between blue potions

            move_potions(potions)
            potions = [p for p in potions if p["rect"].y < HEIGHT]

            # Potion collision
            idx = check_potion_collision(player_rect, potions)
            if idx != -1:
                potion = potions.pop(idx)
                # Change player size by 8%
                old_center = player_rect.center
                if potion["type"] == "blue":
                    player_size = max(int(player_size * 0.92), 20)
                else:
                    player_size = min(int(player_size * 1.08), WIDTH)
                player_rect = pygame.Rect(0, 0, player_size, player_size)
                player_rect.center = old_center
                # Clamp to screen
                if player_rect.left < 0:
                    player_rect.left = 0
                if player_rect.right > WIDTH:
                    player_rect.right = WIDTH
                if player_rect.top < 0:
                    player_rect.top = 0
                if player_rect.bottom > HEIGHT:
                    player_rect.bottom = HEIGHT

            # Collision
            if check_collision(player_rect, enemies):
                game_over = True

            # Score
            score += 1

            # Draw everything
            draw_game(screen, player_rect, enemies, score, potions)

        # Game Over screen
        while game_over:
            game_over_screen(screen, score)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    in_menu = True
                    game_over = False

if __name__ == "__main__":
    main()

