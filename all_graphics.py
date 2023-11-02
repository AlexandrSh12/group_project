import pygame
from pathlib import Path

DIR_PATH = Path.cwd()

def load_image(path, scale = None):
    obj = pygame.image.load(Path(DIR_PATH, "resources", "graphics", path))
    if scale != None:
        pygame.transform.scale(obj, scale)

    return obj

# добавление всей основной графики в код
garry = load_image("harry.png")
background = load_image("backgrounds/level.jpg")
start_menu =load_image("backgrounds/start.png")
end_menu = load_image("backgrounds/end.png", (1200, 600))
victory = load_image("backgrounds/victory.png", (1200, 600))
score_text = load_image("misc/score.png", (130, 50))
hog_logo = load_image("misc/hogwarts_logo.png", (80, 80))
hp = load_image("misc/hp.png", (100, 80))

# загрузка анимации взрыва противника
explosion_anim = []
for i in range(12):
    img = load_image("explosion/explosion{}.png".format(i), (156, 156))
    img.set_colorkey("black")
    explosion_anim.append(img)

# загрузка всех видов врагов
dementor = load_image("enemys/dementor.png")
pojirateli = load_image("enemys/death_eaters.png")
sova = []
clans = []
piu = []

for filename in ["enemys/owl0.png", "enemys/owl1.png", "enemys/owl2.png"]:
    sova.append(load_image(filename))

for filename in ["enemys/ravenclaw.png", "enemys/hufflepuff.png", "enemys/slytherin.png"]:
    clans.append(load_image(filename))

# загрузка анимации попадания
for filename in ["attack/attack0.png", "attack/attack1.png", "attack/attack2.png", "attack/attack3.png", "attack/attack4.png"]:
    piu.append(load_image(filename))