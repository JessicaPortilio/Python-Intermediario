lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]
   #chave valor
d1 = {x:   y for x, y in lista}
print(d1)
d1 = dict(lista) # isso faz a mesma coisa de cima
print(d1)

d2 = {x:   y*2 for x, y in lista}
print(d2)

lista2 = [
    ('chave', 2),
    ('chave2', 4),
]
d3 = {x:   y*2 for x, y in lista2}
print(d3)
d4 = {x.upper():   y.upper() for x, y in lista}
print(d4)

d5 = {x:   y*2 for x, y in enumerate(range(5))}
print(d5)
d6 = {f'chave_{x}': x**2 for x in range(5)}
print(d6)