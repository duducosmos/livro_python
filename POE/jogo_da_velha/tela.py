#!/usr/bin/env python3.6
# -*- coding: UTF-8 -*-
"""
Módulo contendo informações de exibição da Tela do jogo.

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

_AUTHOR = "E. S. Pereira"
_EMAIL = "pereira.somoza@gmail.com"
_DATA = "29/07/2017"
_VERSION = "0.0.1"

class Tela(object):
    """
    Classe para desenhar a tela do Jogo
    Recebe como atributo a tela gerada pelo módulo curses
    """

    def __init__(self, stdscr, posicoes):
        self.stdscr = stdscr
        self.posicoes = posicoes

    def boas_vindas(self):
        """
        Desenha as informações de boas vindas e de crédito
        """
        self.stdscr.addstr(1, 1, "Bem vindo ao Jogo da Velha.")
        self.stdscr.addstr(2, 1, "Digite q para sair e h para obter ajuda.")
        self.stdscr.addstr(3, 1, "Para jogar digite umas das teclas: a,s,w,d.")
        self.stdscr.addstr(16, 1, "Desenvovido por : E. S. Pereira.")
        self.stdscr.addstr(17, 1, "Licensa Nova BSD.")

    def placar(self, jogador1, jogador2):
        "Desenha o placar do jogo"
        self.stdscr.addstr(4, 1, "Jogador: {0} |Máquina {1}.".format(
            jogador1, jogador2))


    def ajuda(self):
        """
        Apresenta a tela de ajuda.
        """
        self.stdscr.clear()
        self.stdscr.border()
        self.stdscr.addstr(1, 1, "Digite q para sair e h para exibir essa ajuda.")
        self.stdscr.addstr(2, 1, "Para mudar a posicao use as teclas: a,d,s,w")
        self.stdscr.addstr(3, 1, "Para definir uma posição do jogo digite: Enter")
        self.stdscr.addstr(4, 1, "Para reiniciar a partida digite: y")
        self.stdscr.addstr(5, 1, "Digite espaço para sair dessa tela.")
        self.stdscr.refresh()

    def fim_de_jogo(self, vencedor):
        """
        Recebe como entrada o nome do vencedor.
        Desenha as informações do fim da jogada e o nome do vencedor
        """
        self.stdscr.addstr(6, 1, "O %s venceu..." % vencedor)
        self.stdscr.addstr(7, 1, "Precione y para jogar novamente ou q para sair.")
        self.stdscr.refresh()

    def reiniciar_tela(self, limpar=True):
        """
        Redezenha e atualiza a tela do jogo
        """
        if limpar is True:
            self.stdscr.clear()
        self.stdscr.border()
        self.boas_vindas()
        self.stdscr.refresh()

    def tabuleiro(self, controle):
        """
        Desenha o tabuleiro do jogo na tela
        """
        self.stdscr.clear()
        self.reiniciar_tela(limpar=False)

        self.stdscr.addstr(10, controle.x_center - 3, "------")
        self.stdscr.addstr(12, controle.x_center - 3, "------")
        i = 9
        for linha in self.posicoes:
            tela = "%s|%s|%s " % tuple(linha)
            self.stdscr.addstr(i, controle.x_center - 3, tela)
            i += 2
