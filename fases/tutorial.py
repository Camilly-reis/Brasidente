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

def tutorial(personagem, nome):

    pygame.mouse.set_cursor(
        pygame.cursors.Cursor(
            pygame.SYSTEM_CURSOR_ARROW
        )
    )

    print("Personagem:", personagem)
    print("Nome:", nome)

    fundo = pygame.image.load(
        "assets/imagens/fundo_tutorial.jpeg"
    ).convert_alpha()

    fundo = pygame.transform.scale(
        fundo,
        (LARGURA, ALTURA)
    )

    fonte_dialogo = pygame.font.SysFont(
        "consolas",
        18
    )

    # =========================
    # PERSONAGEM PRINCIPAL
    # =========================

    if personagem == "masculino":

        frames = carregar_frames(
            "assets/personagens/presidente_masculino_tutorial.png"
        )

    else:

        frames = carregar_frames(
            "assets/personagens/presidente_feminino_tutorial.png"
        )

    LARGURA_PERSONAGEM = 122
    ALTURA_PERSONAGEM = 162

    personagem_x = 580
    personagem_y = 330

    # =========================
    # NPC FEMININA
    # =========================

    personagem_feminina = pygame.image.load(
        "assets/personagens/personagem_feminina_tutorial.png"
    ).convert_alpha()

    rect = personagem_feminina.get_bounding_rect()

    if rect.width > 0 and rect.height > 0:
        personagem_feminina = personagem_feminina.subsurface(rect)

    LARGURA_FEMININA = 176
    ALTURA_FEMININA = 189

    feminina_x = 690
    feminina_y = 330

    # =========================
    # CONTROLE
    # =========================

    velocidade = 4

    frame_atual = 0
    tempo_animacao = 0

    olhando_direita = True

    mostrar_dialogo = False
    tutorial_concluido = False

    # =========================
    # LOOP
    # =========================

    while True:

        personagem_rect = pygame.Rect(
            personagem_x,
            personagem_y,
            LARGURA_PERSONAGEM,
            ALTURA_PERSONAGEM
        )

        npc_rect = pygame.Rect(
            feminina_x,
            feminina_y,
            LARGURA_FEMININA,
            ALTURA_FEMININA
        )

        area_interacao = npc_rect.inflate(
            80,
            40
        )

        perto_npc = personagem_rect.colliderect(
            area_interacao
        )

        # =========================
        # EVENTOS
        # =========================

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:

                # Interagir somente perto da NPC
                if evento.key == pygame.K_e:

                    if perto_npc:

                        mostrar_dialogo = True
                        tutorial_concluido = True

                # Continuar somente após interação
                if (
                    evento.key == pygame.K_RETURN
                    and tutorial_concluido
                ):
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

        # NPC

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

        # Mostrar aviso de interação

        if perto_npc:

            desenhar_texto_pixel(
                "PRESSIONE E",
                fonte_dialogo,
                AMARELO,
                PRETO,
                feminina_x + 10,
                feminina_y - 30
            )

        # Personagem

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
                (120, 500, 560, 70),
                border_radius=10
            )

            pygame.draw.rect(
                tela,
                AMARELO,
                (120, 500, 560, 70),
                2,
                border_radius=10
            )

            desenhar_texto_pixel(
                "Seja bem-vindo(a)! Use A e D para andar e E para interagir.",
                fonte_dialogo,
                BRANCO,
                PRETO,
                140,
                520
            )

            desenhar_texto_pixel(
                "Agora pressione ENTER para continuar.",
                fonte_dialogo,
                BRANCO,
                PRETO,
                140,
                545
            )

        else:

            desenhar_texto_pixel(
                "Aproxime-se da personagem e pressione E.",
                fonte_dialogo,
                BRANCO,
                PRETO,
                210,
                60
            )

        pygame.display.update()
        clock.tick(60)