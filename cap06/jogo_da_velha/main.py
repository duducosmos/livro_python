#!/usr/bin/env python3.6
# -*- coding: UTF-8 -*-
"""
Módulo principal do Jogo

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

from tela import Tela
from controle import Controle
from jogadores import Jogadores

_AUTHOR = "E. S. Pereira"
_EMAIL = "pereira.somoza@gmail.com"
_DATA = "29/07/2017"
_VERSION = "0.0.1"


def main(stdscr):
    """
    Função principal do jogo. Contém o loop principal e o mapeamento das teclas
    do jogo.
    """

    posicoes = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    controle = Controle(stdscr=stdscr)
    tela = Tela(stdscr=stdscr, posicoes=posicoes)
    jogadores = Jogadores(controle=controle, posicoes=posicoes)
    tela.reiniciar_tela()

    jogador_x = 0
    jogador_o = 0

    while True:
        controle.espaco_do_tabuleiro()
        if jogadores.fim_de_partida is False:
            if controle.entrada == "\n":
                jogadores.jogar()

            if jogadores.fim_de_partida is True:
                ganhador = jogadores.vencedor
                if ganhador == "x":
                    jogador_x += 1
                if ganhador == "o":
                    jogador_o += 1

        if controle.entrada == "y":
            """
            # Gera o erro de referência
            posicoes = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
            controle.pos_y = 0
            controle.pos_x = 0
            jogadores.vencedor = None
            jogadores.fim_de_partida = False
            tela.reiniciar_tela()
            """

            #Adequado para poupar memória ao
            #longo da execução prolongada do programa
            for i in range(3):
                for j in range(3):
                    posicoes[i][j] = " "

            controle.pos_y = 0
            controle.pos_x = 0
            jogadores.vencedor = None
            jogadores.fim_de_partida = False
            tela.reiniciar_tela()

            """
            #Cria novos objetos do jogo a cada reinicialização da partida
            #Ao longo do tempo poderá gerar muito lixo na memória
            posicoes = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
            controle = Controle(stdscr=stdscr)
            tela = Tela(stdscr=stdscr, posicoes=posicoes)
            jogadores = Jogadores(controle=controle, posicoes=posicoes)
            tela.reiniciar_tela()
            """

        if controle.entrada == 'h':
            tela.ajuda()
        else:
            tela.tabuleiro(controle)
            tela.placar(jogador_x, jogador_o)
            if jogadores.fim_de_partida is True:
                tela.fim_de_jogo(jogadores.vencedor)
            controle.cursor()


if __name__ == "__main__":
    initscr()
    wrapper(main)
