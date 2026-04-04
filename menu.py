import pygame
import sys

pygame.init()

# Tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("BRASIDENTE")

# Fundo
fundo = pygame.image.load("assets/imagens/fundo.png")
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (40, 90, 200)
AZUL_HOVER = (20, 70, 170)
CINZA = (180, 180, 180)
CINZA_HOVER = (140, 140, 140)

# Fonte
fonte_titulo = pygame.font.SysFont("consolas", 50, bold=True)
fonte_botao = pygame.font.SysFont("consolas", 24)

# Texto pixel (contorno)
def desenhar_texto_pixel(texto, fonte, cor, contorno, x, y):
    base = fonte.render(texto, True, cor)
    sombra = fonte.render(texto, True, contorno)

    for dx in [-2, 2]:
        for dy in [-2, 2]:
            tela.blit(sombra, (x + dx, y + dy))

    tela.blit(base, (x, y))

def desenhar_texto_centro(texto, fonte, cor, rect):
    render = fonte.render(texto, True, cor)
    texto_rect = render.get_rect(center=rect.center)
    tela.blit(render, texto_rect)

def desenhar_botao(rect, cor, texto, fonte, cor_texto):
    pygame.draw.rect(tela, cor, rect, border_radius=8)
    pygame.draw.rect(tela, PRETO, rect, 3, border_radius=8)
    desenhar_texto_centro(texto, fonte, cor_texto, rect)

def escolha_personagem():
    # Som de fundo do menu e escolha do personagem
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sons/menu_e_escolha_dos_personagens.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    # Imagens
    fundo = pygame.image.load("assets/imagens/fundo_escolha_do_personagem.jpeg")
    fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

    img_masc = pygame.image.load("assets/imagens/personagem_masculino.png")
    img_fem = pygame.image.load("assets/imagens/personagem_feminino.png")

    img_masc = pygame.transform.scale(img_masc, (200, 200))
    img_fem = pygame.transform.scale(img_fem, (200, 200))

    # Botões
    botao_masc_img = pygame.image.load("assets/imagens/botao_masculino.png")
    botao_fem_img = pygame.image.load("assets/imagens/botao_feminino.png")

    botao_masc_img = pygame.transform.scale(botao_masc_img, (200, 60))
    botao_fem_img = pygame.transform.scale(botao_fem_img, (200, 60))

    # Posições
    pos_masc = (180, 180)
    pos_fem = (420, 180)

    botao_masc = botao_masc_img.get_rect(center=(280, 420))
    botao_fem = botao_fem_img.get_rect(center=(520, 420))

    # Overlay
    overlay = pygame.Surface((200, 60), pygame.SRCALPHA)
    overlay.fill((255, 255, 255, 60))

    # Loop
    while True:
        tela.blit(fundo, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        # Personagens
        tela.blit(img_masc, pos_masc)
        tela.blit(img_fem, pos_fem)

        # Botão masculino
        tela.blit(botao_masc_img, botao_masc)
        if botao_masc.collidepoint(mouse_pos):
            tela.blit(overlay, botao_masc)

        # Botão feminino
        tela.blit(botao_fem_img, botao_fem)
        if botao_fem.collidepoint(mouse_pos):
            tela.blit(overlay, botao_fem)

        # Cursor
        if botao_masc.collidepoint(mouse_pos) or botao_fem.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        # Título central
        titulo = "ESCOLHA SEU PRESIDENTE"
        render = fonte_titulo.render(titulo, True, BRANCO)
        x = (LARGURA - render.get_width()) // 2
        desenhar_texto_pixel(titulo, fonte_titulo, BRANCO, PRETO, x, 60)

        # Texto inferior
        dica = "Clique em uma opção para escolher"
        render_dica = fonte_botao.render(dica, True, BRANCO)
        x_dica = (LARGURA - render_dica.get_width()) // 2
        tela.blit(render_dica, (x_dica, 500))

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_masc.collidepoint(mouse_pos):
                    return "masculino"

                if botao_fem.collidepoint(mouse_pos):
                    return "feminino"

        pygame.display.update()

def menu():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sons/menu_e_escolha_dos_personagens.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    while True:
        tela.blit(fundo, (0, 0))

        # Título
        texto = "BRASIDENTE"
        render = fonte_titulo.render(texto, True, BRANCO)
        largura_texto = render.get_width()

        x = (LARGURA - largura_texto) // 2

        desenhar_texto_pixel(texto, fonte_titulo, BRANCO, PRETO, x, 80)

        # Botões
        botao_iniciar = pygame.Rect(300, 250, 200, 60)
        botao_sair = pygame.Rect(300, 330, 200, 60)

        mouse_pos = pygame.mouse.get_pos()

        # Efeito
        cor_iniciar = AZUL_HOVER if botao_iniciar.collidepoint(mouse_pos) else AZUL
        cor_sair = CINZA_HOVER if botao_sair.collidepoint(mouse_pos) else CINZA

        # Desenhar botões
        desenhar_botao(botao_iniciar, cor_iniciar, "Iniciar", fonte_botao, BRANCO)
        desenhar_botao(botao_sair, cor_sair, "Sair", fonte_botao, PRETO)

        # Cursor mão
        if botao_iniciar.collidepoint(mouse_pos) or botao_sair.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_iniciar.collidepoint(mouse_pos):
                    personagem = escolha_personagem()
                    print("Personagem escolhido:", personagem)

                if botao_sair.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

menu()