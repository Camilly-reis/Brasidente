import pygame
import sys

pygame.init()

# =========================
# TELA
# =========================

LARGURA = 800
ALTURA = 600

tela = pygame.display.set_mode(
    (LARGURA, ALTURA)
)

pygame.display.set_caption(
    "Tutorial"
)

clock = pygame.time.Clock()

# =========================
# CORES
# =========================

BRANCO = (255,255,255)
PRETO = (0,0,0)
AMARELO = (255,210,0)

# =========================
# FUNÇÃO TEXTO PIXEL
# =========================

def desenhar_texto_pixel(
    texto,
    fonte,
    cor,
    contorno,
    x,
    y
):

    base = fonte.render(
        texto,
        True,
        cor
    )

    sombra = fonte.render(
        texto,
        True,
        contorno
    )

    for dx in [-2,2]:
        for dy in [-2,2]:

            tela.blit(
                sombra,
                (x+dx,y+dy)
            )

    tela.blit(
        base,
        (x,y)
    )

# =========================
# TUTORIAL
# =========================

def tutorial():

    # =========================
    # FUNDO
    # =========================

    fundo = pygame.image.load(
        "assets/imagens/fundo_tutorial.png"
    ).convert()

    fundo = pygame.transform.scale(
        fundo,
        (LARGURA, ALTURA)
    )

    # =========================
    # FONTES
    # =========================

    fonte = pygame.font.SysFont(
        "consolas",
        22,
        bold=True
    )

    fonte_dialogo = pygame.font.SysFont(
        "consolas",
        18
    )

    # =========================
    # DIÁLOGO
    # =========================

    mostrar_dialogo = False

    # =========================
    # LOOP
    # =========================

    while True:

        # =========================
        # EVENTOS
        # =========================

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:

                # tecla E
                if evento.key == pygame.K_e:

                    mostrar_dialogo = True

                # ENTER continua
                if evento.key == pygame.K_RETURN:

                    return

        # =========================
        # FUNDO
        # =========================

        tela.blit(
            fundo,
            (0,0)
        )

        # =========================
        # DIÁLOGO
        # =========================

        if mostrar_dialogo:

            pygame.draw.rect(
                tela,
                (10,10,10),
                (180, 520, 440, 50),
                border_radius=10
            )

            pygame.draw.rect(
                tela,
                AMARELO,
                (180, 520, 440, 50),
                2,
                border_radius=10
            )

            desenhar_texto_pixel(
                "Você interagiu com O personagem!",
                fonte_dialogo,
                BRANCO,
                PRETO,
                220,
                535
            )

        # =========================
        # TEXTO
        # =========================

        desenhar_texto_pixel(
            "APERTE ENTER PARA CONTINUAR",
            fonte_dialogo,
            BRANCO,
            PRETO,
            300,
            65
        )

        pygame.display.update()

        clock.tick(60)

# =========================
# INICIAR
# =========================

tutorial()