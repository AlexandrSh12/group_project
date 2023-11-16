import pygame
import sys
from all_resources import background, start_menu, victory, score_text, hog_logo, hp, end_menu, dementor, owls, clans, death_eater, again_btn, quit_btn
from all_resources import hit_sound, hit_enemy_sound, click, victory_sound, end_menu_sound, shoot_sound
from all_resources import load_font
from helpers.Explosion import Explosion
from helpers.Enemy import Enemy
from helpers.Player import Player
from helpers.Bullet import Bullet
from helpers.Button import Button
from helpers.MaxScoreCounter import MaxScoreCounter
from helpers.MainTheme import MainTheme
from vars import WIDTH, HEIGHT, FPS, MAX_SCORE

# Создаем игру и окно
pygame.init()
pygame.display.set_caption("Гарри Поттер")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
max_score_counter = MaxScoreCounter()
main_theme = MainTheme()


def create_dementor():
    dementor_tmp = Enemy([dementor], [6, 8], [-4, 4])
    all_sprites.add(dementor_tmp)
    dementors_group.add(dementor_tmp)

def create_owl():
    owl_tmp = Enemy(owls, [2, 4])
    all_sprites.add(owl_tmp)
    owls_group.add(owl_tmp)

def create_clans():
    clans_tmp = Enemy(clans, [3, 5])
    all_sprites.add(clans_tmp)
    clans_group.add(clans_tmp)

def create_death_eater():
    death_eater_tmp = Enemy([death_eater], [5, 7], [-2, 2])
    all_sprites.add(death_eater_tmp)
    death_eaters_group.add(death_eater_tmp)

def new_enemy():
    create_dementor()
    create_owl()
    create_clans()
    create_death_eater()

# универсальная функция для вывода любого текста на экран
def draw_text(surf, text, size, x, y):
    font = load_font(size)
    text_surface = font.render(text, True, "yellow")
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# функция вывода стартового меню
def show_go_screen():
    screen.blit(start_menu, start_menu.get_rect()) # загрузка картинки
    draw_text(screen, f'Лучший счёт: {max_score_counter.getMaxScore()}', 35, 250, HEIGHT / 1.5)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # выход из игры
                quit_game()
            if event.type == pygame.KEYDOWN: # если нажалась любая клавиша - игра началась
                click.play()
                waiting = False

# функция выхода из игры
def quit_game():
    global waiting, running

    waiting = False
    running = False
    pygame.quit()
    sys.exit()

# функция вывода меню выигрыша или проигрыша
def show_out_screen(isVictory):
    global score, waiting, max_score_counter

    max_score_counter.updateMaxScore(min(score, MAX_SCORE))
    main_theme.stop()
    hit_sound.stop()
    hit_enemy_sound.stop()
    shoot_sound.stop()
    
    if isVictory:
        screen.blit(victory, victory.get_rect())
        victory_sound.play()
    else:
        screen.blit(end_menu, end_menu.get_rect())
        draw_text(screen, str(score), 60, WIDTH / 1.45, HEIGHT / 2.3)
        end_menu_sound.play()

    group = pygame.sprite.Group()
    again_btn_obj = Button(again_btn, again_btn.get_rect(center=(WIDTH / 3 - 50, HEIGHT / 1.35)), set_up_playground)
    quit_btn_obj = Button(quit_btn, quit_btn.get_rect(center=(WIDTH / 1.5 + 50, HEIGHT / 1.35)), quit_game)
    group.add(again_btn_obj, quit_btn_obj)
    
    group.draw(screen)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        event_list = pygame.event.get()
        for event in event_list:
            
            if event.type == pygame.QUIT:
                quit_game()

        group.update(event_list)

# функция обработки столкновения игрока с противником
def handle_harry_collision_with_enemy(enemy, damage):
    hits = pygame.sprite.spritecollide(player, enemy, True)
    for hit in hits:
        player.hp -= damage
        hit_sound.play()
        expl = Explosion(hit.rect.center)
        all_sprites.add(expl)

# функция обработки попадания игрока по противнику
def handle_attacks_collision_with_enemy(enemys, score_number, create_enemy_func):
    global score
    hits = pygame.sprite.groupcollide(enemys, bullets, True, True)
    for hit in hits:
        hit_enemy_sound.play()
        expl = Explosion(hit.rect.center)
        all_sprites.add(expl)
        score += score_number
        create_enemy_func()

# функция подготовки игрового поля
def set_up_playground():
    global game_over, running, waiting, all_sprites, bullets, player, death_eaters_group, dementors_group, owls_group, clans_group, score
    game_over = True
    running = True
    waiting = False
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    all_sprites.add(bullets)
    death_eaters_group = pygame.sprite.Group()
    dementors_group = pygame.sprite.Group()
    owls_group = pygame.sprite.Group()
    clans_group = pygame.sprite.Group()
    score = 0
    main_theme.play()

    for i in range(6):
        new_enemy()

set_up_playground()
show_go_screen()
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)

    for event in pygame.event.get():
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
    handle_harry_collision_with_enemy(dementors_group, 20)
    handle_harry_collision_with_enemy(owls_group, 10)
    handle_harry_collision_with_enemy(clans_group, 10)
    handle_harry_collision_with_enemy(death_eaters_group, 40)

    # Персонаж попал в противника
    handle_attacks_collision_with_enemy(dementors_group, 20, create_dementor)
    handle_attacks_collision_with_enemy(clans_group, 10, create_clans)
    handle_attacks_collision_with_enemy(owls_group, 20, create_owl)
    handle_attacks_collision_with_enemy(death_eaters_group, 30, create_death_eater)

    if score >= MAX_SCORE:
        show_out_screen(True)
    
    if player.hp <= 0:
        show_out_screen(False)

    # Рендеринг
    screen.blit(background, background.get_rect())
    screen.blit(score_text, score_text.get_rect(center=(WIDTH - 700, 50)))
    screen.blit(hog_logo, hog_logo.get_rect(center=(WIDTH - 825, 50)))
    screen.blit(hp, hp.get_rect(center=(WIDTH - 180, 50)))
    all_sprites.draw(screen)
    draw_text(screen, str(score), 48, WIDTH - 550, 27)
    draw_text(screen, str(player.hp), 48, WIDTH - 80, 27)
    draw_text(screen, f'ЦЕЛЬ:{MAX_SCORE}', 48, 180, HEIGHT - 75)

    pygame.display.flip()

quit_game()