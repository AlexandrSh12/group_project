import pygame
from pathlib import Path

DIR_PATH = Path.cwd()

def load_image(path, scale = None):
    obj = pygame.image.load(Path(DIR_PATH, "graphics", path))
    if scale != None:
        pygame.transform.scale(end_menu, scale)

    return obj

# добавление всей основной графики в код
background = load_image("уровень.jpg")
garry = load_image("гарри.png")
start_menu =load_image("старт.png")
end_menu = load_image("конец.png", (1200, 600))
victory = load_image("выигрыш.png", (1200, 600))
score_text = load_image("счет.png", (130, 50))
hog_logo = load_image("логотип хогвартса.png", (80, 80))
hp = load_image("хп.png", (100, 80))

# загрузка анимации взрыва противника
explosion_anim = []
for i in range(12):
    img = load_image("пух{}.png".format(i), (156, 156))
    img.set_colorkey("black")
    explosion_anim.append(img)

# загрузка всех видов врагов
dementor = load_image("дементор.png")
pojirateli = []
sova = []
clans = []
piu = []

for filename in ["пожиратель .png", "пожиратель1.png"]:
    pojirateli.append(load_image(filename))

for filename in ["сова1.png", "сова2.png", "сова3.png"]:
    sova.append(load_image(filename))

for filename in ["когтевран.png", "пуффендуй.png", "слизерин.png"]:
    clans.append(load_image(filename))

# загрузка анимации попадания
for filename in ["пиу.png", "пиу1.png", "пиу2.png", "пиу3.png", "пиу4.png"]:
    piu.append(load_image(filename))