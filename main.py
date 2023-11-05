import pygame
from all_graphics import explosion_anim, background, start_menu, victory, score_text, hog_logo, hp, end_menu, dementor, owls, clans, death_eater
from all_sound import hit_sound, hit_enemy_sound, click, victory_sound, end_menu_sound, shoot_sound, main_theme
from helpers.Explosion import Explosion
from helpers.Enemy import Enemy
from helpers.Player import Player
from helpers.Bullet import Bullet

WIDTH = 1200
HEIGHT = 600
FPS = 60

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

def new_enemy():
    dementor_tmp = Enemy([dementor], [6, 8], [-4, 4])
    owl_tmp = Enemy(owls, [2, 4])
    clans_tmp = Enemy(clans, [3, 5])
    death_eater_tmp = Enemy(death_eater, [5, 7], [-2, 2])

    all_sprites.add(dementor_tmp)
    all_sprites.add(owl_tmp)
    all_sprites.add(clans_tmp)
    all_sprites.add(death_eater_tmp)

    dem.add(dementor_tmp)
    sov.add(owl_tmp)
    cl.add(clans_tmp)
    death.add(death_eater_tmp)

# универсальная функция для вывода любого текста на экран
def draw_text(surf, text, size, x, y):
    font_name = pygame.font.match_font('VCROSDMonoRUSbyD')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, "yellow")
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# функция вывода стартового меню
def show_go_screen():
    screen.blit(start_menu, start_menu.get_rect()) # загрузка картинки
    pygame.display.flip()
    waiting = True
    pygame.mixer.music.play(loops=-1)
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # выход из игры
                pygame.quit()
            if event.type == pygame.KEYDOWN: # если нажалась любая клавиша - игра началась
                click.play()
                waiting = False
                pygame.mixer.music.stop() # музыка в меню остановилась, пошла музыка геймплея
                pygame.mixer.music.play(loops=-1)
                pygame.mixer.music.set_volume(0.2)

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