import pygame
import imageio
import numpy as np

pygame.init()

# Tamanho da cena
LARGURA = 320
ALTURA = 180

tela = pygame.Surface((LARGURA, ALTURA))

quadros = []

# Função para desenhar pixel art
def pixel_rect(surface, cor, x, y, w, h):
    pygame.draw.rect(surface, cor, (x, y, w, h))

for frame in range(6):

    # Céu noturno
    tela.fill((10, 20, 50))

    # Estrelas simples
    estrelas = [
        (30,20),(90,40),(150,30),
        (250,50),(290,25),(200,15)
    ]

    for e in estrelas:
        pixel_rect(tela,(255,255,255),e[0],e[1],2,2)

    # Cidade ao fundo
    predios = [
        (20,100,20,40),
        (55,90,25,50),
        (95,105,30,35),
        (140,80,20,60),
        (180,95,25,45),
        (220,85,35,55),
        (270,100,25,40)
    ]

    for p in predios:
        pixel_rect(
            tela,
            (40,40,60),
            p[0],
            p[1],
            p[2],
            p[3]
        )

        # janelas
        for jx in range(p[0]+4,p[0]+p[2]-4,6):
            for jy in range(p[1]+4,p[1]+p[3]-4,8):
                pixel_rect(
                    tela,
                    (255,220,100),
                    jx,
                    jy,
                    2,
                    2
                )

    # Pista (sempre embaixo)
    pixel_rect(
        tela,
        (40,40,40),
        0,
        ALTURA-25,
        LARGURA,
        25
    )

    # Luzes da pista
    for x in range(0,LARGURA,20):

        cor = (0,120,255) if x%40==0 else (255,220,0)

        pixel_rect(
            tela,
            cor,
            x,
            ALTURA-28,
            4,
            4
        )

    # Movimento do avião
    aviao_x = -50 + frame*45
    aviao_y = 20 + frame*18

    # Ao pousar desacelera
    if frame>=4:
        aviao_x-=10*(frame-3)

    # Corpo
    pixel_rect(
        tela,
        (240,240,240),
        aviao_x,
        aviao_y,
        48,
        10
    )

    # Nariz
    pixel_rect(
        tela,
        (240,240,240),
        aviao_x+48,
        aviao_y+2,
        8,
        6
    )

    # Asa
    pixel_rect(
        tela,
        (210,210,210),
        aviao_x+15,
        aviao_y+10,
        20,
        5
    )

    # Cauda
    pixel_rect(
        tela,
        (210,210,210),
        aviao_x+2,
        aviao_y-8,
        6,
        10
    )

    # Rodas aparecem ao aproximar da pista
    if frame >= 2:

        pixel_rect(
            tela,
            (20,20,20),
            aviao_x+15,
            aviao_y+14,
            4,
            4
        )

        pixel_rect(
            tela,
            (20,20,20),
            aviao_x+35,
            aviao_y+14,
            4,
            4
        )

    # Fumaça ao tocar pista
    if frame >=4:

        for i in range(5):

            pixel_rect(
                tela,
                (180,180,180),
                aviao_x-10-(i*5),
                ALTURA-40-i,
                5,
                5
            )

    # Converter quadro pygame -> imagem
    frame_array = pygame.surfarray.array3d(tela)
    frame_array=np.transpose(frame_array,(1,0,2))

    quadros.append(frame_array)

# Criar GIF
imageio.mimsave(
    "aviao_pousando.gif",
    quadros,
    duration=0.15,
    loop=0
)

print("GIF criado: aviao_pousando.gif")

pygame.quit()