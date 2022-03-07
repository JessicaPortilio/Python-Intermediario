# lists, tuples, str -> Sequences -> Iterável

nome = 'Maria Vanessa'

for letra in nome:
    print(letra)

print('#' * 20)

iterador = iter(nome)

try:
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
except:
    pass

print('Cadê os Valores')
for valor in iterador:
    print(valor)
print('Eu já consumir os valores usando o next lá em cima')

gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))



print('Olha o for')
for letra in gerador:
    print(letra)

print('Olha o outro for')
for letra in gerador:
    print(letra)
print('Não tem valor pq já consumiu tudo')