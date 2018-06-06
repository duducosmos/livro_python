#!/usr/bin/env python3.6
# -*- coding: UTF-8 -*-
"""
Jogo de dados
Programa sob licença GNU V.3
Desenvolvido por: E. S. Pereira
Versão 0.0.1
"""

from random import randint

print("Jogo de Dados")
print("Teste sua sorte")

while(True):
    numero = int(input("Escolha um número: "))
    dado = randint(1, 6)
    if dado == numero:
        print("Parabéns, saiu o seu número no dado.")
    else:
        print("Não foi dessa vez.")
        print("O número sorteado foi: ")
        print(dado)
    print("Deseja tentar a sorte novamente?")
    continuar = input("Digite S para continuar ou N para sair: ")

    if continuar == 'N' or continuar == 'n':
        break