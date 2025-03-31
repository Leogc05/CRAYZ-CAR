import pygame
import sys
from code.const import COLOR_BLACK, COLOR_WHITE, COLOR_GREEN
from code.game import start_game  # Importa a função de iniciar o jogo (sem depender de 'running')

# Inicializar o Pygame
pygame.init()

# Definir dimensões da tela
WIN_X = 839
WIN_Y = 679
screen = pygame.display.set_mode((WIN_X, WIN_Y))
pygame.display.set_caption("Menu do Jogo")

# Carregar imagem de fundo
bg = pygame.image.load('asset/citysky.png').convert_alpha()
bg = pygame.transform.scale(bg, (WIN_X, WIN_Y))  # Redimensionar a imagem para cobrir toda a tela

# Fontes
font = pygame.font.Font(None, 50)

# Função para desenhar o menu
def draw_menu(mouse_x, mouse_y):
    # Desenhar o fundo
    screen.blit(bg, (0, 0))  # Coloca o fundo na tela (na posição (0,0))

    # Títulos e opções
    title = font.render("CRAZY CITY", True, COLOR_BLACK)
    new_game_text = font.render("New Game", True, COLOR_WHITE)
    exit_text = font.render("Exit", True, COLOR_WHITE)

    # Verificar se o mouse está sobre o texto "New Game"
    if WIN_X // 2 - new_game_text.get_width() // 2 < mouse_x < WIN_X // 2 + new_game_text.get_width() // 2 and 300 < mouse_y < 350:
        new_game_text = font.render("New Game", True, COLOR_GREEN)  # Muda a cor para verde

    # Verificar se o mouse está sobre o texto "Exit"
    if WIN_X // 2 - exit_text.get_width() // 2 < mouse_x < WIN_X // 2 + exit_text.get_width() // 2 and 400 < mouse_y < 450:
        exit_text = font.render("Exit", True, COLOR_GREEN)  # Muda a cor para verde

    # Centralizar o texto
    screen.blit(title, (WIN_X // 2 - title.get_width() // 2, 100))
    screen.blit(new_game_text, (WIN_X // 2 - new_game_text.get_width() // 2, 300))
    screen.blit(exit_text, (WIN_X // 2 - exit_text.get_width() // 2, 400))

    pygame.display.update()

# Função para executar o menu
# Função para executar o menu
def menu():
    running_menu = True
    while running_menu:
        mouse_x, mouse_y = pygame.mouse.get_pos()  # Pega a posição do mouse

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Verificar se o clique foi "New Game"
                if 300 < mouse_y < 350 and WIN_X // 2 - 100 < mouse_x < WIN_X // 2 + 100:
                    start_game(menu)  # Passa a função menu como argumento

                # Verificar se o clique foi "Exit"
                if 400 < mouse_y < 450 and WIN_X // 2 - 50 < mouse_x < WIN_X // 2 + 50:
                    pygame.quit()
                    sys.exit()

        draw_menu(mouse_x, mouse_y)  # Atualizar o menu, passando a posição do mouse