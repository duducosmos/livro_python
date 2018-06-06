#!/usr/bin/env python3.6
# -*- coding: UTF-8 -*-
"""
Um jogo da velha simples.
"""

from curses import initscr, wrapper
from random import randint

def boas_vindas(stdscr):
    stdscr.addstr(1, 1, "Bem-vindo ao Jogo da Velha.")
    stdscr.addstr(2, 1, "Pressione q para sair e h para obter ajuda.")
    stdscr.addstr(16, 1, "Desenvolvido por: E. S. Pereira.")
    stdscr.addstr(17, 1, "Licensa Nova BSD.")

def ajuda(stdscr):
    stdscr.clear()
    stdscr.border()
    stdscr.addstr(1, 1, "Pressione Q para sair ou H para exibir essa ajuda.")
    stdscr.addstr(2, 1, "Para mudar a posição, use as teclas: A, D, S, W")
    stdscr.addstr(3, 1, "Para definir uma posição do jogo, digite: L")
    stdscr.addstr(4, 1, "Para reiniciar a partida, digite: Y")
    stdscr.addstr(5, 1, "Pressione espaço para sair dessa tela.")
    stdscr.refresh()

def reiniciar_tela(stdscr, limpar=True):
    if limpar is True:
        stdscr.clear()
    stdscr.border()
    boas_vindas(stdscr)
    stdscr.refresh()

def tabuleiro(stdscr, posicoes, x_center):
    stdscr.clear()
    reiniciar_tela(stdscr, limpar=False)

    stdscr.addstr(10, x_center - 3, "------")
    stdscr.addstr(12, x_center - 3, "------")
    i = 9
    for linha in posicoes:
        tela = "%s|%s|%s " % tuple(linha)
        stdscr.addstr(i, x_center - 3, tela)
        i += 2

def limites(pos_x, pos_y):
    if pos_x > 2:
        pos_x = 0
    if pos_x < 0:
        pos_x = 2

    if pos_y > 2:
        pos_y = 0

    if pos_y < 0:
        pos_y = 2

    return pos_x, pos_y

def espaco_do_tabuleiro(pos_x, pos_y, entrada):
    if entrada == 'a':
        pos_x, pos_y = limites(pos_x - 1, pos_y)
    elif entrada == 'd':
        pos_x, pos_y = limites(pos_x + 1, pos_y)
    elif entrada == 's':
        pos_x, pos_y = limites(pos_x, pos_y + 1)
    elif entrada == 'w':
        pos_x, pos_y = limites(pos_x, pos_y - 1)
    else:
        pass

    return pos_x, pos_y

def cursor(stdscr, pos_x, pos_y, x_center):
    
    cursor_y = 9
    cursor_x = x_center - 3
    if pos_y == 1:
        cursor_y += 2

    if pos_y == 2:
        cursor_y += 4

    if pos_x == 1:
        cursor_x += 2

    if pos_x == 2:
        cursor_x += 4

    stdscr.move(cursor_y, cursor_x)

def jogador(pos_x, pos_y, posicoes):
    if posicoes[pos_y][pos_x] == " ":
        posicoes[pos_y][pos_x] = "x"
        return True, posicoes
    return False, posicoes

def robo(posicoes):
    
    vazias = []
    for i in range(0, 3):
        for j in range(0, 3):
            if posicoes[j][i] == " ":
                vazias.append([j, i])

    n_escolhas = len(vazias)
    if n_escolhas != 0:
        j, i = vazias[randint(0, n_escolhas - 1)]
        posicoes[j][i] = "o"

    return posicoes


def ganhador(posicoes):
    diagonal1 = [posicoes[0][0], posicoes[1][1], posicoes[2][2]]
    diagonal2 = [posicoes[0][2], posicoes[1][1], posicoes[2][0]]

    transposta = [[], [], []]
    for i in range(3):
        for j in range(3):
            transposta[i].append(posicoes[j][i])

    gan = total_alinhado(diagonal1)
    if gan is not None:
        return gan

    gan = total_alinhado(diagonal2)

    if gan is not None:
        return gan

    velha = 9
    for i in range(3):

        gan = total_alinhado(posicoes[i])
        if gan is not None:
            return gan

        gan = total_alinhado(transposta[i])
        if gan is not None:
            return gan

        velha -= posicoes[i].count("x")
        velha -= posicoes[i].count("o")

    if velha == 0:
        return "velha"

    return None

def total_alinhado(linha):
    num_x = linha.count("x")
    num_o = linha.count("o")

    if num_x == 3:
        return "x"
    if num_o == 3:
        return "o"

    return None

def fim_de_jogo(stdscr, vencedor):
    stdscr.addstr(6, 1, "O %s venceu..." % vencedor)
    stdscr.addstr(7, 1, "Pressione Y para jogar novamente ou Q para sair.")
    stdscr.refresh()

def main(stdscr):
    reiniciar_tela(stdscr)
    width = stdscr.getmaxyx()[1]
    x_center = (width - 1) // 2
    posicoes = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    pos_x, pos_y = 0, 0

    fim_de_partida = None

    while True:
        entrada = stdscr.getkey()
        if entrada == 'q':
            break

        if fim_de_partida is None:

            if entrada in ['a', 's', 'w', 'd']:
                pos_x, pos_y = espaco_do_tabuleiro(pos_x, pos_y, entrada)

            if entrada == "\n":
                jogou, posicoes = jogador(pos_x, pos_y, posicoes)
                fim_de_partida = ganhador(posicoes)
                if jogou is True and fim_de_partida is None:
                    posicoes = robo(posicoes)

        if entrada == "y":
            fim_de_partida = None
            posicoes = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
            pos_x = 0
            pos_y = 0

        if entrada == 'h':
            ajuda(stdscr)
        else:
            tabuleiro(stdscr, posicoes, x_center)
            if fim_de_partida is not None:
                fim_de_jogo(stdscr, fim_de_partida)
            cursor(stdscr, pos_x, pos_y, x_center)


if __name__ == "__main__":
    initscr()
    wrapper(main)