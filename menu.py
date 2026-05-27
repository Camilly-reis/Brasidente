import pygame
import cv2
import sys

pygame.init()
pygame.mixer.init()

som_clique = None
try:
    som_clique = pygame.mixer.Sound(
        "assets/sons/Cliquee.mpeg.wav"
    )
    som_clique.set_volume(0.5)
except (pygame.error, FileNotFoundError):
    som_clique = None

# ==========================
# TELA
# ==========================

LARGURA = 800
ALTURA = 600

tela = pygame.display.set_mode(
    (LARGURA, ALTURA)
)

pygame.display.set_caption(
    "BRASIDENTE"
)

clock = pygame.time.Clock()

# ==========================
# CURSORES
# ==========================

cursor_seta = pygame.cursors.Cursor(
    pygame.SYSTEM_CURSOR_ARROW
)

cursor_mao = pygame.cursors.Cursor(
    pygame.SYSTEM_CURSOR_HAND
)

# ==========================
# VÍDEO MENU
# ==========================

video = cv2.VideoCapture(
    "assets/imagens/fundo.mp4"
)

# ==========================
# CORES
# ==========================

BRANCO=(255,255,255)
PRETO=(0,0,0)

# ==========================
# FONTES
# ==========================

fonte_titulo=pygame.font.SysFont(
    "consolas",
    50,
    bold=True
)

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

    base=fonte.render(
        texto,
        True,
        cor
    )

    sombra=fonte.render(
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
# ESCOLHA PERSONAGEM
# ==========================

def tocar_clique():
    if som_clique is None:
        return
    try:
        som_clique.play()
    except pygame.error:
        pass


def escolha_personagem():

    fundo=pygame.image.load(
        "assets/imagens/fundo_escolha_do_personagem.png"
    )

    fundo=pygame.transform.scale(
        fundo,
        (LARGURA,ALTURA)
    )

    area_masc=pygame.Rect(
        125,
        215,
        190,
        220
    )

    area_fem=pygame.Rect(
        485,
        215,
        190,
        220
    )

    while True:

        tela.blit(
            fundo,
            (0,0)
        )

        mouse=pygame.mouse.get_pos()

        if (
            area_masc.collidepoint(mouse)
            or
            area_fem.collidepoint(mouse)
        ):

            pygame.mouse.set_cursor(
                cursor_mao
            )

        else:

            pygame.mouse.set_cursor(
                cursor_seta
            )

        for evento in pygame.event.get():

            if evento.type==pygame.QUIT:

                pygame.quit()
                sys.exit()


            if evento.type==pygame.MOUSEBUTTONDOWN:

                if area_masc.collidepoint(mouse):

                    tocar_clique()
                    return "masculino"

                if area_fem.collidepoint(mouse):

                    tocar_clique()
                    return "feminino"

        pygame.display.update()
        clock.tick(60)


# ==========================
# NOME PRESIDENTE
# ==========================

def criar_nome_presidente():

    fundo=pygame.image.load(
        "assets/imagens/fundo_nome_presidente.png"
    )

    fundo=pygame.transform.scale(
        fundo,
        (LARGURA,ALTURA)
    )

    fonte_input=pygame.font.SysFont(
        "consolas",
        34
    )

    nome=""

    caixa_texto=pygame.Rect(
        175,
        370,
        500,
        80
    )

    botao_voltar=pygame.Rect(
        35,
        530,
        135,
        45
    )

    ativo=False

    while True:

        tela.blit(
            fundo,
            (0,0)
        )

        mouse=pygame.mouse.get_pos()

        if (
            caixa_texto.collidepoint(mouse)
            or
            botao_voltar.collidepoint(mouse)
        ):

            pygame.mouse.set_cursor(
                cursor_mao
            )

        else:

            pygame.mouse.set_cursor(
                cursor_seta
            )


        texto=fonte_input.render(
            nome,
            True,
            BRANCO
        )

        tela.blit(
            texto,
            (
                caixa_texto.x+15,
                caixa_texto.y+10
            )
        )


        if ativo:

            if pygame.time.get_ticks()%800<400:

                x_cursor=(
                    caixa_texto.x
                    +15
                    +texto.get_width()
                )

                pygame.draw.line(
                    tela,
                    BRANCO,
                    (
                        x_cursor,
                        caixa_texto.y+10
                    ),
                    (
                        x_cursor,
                        caixa_texto.y+45
                    ),
                    3
                )


        for evento in pygame.event.get():

            if evento.type==pygame.QUIT:

                pygame.quit()
                sys.exit()


            elif evento.type==pygame.MOUSEBUTTONDOWN:

                if botao_voltar.collidepoint(
                    evento.pos
                ):

                    tocar_clique()
                    return None


                ativo=caixa_texto.collidepoint(
                    evento.pos
                )


            elif evento.type==pygame.KEYDOWN and ativo:

                if evento.key==pygame.K_RETURN:

                    if nome.strip()!="":

                        tocar_clique()
                        return nome


                elif evento.key==pygame.K_BACKSPACE:

                    nome=nome[:-1]


                else:

                    novo=nome+evento.unicode

                    largura=fonte_input.render(
                        novo,
                        True,
                        BRANCO
                    ).get_width()

                    if largura<390:

                        nome+=evento.unicode


        pygame.display.update()
        clock.tick(60)


# ==========================
# MENU
# ==========================

def menu():

    pygame.mixer.music.load(
        "assets/sons/menu_e_escolha_dos_personagens.mp3"
    )

    pygame.mixer.music.set_volume(
        0.3
    )

    pygame.mixer.music.play(-1)

    while True:

        ret,frame=video.read()

        if not ret:

            video.set(
                cv2.CAP_PROP_POS_FRAMES,
                0
            )

            ret,frame=video.read()


        frame=cv2.resize(
            frame,
            (LARGURA,ALTURA)
        )

        frame=cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        frame=pygame.surfarray.make_surface(
            frame.swapaxes(0,1)
        )

        tela.blit(
            frame,
            (0,0)
        )


        mouse=pygame.mouse.get_pos()


        area_iniciar=pygame.Rect(
            285,
            255,
            235,
            65
        )

        area_sair=pygame.Rect(
            285,
            335,
            235,
            65
        )


        if (
            area_iniciar.collidepoint(mouse)
            or
            area_sair.collidepoint(mouse)
        ):

            pygame.mouse.set_cursor(
                cursor_mao
            )

        else:

            pygame.mouse.set_cursor(
                cursor_seta
            )


        for evento in pygame.event.get():

            if evento.type==pygame.QUIT:

                video.release()

                pygame.quit()

                sys.exit()


            if evento.type==pygame.MOUSEBUTTONDOWN:


                if area_iniciar.collidepoint(mouse):

                    tocar_clique()
                    personagem=escolha_personagem()

                    if personagem is None:
                        continue


                    nome=criar_nome_presidente()

                    if nome is None:
                        continue


                    pygame.mixer.music.stop()


                    from fases.introducao import animacao_aviao
                    from fases.introducao import intro_aeroporto


                    animacao_aviao()

                    intro_aeroporto(
                        personagem,
                        nome
                    )


                    pygame.mixer.music.play(-1)



                if area_sair.collidepoint(mouse):

                    tocar_clique()
                    video.release()

                    pygame.quit()

                    sys.exit()


        pygame.display.update()

        clock.tick(60)


menu()