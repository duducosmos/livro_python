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
    return posicoes


def main(stdscr):
    reiniciar_tela(stdscr)
    width = stdscr.getmaxyx()[1]
    x_center = (width - 1) // 2
    posicoes = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    pos_x, pos_y = 0, 0


    while True:
        entrada = stdscr.getkey()
        if entrada == 'q':
            break

        if entrada in ['a', 's', 'w', 'd']:
            pos_x, pos_y = espaco_do_tabuleiro(pos_x, pos_y, entrada)

        if entrada == "\n":
            posicoes = jogador(pos_x, pos_y, posicoes)



        if entrada == 'h':
            ajuda(stdscr)
        else:
            tabuleiro(stdscr, posicoes, x_center)
            cursor(stdscr, pos_x, pos_y, x_center)


if __name__ == "__main__":
    initscr()
    wrapper(main)