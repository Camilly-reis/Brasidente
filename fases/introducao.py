import pygame
import cv2
import sys

pygame.init()
pygame.mixer.init()

LARGURA = 800
ALTURA = 600

tela = pygame.display.set_mode(
    (LARGURA, ALTURA)
)

pygame.display.set_caption(
    "Vídeo Avião"
)

clock = pygame.time.Clock()

# vídeo
video = cv2.VideoCapture(
    "assets/videos/aviao.mp4"
)

BRANCO = (255,255,255)
PRETO = (0,0,0)


# ==========================
# TEXTO PIXEL
# ==========================

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


# ==========================
# ANIMAÇÃO AVIÃO
# ==========================

def animacao_aviao():

    fonte_principal = pygame.font.SysFont(
        "consolas",
        30,
        bold=True
    )

    fonte_secundaria = pygame.font.SysFont(
        "consolas",
        18,
        bold=True
    )


    # ==========================
    # SOM
    # ==========================

    pygame.mixer.music.load(
        "assets/sons/aviao_pousando.mp3"
    )

    pygame.mixer.music.set_volume(
        0.5
    )

    # inicia áudio
    pygame.mixer.music.play()


    while True:

        ret, frame = video.read()


        # ==========================
        # REINICIAR VÍDEO + SOM
        # ==========================

        if not ret:

            # volta vídeo
            video.set(
                cv2.CAP_PROP_POS_FRAMES,
                0
            )

            # reinicia som
            pygame.mixer.music.stop()

            pygame.mixer.music.play()

            continue


        frame = cv2.resize(
            frame,
            (LARGURA, ALTURA)
        )

        frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        frame = pygame.surfarray.make_surface(
            frame.swapaxes(0,1)
        )


        tela.blit(
            frame,
            (0,0)
        )


        # ==========================
        # TEXTO PISCANDO
        # ==========================

        if pygame.time.get_ticks()%1000 < 700:

            texto1 = "PRESSIONE ENTER"
            texto2 = "PARA CONTINUAR"

            render1 = fonte_principal.render(
                texto1,
                True,
                BRANCO
            )

            x = (
                LARGURA
                - render1.get_width()
            )//2


            pygame.draw.line(
                tela,
                (180,180,180),
                (x-90,545),
                (x-20,545),
                2
            )


            pygame.draw.line(
                tela,
                (180,180,180),
                (
                    x+render1.get_width()+20,
                    545
                ),
                (
                    x+render1.get_width()+90,
                    545
                ),
                2
            )


            desenhar_texto_pixel(
                texto1,
                fonte_principal,
                BRANCO,
                PRETO,
                x,
                520
            )


            render2 = fonte_secundaria.render(
                texto2,
                True,
                (180,180,180)
            )


            x2 = (
                LARGURA
                - render2.get_width()
            )//2


            desenhar_texto_pixel(
                texto2,
                fonte_secundaria,
                (180,180,180),
                PRETO,
                x2,
                560
            )


        # ==========================
        # EVENTOS
        # ==========================

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                video.release()

                pygame.mixer.music.stop()

                pygame.quit()

                sys.exit()


            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_RETURN:

                    video.release()

                    pygame.mixer.music.stop()

                    return


        pygame.display.update()

        clock.tick(60)


animacao_aviao()