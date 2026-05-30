import pygame
import sys

pygame.init()

LARGURA = 800
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tutorial")

clock = pygame.time.Clock()

BRANCO = (255,255,255)
PRETO = (0,0,0)
AMARELO = (255,210,0)

# =========================
# FUNÇÃO TEXTO PIXEL
# =========================

def desenhar_texto_pixel(texto, fonte, cor, contorno, x, y):

    base = fonte.render(texto, True, cor)
    sombra = fonte.render(texto, True, contorno)

    for dx in [-2,2]:
        for dy in [-2,2]:
            tela.blit(sombra, (x+dx,y+dy))

    tela.blit(base, (x,y))


def carregar_spritesheet(imagem, largura_frame, altura_frame):

    frames = []

    quantidade = imagem.get_width() // largura_frame

    for i in range(quantidade):

        frame = pygame.Surface(
            (largura_frame, altura_frame),
            pygame.SRCALPHA
        )

        frame.blit(
            imagem,
            (0,0),
            (i * largura_frame, 0,
             largura_frame, altura_frame)
        )

        frames.append(frame)

    return frames


def tutorial():

    fundo = pygame.image.load(
        "assets/imagens/fundo_tutorial.png"
    ).convert()

    fundo = pygame.transform.scale(
        fundo,
        (LARGURA, ALTURA)
    )

    # ====================================
    # PERSONAGEM
    # ====================================

    spritesheet = pygame.image.load(
        "assets/personagens/presidente.png"
    ).convert_alpha()

    # ajuste para o tamanho real da sua spritesheet
    FRAMES = 10
    largura_frame = spritesheet.get_width() // FRAMES
    altura_frame = spritesheet.get_height()

    frames = carregar_spritesheet(
        spritesheet,
        largura_frame,
        altura_frame
    )

    personagem_x = 650
    personagem_y = 380

    velocidade = 4

    frame_atual = 0
    tempo_animacao = 0

    fonte_dialogo = pygame.font.SysFont(
        "consolas",
        18
    )

    mostrar_dialogo = False

    while True:

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

        if teclas[pygame.K_a]:
            personagem_x -= velocidade
            andando = True

        if teclas[pygame.K_d]:
            personagem_x += velocidade
            andando = True

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

        tela.blit(fundo, (0,0))

        # personagem
        sprite = pygame.transform.scale(
            frames[frame_atual],
            (90, 120)
        )

        tela.blit(
            sprite,
            (personagem_x, personagem_y)
        )

        if mostrar_dialogo:

            pygame.draw.rect(
                tela,
                (10,10,10),
                (180,520,440,50),
                border_radius=10
            )

            pygame.draw.rect(
                tela,
                AMARELO,
                (180,520,440,50),
                2,
                border_radius=10
            )

            desenhar_texto_pixel(
                "Voce interagiu com o personagem!",
                fonte_dialogo,
                BRANCO,
                PRETO,
                210,
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

tutorial()