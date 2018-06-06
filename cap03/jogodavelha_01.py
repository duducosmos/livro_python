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

def main(stdscr):
    stdscr.clear()
    stdscr.border()
    boas_vindas(stdscr)
    stdscr.refresh()

    while True:
        pass


if __name__ == "__main__":
    initscr()
    wrapper(main)