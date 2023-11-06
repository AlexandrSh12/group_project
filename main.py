import pygame
from pathlib import Path
from all_graphics import background, start_menu, victory, score_text, hog_logo, hp, end_menu, dementor, owls, clans, death_eater
from all_sound import hit_sound, hit_enemy_sound, click, victory_sound, end_menu_sound, shoot_sound, main_theme
from helpers.Explosion import Explosion
from helpers.Enemy import Enemy
from helpers.Player import Player
from helpers.Bullet import Bullet
from vars import WIDTH, HEIGHT, FPS

DIR_PATH = Path.cwd()

main_theme.play()

# Создаем игру и окно
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Гарри Поттер")
clock = pygame.time.Clock()
game_over = True
running = True
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
all_sprites.add(bullets)
enemy = pygame.sprite.Group()
death = pygame.sprite.Group()
dem = pygame.sprite.Group()
sov = pygame.sprite.Group()
cl = pygame.sprite.Group()
score = 0

def create_dementor():
    dementor_tmp = Enemy([dementor], [6, 8], [-4, 4])
    all_sprites.add(dementor_tmp)
    dem.add(dementor_tmp)

def create_owl():
    owl_tmp = Enemy(owls, [2, 4])
    all_sprites.add(owl_tmp)
    sov.add(owl_tmp)

def create_clans():
    clans_tmp = Enemy(clans, [3, 5])
    all_sprites.add(clans_tmp)
    cl.add(clans_tmp)

def create_death_eater():
    death_eater_tmp = Enemy([death_eater], [5, 7], [-2, 2])
    all_sprites.add(death_eater_tmp)
    death.add(death_eater_tmp)

def new_enemy():
    create_dementor()
    create_owl()
    create_clans()
    create_death_eater()

# универсальная функция для вывода любого текста на экран
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(Path(DIR_PATH, "resources", "fonts", "font.ttf"), size)
    text_surface = font.render(text, True, "yellow")
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# функция вывода стартового меню
def show_go_screen():
    screen.blit(start_menu, start_menu.get_rect()) # загрузка картинки
    pygame.display.flip()
    waiting = True
    # pygame.mixer.music.play(loops=-1)
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # выход из игры
                pygame.quit()
            if event.type == pygame.KEYDOWN: # если нажалась любая клавиша - игра началась
                click.play()
                waiting = False
                # pygame.mixer.music.stop() # музыка в меню остановилась, пошла музыка геймплея
                # pygame.mixer.music.play(loops=-1)
                # pygame.mixer.music.set_volume(0.2)

def show_out_screen():
    draw_text(screen, str(score), 60, WIDTH / 1.4, HEIGHT / 1.75)
    pygame.mixer.music.stop() # остановка всего звука
    hit_sound.stop()
    hit_enemy_sound.stop()
    shoot_sound.stop()
    
    if score >= 1000: # если набрано необходимое количество очков, вывод победного экрана
        screen.blit(victory, victory.get_rect()) #
        victory_sound.play() # проигрыш звука победы
    else:
        screen.blit(end_menu, end_menu.get_rect()) # если гарри умер, то вывод проигрышного экрана
        end_menu_sound.play()

    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # выход из игры
                pygame.quit()

def handle_harry_collision_with_enemy(enemy, damage):
    hits = pygame.sprite.spritecollide(player, enemy, True)
    for hit in hits:
        player.hp -= damage
        hit_sound.play()
        expl = Explosion(hit.rect.center)
        all_sprites.add(expl)
        if player.hp <= 0:
            running = False
            game_over = True
            show_out_screen()

def handle_attacks_collision_with_enemy(enemys, score_number, create_enemy_func):
    global score
    hits = pygame.sprite.groupcollide(enemys, bullets, True, True)
    for hit in hits:
        hit_enemy_sound.play()
        expl = Explosion(hit.rect.center)
        all_sprites.add(expl)
        print(score)
        score += score_number
        create_enemy_func()

for i in range(6):
    new_enemy()

while running:
    if game_over:
        show_go_screen()
        game_over = False
        all_sprites = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        all_sprites.add(bullets)
        enemy = pygame.sprite.Group()
        death = pygame.sprite.Group()
        dem = pygame.sprite.Group()
        sov = pygame.sprite.Group()
        cl = pygame.sprite.Group()
        score = 0
        for i in range(6):
            new_enemy()

    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.right, player.rect.centery)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()

    # Обновление
    all_sprites.update()

    # Столкновения персонажа с противниками
    handle_harry_collision_with_enemy(dem, 20)
    handle_harry_collision_with_enemy(sov, 10)
    handle_harry_collision_with_enemy(cl, 10)
    handle_harry_collision_with_enemy(death, 40)

    # Персонаж попал в противника
    handle_attacks_collision_with_enemy(dem, 20, create_dementor)
    handle_attacks_collision_with_enemy(cl, 10, create_clans)
    handle_attacks_collision_with_enemy(sov, 20, create_owl)
    handle_attacks_collision_with_enemy(death, 30, create_death_eater)

    if score >= 1000:
        show_out_screen()
        victory_sound.play()
        running = False
        game_over = True

    # Рендеринг
    screen.blit(background, background.get_rect())
    screen.blit(score_text, score_text.get_rect(center=(WIDTH - 700, 50)))
    screen.blit(hog_logo, hog_logo.get_rect(center=(WIDTH - 825, 50)))
    screen.blit(hp, hp.get_rect(center=(WIDTH - 180, 50)))
    all_sprites.draw(screen)
    draw_text(screen, str(score), 48, WIDTH - 550, 27)
    draw_text(screen, str(player.hp), 48, WIDTH - 80, 27)
    draw_text(screen, "ЦЕЛЬ:1000", 48, 180, HEIGHT - 75)

    # После отрисовки всего, обновляем экран
    pygame.display.flip()

pygame.quit()