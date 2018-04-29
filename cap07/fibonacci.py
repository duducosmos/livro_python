import time
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def fibonacciGen(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

t1 = time.time()
sequencia = [fibonacci(n) for n in range(10000)]
t2 = time.time() - t1
print("Tempo total = {0}".format(t2))
t1 = time.time()
sequencia = list(fibonacciGen(10000))
t2 = time.time() - t1
print("Tempo total com Gerador = {0}".format(t2))
