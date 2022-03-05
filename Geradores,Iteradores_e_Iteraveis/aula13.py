import sys
import time
lista = [0,1,2,3,4,5] #É um objeto interavel
print(hasattr(lista, '__iter__'))

for v in lista: #o for transforma nossa lista em um iterador
    print(v)

lista = iter(lista)
print(hasattr(lista, '__next__'))
print(next(lista))   #é o que o for faz iterador
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

lista1 = list(range(1000))

print(lista1)

print(sys.getsizeof(lista1))

# def gera():
#     r = []
#     for n in range(100):
#         r.append(n)
#         time.sleep(0.1)
#     return r
#
# g = gera()
#
# for v in g:
#     print(v)

def gera2():
    for n in range(100):
        yield n    #essa minha função é um gerador
        time.sleep(0.1)


g2 = gera2()

for v2 in g2:
    print(v2)


lista2 = [x for x in range(1000)]
print(type(lista2))
lista2 = (x for x in range(1000))
print(type(lista2))
print(next(lista2))
print(next(lista2))
print(next(lista2))
print(next(lista2))

l1 = [x for x in range(1000)]
l2 = (x for x in range(1000))
print(sys.getsizeof(l1))
print(sys.getsizeof(l2))