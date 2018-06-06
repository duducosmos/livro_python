#!/usr/bin/env python3.6
# -*- coding: UTF-8 -*-
"""
Módulo principal do Jogo
"""

from curses import initscr, wrapper

from tela import Tela
from controle import Controle
from jogadores import Jogadores

def main(stdscr):
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
            posicoes = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
            controle.pos_y = 0
            controle.pos_x = 0
            jogadores.vencedor = None
            jogadores.fim_de_partida = False
            tela.reiniciar_tela()


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