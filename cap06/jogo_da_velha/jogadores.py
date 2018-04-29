#!/usr/bin/env python3.6
# -*- coding: UTF-8 -*-
"""
Módulo responsável por gerenciar os Jogadores.

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

from random import randint


_AUTHOR = "E. S. Pereira"
_EMAIL = "pereira.somoza@gmail.com"
_DATA = "29/07/2017"
_VERSION = "0.0.1"


class Jogadores(object):
    """
    Gerencia os Jogadores do Jogo
    Recebe o controle e a matrix contendo as posições da jogada
    """

    def __init__(self, controle, posicoes):
        self.controle = controle
        self.posicoes = posicoes
        self.fim_de_partida = False
        self._vencedor = None

    def _get_vencedor(self):
        return self._vencedor

    def _set_vencedor(self, vencedor):
        self._vencedor = vencedor

    def jogador(self):
        """
        Marca a opção do jogador
        """
        if self.posicoes[self.controle.pos_y][self.controle.pos_x] == " ":
            self.posicoes[self.controle.pos_y][self.controle.pos_x] = "x"
            return True
        return False

    def robo(self):
        """
        Jogador autônomo ou jogador máquina
        """
        vazias = []
        for i in range(0, 3):
            for j in range(0, 3):
                if self.posicoes[j][i] == " ":
                    vazias.append([j, i])

        n_escolhas = len(vazias)
        if n_escolhas != 0:
            j, i = vazias[randint(0, n_escolhas - 1)]
            self.posicoes[j][i] = "o"

    def __total_alinhado(self, linha):
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

    def ganhador(self):
        """
        Determina, dentro das regras do jogo, quem foi o ganhador.
        """
        diagonal1 = [self.posicoes[0][0],
                     self.posicoes[1][1],
                     self.posicoes[2][2]
                     ]

        diagonal2 = [self.posicoes[0][2],
                     self.posicoes[1][1],
                     self.posicoes[2][0]
                     ]

        transposta = [[], [], []]
        for i in range(3):
            for j in range(3):
                transposta[i].append(self.posicoes[j][i])

        gan = self.__total_alinhado(diagonal1)
        if gan is not None:
            self._vencedor = gan
            return True

        gan = self.__total_alinhado(diagonal2)

        if gan is not None:
            self._vencedor = gan
            return True

        velha = 9
        for i in range(3):

            gan = self.__total_alinhado(self.posicoes[i])
            if gan is not None:
                self._vencedor = gan
                return True

            gan = self.__total_alinhado(transposta[i])
            if gan is not None:
                self._vencedor = gan
                return True

            velha -= self.posicoes[i].count("x")
            velha -= self.posicoes[i].count("o")

        if velha == 0:
            self._vencedor = "velha"
            return True

        return False

    def jogar(self):
        """
        Realiza a jogada de uma partida.
        """
        jogou = self.jogador()
        self.fim_de_partida = self.ganhador()

        if jogou is True and self.fim_de_partida is False:
            self.robo()
            self.fim_de_partida = self.ganhador()

    vencedor = property(_get_vencedor, _set_vencedor)
