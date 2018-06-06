#!/usr/bin/env python3.6
# -*- coding: UTF-8 -*-
"""
Programa sob licença GNU V.3
Desenvolvido por: E. S. Pereira
Versão 0.0.1
"""

class Carro(object):
    def __init__(self, cor, potencia):
        self.cor = cor
        self.potencia = potencia
        self._velocidade = 0

    def __atualiza_velocidade(self, valor):
        self._velocidade = valor

    def acelerar(self):
        self.__atualiza_velocidade(valor=10)
        print("Vrummm")

    def freiar(self):
        self.__atualiza_velocidade(valor=0)
        print("Parando")