#!/usr/bin/env python3.6
# -*- coding: UTF-8 -*-
"""
Programa sob licença GNU V.3
Desenvolvido por: E. S. Pereira
Versão 0.0.1
"""

class Carro(object):
    def __init__(self, cor, potencia, modelo, marca):
        self.cor = cor
        self.potencia = potencia
        self.modelo = modelo
        self.marca = marca

    def acelerar(self):
        print("Vrummm")

    def freiar(self):
        print("parando")