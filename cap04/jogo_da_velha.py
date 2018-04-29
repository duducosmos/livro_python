#!/usr/bin/env python3.6
# -*- coding: UTF-8 -*-
"""
Um jogo da velha simples.

Licensa:

Copyright 2017 E. S. Pereira

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation and/or
other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors
may be used to endorse or promote products derived from this software without
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
THE POSSIBILITY OF SUCH DAMAGE.
"""

from curses import initscr, wrapper
from random import randint

_AUTHOR = "E. S. Pereira"
_EMAIL = "pereira.somoza@gmail.com"
_DATA = "29/07/2017"
_VERSION = "0.0.1"


def boas_vindas(stdscr):
    """
    Desenha as informações de boas vindas e de crédito
    """
    stdscr.addstr(1, 1, "Bem vindo ao Jogo da Velha.")
    stdscr.addstr(2, 1, "Digite q para sair e h para obter ajuda.")
    stdscr.addstr(3, 1, "Para jogar digite umas das teclas: a,s,w,d.")
    stdscr.addstr(16, 1, "Desenvovido por : E. S. Pereira.")
    stdscr.addstr(17, 1, "Licensa Nova BSD.")


def ajuda(stdscr):
    """
    Apresenta a tela de ajuda.
    """
    stdscr.clear()
    stdscr.border()
    stdscr.addstr(1, 1, "Digite q para sair e h para exibir essa ajuda.")
    stdscr.addstr(2, 1, "Para mudar a posicao use as teclas: a,d,s,w")
    stdscr.addstr(3, 1, "Para definir uma posição do jogo digite: Enter")
    stdscr.addstr(4, 1, "Para reiniciar a partida digite: y")
    stdscr.addstr(5, 1, "Digite espaço para sair dessa tela.")
    stdscr.refresh()


def fim_de_jogo(stdscr, vencedor):
    """
    Recebe como entrada o nome do vencedor.
    Desenha as informações do fim da jogada e o nome do vencedor
    """
    stdscr.addstr(6, 1, "O %s venceu..." % vencedor)
    stdscr.addstr(7, 1, "Precione y para jogar novamente ou q para sair.")
    stdscr.refresh()


def reiniciar_tela(stdscr, limpar=True):
    """
    Redezenha e atualiza a tela do jogo
    """
    if limpar is True:
        stdscr.clear()
    stdscr.border()
    boas_vindas(stdscr)
    stdscr.refresh()


def limites(pos_x, pos_y):
    """
    Determina os limites do tabuleiro do jogo
    """
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
    """
    Retorna a posição relativa da peça dentro do tabuleiro do jogo
    """
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
    """
    Move o cursor ao longo das casas do tabuleiro
    """

    curor_y = 9
    cursor_x = x_center - 3
    if pos_y == 1:
        curor_y += 2

    if pos_y == 2:
        curor_y += 4

    if pos_x == 1:
        cursor_x += 2

    if pos_x == 2:
        cursor_x += 4

    stdscr.move(curor_y, cursor_x)


def tabuleiro(stdscr, posicoes, x_center):
    """
    Desenha o tabuleiro do jogo na tela
    """
    stdscr.clear()
    reiniciar_tela(stdscr, limpar=False)

    stdscr.addstr(10, x_center - 3, "------")
    stdscr.addstr(12, x_center - 3, "------")
    i = 9
    for linha in posicoes:
        tela = "%s|%s|%s " % tuple(linha)
        stdscr.addstr(i, x_center - 3, tela)
        i += 2


def jogador(pos_x, pos_y, posicoes):
    """
    Marca a opção do jogador
    """
    if posicoes[pos_y][pos_x] == " ":
        posicoes[pos_y][pos_x] = "x"
        return True, posicoes
    return False, posicoes


def robo(posicoes):
    """
    Jogador autônomo ou jogador máquina
    """

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


def total_alinhado(linha):
    """
    Verifica se existem três elementos iguais numa dada lista
    """
    num_x = linha.count("x")
    num_o = linha.count("o")

    if num_x == 3:
        return "x"
    if num_o == 3:
        return "o"

    return None


def ganhador(posicoes):
    """
    Determina, dentro das regras do jogo, quem foi o ganhador.
    """
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


def main(stdscr):
    """
    Função principal do jogo. Contém o loop principal e o mapeamento das teclas
    do jogo.
    """
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
                    fim_de_partida = ganhador(posicoes)

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
