import pygame
import sys

pygame.init()

# =========================
# TELA
# =========================

LARGURA = 800
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tutorial")

clock = pygame.time.Clock()

# =========================
# CORES
# =========================

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AMARELO = (255, 210, 0)

# =========================
# TEXTO PIXEL
# =========================

def desenhar_texto_pixel(texto, fonte, cor, contorno, x, y):

    base = fonte.render(texto, True, cor)
    sombra = fonte.render(texto, True, contorno)

    for dx in [-2, 2]:
        for dy in [-2, 2]:
            tela.blit(sombra, (x + dx, y + dy))

    tela.blit(base, (x, y))


# =========================
# CARREGAR SPRITESHEET
# =========================

def carregar_frames(caminho):

    spritesheet = pygame.image.load(
        caminho
    ).convert_alpha()

    COLUNAS = 5
    LINHAS = 2

    largura_frame = spritesheet.get_width() // COLUNAS
    altura_frame = spritesheet.get_height() // LINHAS

    frames = []

    for linha in range(LINHAS):

        for coluna in range(COLUNAS):

            frame = pygame.Surface(
                (largura_frame, altura_frame),
                pygame.SRCALPHA
            )

            frame.blit(
                spritesheet,
                (0, 0),
                (
                    coluna * largura_frame,
                    linha * altura_frame,
                    largura_frame,
                    altura_frame
                )
            )

            frames.append(frame)

    return frames


# =========================
# TUTORIAL
# =========================

def tutorial():

    fundo = pygame.image.load(
        "assets/imagens/fundo_tutorial.jpeg"
    ).convert()

    fundo = pygame.transform.scale(
        fundo,
        (LARGURA, ALTURA)
    )

    fonte_dialogo = pygame.font.SysFont(
        "consolas",
        18
    )

    # =========================
    # PERSONAGEM MASCULINO
    # =========================

    frames = carregar_frames(
        "assets/personagens/presidente_masculino_tutorial.png"
    )

    # =========================
    # PERSONAGEM FEMININA
    # =========================

    personagem_feminina = pygame.image.load(
        "assets/personagens/personagem_feminina_tutorial.png"
    ).convert_alpha()

    LARGURA_FEMININA = 90
    ALTURA_FEMININA = 120

    feminina_x = 680
    feminina_y = 330

    # =========================
    # PERSONAGEM MASCULINO
    # =========================

    LARGURA_PERSONAGEM = 90
    ALTURA_PERSONAGEM = 120

    personagem_x = 580
    personagem_y = 330

    velocidade = 4

    frame_atual = 0
    tempo_animacao = 0

    olhando_direita = True

    mostrar_dialogo = False

    while True:

        # =========================
        # EVENTOS
        # =========================

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_e:
                    mostrar_dialogo = True

                if evento.key == pygame.K_RETURN:
                    return

        teclas = pygame.key.get_pressed()

        andando = False

        # =========================
        # MOVIMENTO
        # =========================

        if teclas[pygame.K_a]:

            personagem_x -= velocidade
            andando = True
            olhando_direita = False

        if teclas[pygame.K_d]:

            personagem_x += velocidade
            andando = True
            olhando_direita = True

        personagem_x = max(
            0,
            min(
                personagem_x,
                LARGURA - LARGURA_PERSONAGEM
            )
        )

        # =========================
        # ANIMAÇÃO
        # =========================

        if andando:

            tempo_animacao += 1

            if tempo_animacao >= 8:

                frame_atual += 1

                if frame_atual >= len(frames):
                    frame_atual = 0

                tempo_animacao = 0

        else:

            frame_atual = 0

        # =========================
        # DESENHO
        # =========================

        tela.blit(
            fundo,
            (0, 0)
        )

        # =========================
        # FEMININA (PARADA)
        # =========================

        sprite_feminina = pygame.transform.scale(
            personagem_feminina,
            (
                LARGURA_FEMININA,
                ALTURA_FEMININA
            )
        )

        tela.blit(
            sprite_feminina,
            (
                feminina_x,
                feminina_y
            )
        )

        # =========================
        # MASCULINO (ANIMADO)
        # =========================

        sprite = pygame.transform.scale(
            frames[frame_atual],
            (
                LARGURA_PERSONAGEM,
                ALTURA_PERSONAGEM
            )
        )

        if not olhando_direita:

            sprite = pygame.transform.flip(
                sprite,
                True,
                False
            )

        tela.blit(
            sprite,
            (
                personagem_x,
                personagem_y
            )
        )

        # =========================
        # DIÁLOGO
        # =========================

        if mostrar_dialogo:

            pygame.draw.rect(
                tela,
                (10, 10, 10),
                (150, 520, 500, 50),
                border_radius=10
            )

            pygame.draw.rect(
                tela,
                AMARELO,
                (150, 520, 500, 50),
                2,
                border_radius=10
            )

            desenhar_texto_pixel(
                "Voce pressionou E para interagir.",
                fonte_dialogo,
                BRANCO,
                PRETO,
                185,
                535
            )

        desenhar_texto_pixel(
            "APERTE ENTER PARA CONTINUAR",
            fonte_dialogo,
            BRANCO,
            PRETO,
            250,
            60
        )

        pygame.display.update()
        clock.tick(60)


# =========================
# INICIAR
# =========================

tutorial()