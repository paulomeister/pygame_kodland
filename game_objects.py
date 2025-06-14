import pygame, random
from settings import AVATAR_SIZE, WIDTH, HEIGHT

def spawn_enemy(enemies, score):
    # Enemy One: 0-2000
    # Enemy Two: 2000-4000
    # Enemy Three: 4000-5500
    # Beyond 5500: all enemies
    if score < 2000:
        # Spawn enemy one
        enemy = {
            "rect": pygame.Rect(random.randint(0, WIDTH-AVATAR_SIZE), -AVATAR_SIZE, AVATAR_SIZE, AVATAR_SIZE),
            "type": "one",
            "vx": 0,
            "vy": 5
        }
        enemies.append(enemy)
    elif 2000 <= score < 4000:
        # Spawn enemy two
        count = 1
        if score >= 3000:
            count = 2
        for _ in range(count):
            vx = random.choice([-1, 1]) * random.randint(2, 3)
            vy = random.randint(4, 6)  # Reduced speed
            enemy = {
                "rect": pygame.Rect(random.randint(0, WIDTH-AVATAR_SIZE), -AVATAR_SIZE, AVATAR_SIZE, AVATAR_SIZE),
                "type": "two",
                "vx": vx,
                "vy": vy
            }
            enemies.append(enemy)
    elif 4000 <= score < 5500:
        # Spawn enemy three
        for _ in range(1, 2):  # Only 1 enemy three per spawn
            move_type = random.choice(["vertical", "diagonal"])
            if move_type == "vertical":
                vx = 0
                vy = random.choice([7, 9, 11])
            else:
                vx = random.choice([-1, 1]) * random.randint(6, 9)
                vy = random.randint(7, 11)
            enemy = {
                "rect": pygame.Rect(random.randint(0, WIDTH-AVATAR_SIZE), -AVATAR_SIZE, AVATAR_SIZE, AVATAR_SIZE),
                "type": "three",
                "vx": vx,
                "vy": vy
            }
            enemies.append(enemy)
    elif score >= 5500:
        # Spawn all enemies
        # One enemy three
        for _ in range(1):
            move_type = random.choice(["vertical", "diagonal"])
            if move_type == "vertical":
                vx = 0
                vy = random.choice([7, 9, 11])
            else:
                vx = random.choice([-1, 1]) * random.randint(6, 9)
                vy = random.randint(7, 11)
            enemy = {
                "rect": pygame.Rect(random.randint(0, WIDTH-AVATAR_SIZE), -AVATAR_SIZE, AVATAR_SIZE, AVATAR_SIZE),
                "type": "three",
                "vx": vx,
                "vy": vy
            }
            enemies.append(enemy)
        # One enemy one
        enemy = {
            "rect": pygame.Rect(random.randint(0, WIDTH-AVATAR_SIZE), -AVATAR_SIZE, AVATAR_SIZE, AVATAR_SIZE),
            "type": "one",
            "vx": 0,
            "vy": 5
        }
        enemies.append(enemy)
        # One enemy two
        for _ in range(1):
            vx = random.choice([-1, 1]) * random.randint(2, 3)
            vy = random.randint(4, 6)
            enemy = {
                "rect": pygame.Rect(random.randint(0, WIDTH-AVATAR_SIZE), -AVATAR_SIZE, AVATAR_SIZE, AVATAR_SIZE),
                "type": "two",
                "vx": vx,
                "vy": vy
            }
            enemies.append(enemy)

def move_enemies(enemies):
    for enemy in enemies:
        enemy["rect"].x += enemy["vx"]
        enemy["rect"].y += enemy["vy"]
        # Keep enemies within screen horizontally
        if enemy["rect"].left < 0 or enemy["rect"].right > WIDTH:
            enemy["vx"] *= -1

def check_collision(player_rect, enemies):
    for enemy in enemies:
        if player_rect.colliderect(enemy["rect"]):
            return True
    return False

def spawn_potion(potions, potion_type):
    # Potions are circles, size 24x24
    size = 24
    potion = {
        "rect": pygame.Rect(random.randint(0, WIDTH-size), -size, size, size),
        "type": potion_type,
        "vy": 4
    }
    potions.append(potion)

def move_potions(potions):
    for potion in potions:
        potion["rect"].y += potion["vy"]

def check_potion_collision(player_rect, potions):
    for i, potion in enumerate(potions):
        if player_rect.colliderect(potion["rect"]):
            return i
    return -1