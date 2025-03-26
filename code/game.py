import pygame

pygame.init()

from code.const import WIN_X, WIN_Y

# Configuração da tela
screen = pygame.display.set_mode((WIN_X, WIN_Y))
pygame.display.set_caption('CRAZY CITY')

# Som do jogo
pygame.mixer_music.load('./asset/gamesound.mp3')
pygame.mixer_music.play(-1)

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

# Posições iniciais
pos_player_x = 16
pos_player_y = 456
pos_enemy_x = 785  # Posição inicial do inimigo
pos_enemy_y = 476  # Posição inicial do inimigo

# Velocidades (controle de movimento)
player_speed = 0.5
enemy_speed = 0.3

# Variável para o movimento do fundo
bg_x = 0

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

    # Movimentação do jogador (ajuste conforme necessário)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pos_player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        pos_player_x += player_speed
    if keys[pygame.K_UP]:
        pos_player_y -= player_speed
    if keys[pygame.K_DOWN]:
        pos_player_y += player_speed

    # Impedir o jogador de sair da tela
    pos_player_x = max(0, min(WIN_X - CAR_WIDTH, pos_player_x))
    pos_player_y = max(0, min(WIN_Y - CAR_HEIGHT, pos_player_y))

    # Movimentação do inimigo
    pos_enemy_x -= enemy_speed  # O inimigo se move da direita para a esquerda
    if pos_enemy_x < -CAR_WIDTH:  # Reaparece do lado direito após sair da tela
        pos_enemy_x = WIN_X

    # Criar imagens
    screen.blit(enemy, (pos_enemy_x, pos_enemy_y))
    screen.blit(player, (pos_player_x, pos_player_y))

    pygame.display.update()  # Atualizar a tela
