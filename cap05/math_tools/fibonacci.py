#!/usr/bin/env python3.6
# -*- coding: UTF-8 -*-
"""
Script com funções relacionadas a série de Fibonacci
"""

def fibonacci(n):
    """
    Função geradora que retorna elementos da série de Fibonacci.
    Entrada:
        n: Total de elementos a serem calculados
    Saída:
        valor correspondente da série
    """
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

if __name__ == "__main__":
    import sys
    n = int(sys.argv[1])
    fib = list(fibonacci(n))
    print(fib)
