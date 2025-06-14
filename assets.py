import pygame, os
from settings import AVATAR_SIZE

# Load avatars
AVATAR_PATH = os.path.join(os.path.dirname(__file__), "avatars")
player_img = pygame.image.load(os.path.join(AVATAR_PATH, "player.png"))
player_img = pygame.transform.scale(player_img, (AVATAR_SIZE, AVATAR_SIZE))
enemy_imgs = {
    "one": pygame.transform.scale(pygame.image.load(os.path.join(AVATAR_PATH, "enemy_one.png")), (AVATAR_SIZE, AVATAR_SIZE)),
    "two": pygame.transform.scale(pygame.image.load(os.path.join(AVATAR_PATH, "enemy_two.png")), (AVATAR_SIZE, AVATAR_SIZE)),
    "three": pygame.transform.scale(pygame.image.load(os.path.join(AVATAR_PATH, "enemy_three.png")), (AVATAR_SIZE, AVATAR_SIZE)),
}

FONT = pygame.font.SysFont("consolas", 28)