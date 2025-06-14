import pygame, sys
from settings import *
from assets import *

def draw_menu(screen, show_tutorial_hint=True):
    screen.fill(BLACK)
    title = FONT.render("Conquistador", True, WHITE)
    start = FONT.render("Comenzar [ESPACIO]", True, BLUE)
    screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//3))
    screen.blit(start, (WIDTH//2 - start.get_width()//2, HEIGHT//2))
    if show_tutorial_hint:
        tutorial = FONT.render("Tutorial [T]", True, WHITE)
        screen.blit(tutorial, (WIDTH//2 - tutorial.get_width()//2, HEIGHT//2 + 60))
    pygame.display.flip()


def draw_game(screen, player_rect, enemies, score, potions):
    screen.fill(BLACK)
    screen.blit(player_img, player_rect)
    for enemy in enemies:
        screen.blit(enemy_imgs[enemy["type"]], enemy["rect"])
    # Draw potions
    for potion in potions:
        color = BLUE if potion["type"] == "blue" else RED
        pygame.draw.circle(screen, color, (potion["rect"].centerx, potion["rect"].centery), potion["rect"].width // 2)
    # Score (left)
    score_text = FONT.render(f"Puntaje: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    # Pause [ESC] (right)
    pause_text = FONT.render("Pausar [ESC]", True, WHITE)
    screen.blit(pause_text, (WIDTH - pause_text.get_width() - 10, 10))
    pygame.display.flip()

def game_over_screen(screen, score):
    screen.fill(BLACK)
    over = FONT.render("Fin del Juego!", True, RED)
    score_text = FONT.render(f"Puntaje: {score}", True, WHITE)
    restart = FONT.render("Presione R para Reiniciar", True, BLUE)
    screen.blit(over, (WIDTH//2 - over.get_width()//2, HEIGHT//3))
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2))
    screen.blit(restart, (WIDTH//2 - restart.get_width()//2, HEIGHT//2 + 50))
    pygame.display.flip()

def draw_tutorial(screen, slide):
    slides = [
        [
            "Eres un Conquistador valiente!",
            "Tu deber: sobrevive al",
            "atacar del enemigo",
            "y conquista las tierras lejanas!",
            "",
            "-> FLECHA DERECHA"
        ],
        [
            "Hay 3 tipos de enemigos:",
            "- Euler: Simple y lento.",
            "- Gauss: Se mueve en diagonal, ",
            "pero más rápido.",
            "- Newton: Impredecible,",
            "y muy pero muy rápido!",
            "La dificultad aumenta mientras",
            "avanzas.",
            "",
            " <- Flecha IZQ/DER -> para navegar"
        ],
        [
            "Las pociones cambian tu aspecto!",
            "- Poción Azul: te reduce en 8%.",
            "- Poción Roja: creces un 8%.",
            "",
            "Presiona T para salir"
        ]
    ]
    # Modal background
    modal_width, modal_height = WIDTH-60, HEIGHT-200
    modal = pygame.Surface((modal_width, modal_height))
    modal.set_alpha(230)
    modal.fill((30, 30, 30))
    screen.blit(modal, (30, 100))

    # Use a smaller font for tutorial text
    tutorial_font = pygame.font.SysFont("consolas", 22)
    y = 130 + 20  # Start a bit lower inside the modal
    for line in slides[slide]:
        text = tutorial_font.render(line, True, WHITE)
        screen.blit(text, (WIDTH//2 - text.get_width()//2, y))
        y += 32  # Slightly smaller spacing for more lines
    pygame.display.flip()

def show_tutorial(screen):
    slide = 0
    total_slides = 3
    while True:
        draw_tutorial(screen, slide)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and slide < total_slides-1:
                    slide += 1
                elif event.key == pygame.K_LEFT and slide > 0:
                    slide -= 1
                elif event.key == pygame.K_t and slide == total_slides-1:
                    return
                elif event.key == pygame.K_t and slide != total_slides-1:
                    # Allow closing tutorial from any slide
                    return

def draw_pause_menu(screen):
    modal = pygame.Surface((WIDTH-100, HEIGHT-300))
    modal.set_alpha(240)
    modal.fill((50, 50, 50))
    screen.blit(modal, (50, 150))
    pause = FONT.render("PAUSADO", True, BLUE)
    resume = FONT.render("Continuar [G]", True, WHITE)
    restart = FONT.render("Reiniciar [R]", True, WHITE)
    screen.blit(pause, (WIDTH//2 - pause.get_width()//2, 200))
    screen.blit(resume, (WIDTH//2 - resume.get_width()//2, 300))
    screen.blit(restart, (WIDTH//2 - restart.get_width()//2, 350))
    pygame.display.flip()

def pause_menu(screen):
    while True:
        draw_pause_menu(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    return "resume"
                elif event.key == pygame.K_r:
                    return "restart"