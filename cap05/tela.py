#!/usr/bin/env python3.6
# -*- coding: UTF-8 -*-
"""
Módulo contendo informações de exibição da Tela do jogo.
"""

class Tela(object):
    """
    Classe para desenhar a tela do Jogo
    Recebe como atributo a tela gerada pelo módulo curses
    """

    def __init__(self, stdscr, posicoes):
        self.stdscr = stdscr
        self.posicoes = posicoes

    def boas_vindas(self):
        self.stdscr.addstr(1, 1, "Bem-vindo ao Jogo da Velha.")
        self.stdscr.addstr(2, 1, "Pressione Q para sair ou H para obter ajuda.")
        self.stdscr.addstr(3, 1, "Para jogar, digite umas das teclas: A, S, W, D.")
        self.stdscr.addstr(16, 1, "Desenvolvido por: E. S. Pereira.")
        self.stdscr.addstr(17, 1, "Licensa Nova BSD.")

    def ajuda(self):
        self.stdscr.clear()
        self.stdscr.border()
        self.stdscr.addstr(1, 1, "Pressione Q para sair ou H para exibir essa ajuda.")
        self.stdscr.addstr(2, 1, "Para mudar a posição, use as teclas: A, S, W, D")
        self.stdscr.addstr(3, 1, "Para definir uma posição do jogo, aperte: Enter")
        self.stdscr.addstr(4, 1, "Para reiniciar a partida, digite: Y")
        self.stdscr.addstr(5, 1, "Pressione espaço para sair dessa tela.")
        self.stdscr.refresh()

    def fim_de_jogo(self, vencedor):
        self.stdscr.addstr(6, 1, "O %s venceu..." % vencedor)
        self.stdscr.addstr(7, 1, "Pressione Y para jogar novamente ou Q para sair.")
        self.stdscr.refresh()

    def reiniciar_tela(self, limpar=True):
        if limpar is True:
            self.stdscr.clear()
        self.stdscr.border()
        self.boas_vindas()
        self.stdscr.refresh()

    def tabuleiro(self, controle):

        self.stdscr.clear()
        self.reiniciar_tela(limpar=False)

        self.stdscr.addstr(10, controle.x_center - 3, "------")
        self.stdscr.addstr(12, controle.x_center - 3, "------")
        i = 9
        for linha in self.posicoes:
            tela = "%s|%s|%s " % tuple(linha)
            self.stdscr.addstr(i, controle.x_center - 3, tela)
            i += 2

    def placar(self, jogador1, jogador2):
        self.stdscr.addstr(4, 1, "Jogador: {0} |Máquina {1}.".format(
            jogador1, jogador2))