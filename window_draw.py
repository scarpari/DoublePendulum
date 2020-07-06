import math
import pygame
import numpy as np

def draw(system, cvs, width, height, dt):
    """
                     system -> representa o dispositivo geral
                     cvs -> janela
                     dt-> tempo entre os "quadros"
                                                                            """

    t1 = system.t1
    t2 = system.t2
    # Associando o tamanho da janela aberta ao tamanho das hastes
    P1 = 0.9*min(width/2, height/2)*0.5
    P2 = 0.9*min(width/2, height/2)*0.5

    # posicao em (x,y) -> gerada pelo numpy
    O = np.array([int(width/2), int(height/2)])  # onde esta fixado a haste 1
    A = O + np.array([int(P1*math.sin(t1)), int(P1*math.cos(t1))])  # bolinha 1
    B = A + np.array([int(P2*math.sin(t2)), int(P2*math.cos(t2))])  # bolinha 2

    # formatos e cores das bolinhas e haste
    color_L = (255, 255, 255)  # BRANCO
    cvs.fill((50, 15, 50))      # Atualiza apagando tudo na tela -> apaga tudo
    pygame.draw.line(cvs, color_L, O, A, 3)
    pygame.draw.line(cvs, color_L, A, B, 3)

    """ A logica usada foi a de que a cada dt a tela apaga inteira e atualiza em seguida com os dados novos """

    myfont = pygame.font.SysFont("Arial", 15)
    label = myfont.render("dt = %.3g        "
                          "Programa Feito para o Projeto de FIS-32 ITA" % dt, 1, (255, 255, 255))
    cvs.blit(label, (10, 10))
    pygame.display.flip()
