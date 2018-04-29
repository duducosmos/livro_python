#!/usr/bin/env python3.6
# -*- coding: UTF-8 -*-
"""
Módulo responsável por controlar as ações do jogo.

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
import sys

_AUTHOR = "E. S. Pereira"
_EMAIL = "pereira.somoza@gmail.com"
_DATA = "29/07/2017"
_VERSION = "0.0.1"


class Controle(object):
    """
    Responsável por fazer a conexão entre o jogador e a tela do jogo
    """

    def __init__(self, stdscr):
        self.stdscr = stdscr
        width = stdscr.getmaxyx()[1]
        self.x_center = (width - 1) // 2
        self.pos_x = 0
        self.pos_y = 0
        self.entrada = None

    def _limites(self):
        """
        Determina os limites do tabuleiro do jogo
        """
        if self.pos_x > 2:
            self.pos_x = 0
        if self.pos_x < 0:
            self.pos_x = 2

        if self.pos_y > 2:
            self.pos_y = 0

        if self.pos_y < 0:
            self.pos_y = 2

    def espaco_do_tabuleiro(self):
        """
        Retorna a posição relativa da peça dentro do tabuleiro do jogo
        """
        self.entrada = self.stdscr.getkey()

        if self.entrada == 'q':
            sys.exit(0)

        if self.entrada == 'a':
            self.pos_x -= 1
        elif self.entrada == 'd':
            self.pos_x += 1
        elif self.entrada == 's':
            self.pos_y += 1
        elif self.entrada == 'w':
            self.pos_y -= 1
        else:
            pass

        self._limites()

    def cursor(self):
        """
        Move o cursor ao longo das casas do tabuleiro
        """

        curor_y = 9
        cursor_x = self.x_center - 3
        if self.pos_y == 1:
            curor_y += 2

        if self.pos_y == 2:
            curor_y += 4

        if self.pos_x == 1:
            cursor_x += 2

        if self.pos_x == 2:
            cursor_x += 4

        self.stdscr.move(curor_y, cursor_x)
