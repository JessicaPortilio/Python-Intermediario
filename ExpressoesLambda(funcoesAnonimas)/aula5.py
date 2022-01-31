lista = [
    [9],
    [1],
    [3],
]
lista.sort()
print(lista)

lista2 = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

def func(item):
    return item[1]

lista2.sort(key=func)
print(lista2)
lista2.sort(key=func, reverse= True)
print(lista2)
lista2.sort(key=lambda item: item[1], reverse= True)
print(lista2)

print(sorted(lista2, key=lambda  i: i[1]))