import sys
import time

def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)

def gera2():
    variavel ='valor 1'
    yield variavel
    variavel ='valor 2'
    yield variavel
    variavel ='valor 3'
    yield variavel

g = gera()
g2 = gera2()

for v in g:
    print(v)

print(next(g2))
print(next(g2))
print(next(g2))
