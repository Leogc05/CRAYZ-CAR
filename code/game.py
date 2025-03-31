# game.py

import random
import pygame
import sys
from code.const import WIN_X, WIN_Y

# Inicialização do Pygame
pygame.init()
pygame.mixer.init()  # Inicializa o mixer de áudio

# Configuração da tela
screen = pygame.display.set_mode((WIN_X, WIN_Y))
pygame.display.set_caption('CRAZY CITY')

# Som do jogo
pygame.mixer_music.load('./asset/gamesound.mp3')
pygame.mixer_music.play(-1)

# Imagem de explosão
explosion = pygame.image.load('asset/explosion.png').convert_alpha()

# Som de colisão
collision_sound = pygame.mixer.Sound('./asset/collision.flac')

# Constantes para tamanho das imagens
CAR_WIDTH, CAR_HEIGHT = 100, 100

# Carregar imagens
bg = pygame.image.load('asset/city.png').convert_alpha()
bg = pygame.transform.scale(bg, (WIN_X, WIN_Y))

# Carro inimigo
enemy = pygame.image.load('asset/police.png').convert_alpha()
enemy = pygame.transform.scale(enemy, (CAR_WIDTH, CAR_HEIGHT))

# Jogador
player = pygame.image.load('ASSET/uber.png').convert_alpha()
player = pygame.transform.scale(player, (CAR_WIDTH, CAR_HEIGHT))


# Função para iniciar o jogo
def start_game(menu):
    pos_player_x = 16
    pos_player_y = 456
    pos_enemy_x = 785  # Posição inicial do inimigo
    pos_enemy_y = 476  # Posição inicial do inimigo
    player_speed = 0.5
    enemy_speed = 0.3
    bg_x = 0  # Inicialização do movimento do fundo

    # Inicialização da variável para controlar a explosão
    collision_played = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movimento do fundo
        bg_x -= 0.2  # Controla a velocidade de movimento do fundo
        if bg_x <= -WIN_X:  # Se o fundo ultrapassar a tela, volta à posição inicial
            bg_x = 0

        # Desenhar o fundo
        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x + WIN_X, 0))  # Fundo repetido

        # Movimentação do jogador
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and pos_player_y > 448:
            pos_player_y -= player_speed
        if key[pygame.K_DOWN] and pos_player_y < 665 - 100:
            pos_player_y += player_speed
        if key[pygame.K_LEFT] and pos_player_x > 0:
            pos_player_x -= player_speed
        if key[pygame.K_RIGHT] and pos_player_x < 837 - 100:
            pos_player_x += player_speed

        # Impedir o jogador de sair da tela
        pos_player_x = max(0, min(WIN_X - CAR_WIDTH, pos_player_x))
        pos_player_y = max(0, min(WIN_Y - CAR_HEIGHT, pos_player_y))

        # Movimentação do inimigo
        pos_enemy_x -= enemy_speed
        if pos_enemy_x < -100:
            pos_enemy_x = 839
            pos_enemy_y = random.randint(448, 665 - 100)

        # Criar retângulos para detectar colisão
        pygame.Rect(pos_player_x, pos_player_y, CAR_WIDTH, CAR_HEIGHT)
        pygame.Rect(pos_enemy_x, pos_enemy_y, CAR_WIDTH, CAR_HEIGHT)

        # Verificar colisão
        if (
            abs(pos_player_x - pos_enemy_x) < CAR_WIDTH  # Checando colisão horizontal
            and abs(pos_player_y - pos_enemy_y) < 10  # Permite apenas colisões na mesma linha
        ):
            if not collision_played:
                collision_sound.play()  # Toca o som de colisão uma vez
                collision_played = True  # Marca que o som foi tocado

            # Espera um momento para o som de colisão
            pygame.time.delay(int(collision_sound.get_length() * 1000))  # Aguarda o tempo do som

            running = False  # Encerra o jogo após a colisão

        # Desenhar elementos na tela
        screen.blit(enemy, (pos_enemy_x, pos_enemy_y))  # O inimigo continua na tela
        if pos_player_x >= 0 and pos_player_y >= 0:  # Verifica se o jogador não foi removido
            screen.blit(player, (pos_player_x, pos_player_y))  # O jogador será removido após a colisão

        # Atualizar a tela
        pygame.display.update()

    # Após o jogo terminar, voltar para o menu
    menu()  # Chama a função do menu após o jogo terminar
