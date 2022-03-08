"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""
from itertools import zip_longest, count

indice = count()

# Código
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
# Código
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(indice, estados, cidades)
#print(list(cidades_estados))

#for valor in cidades_estados:
#    print(valor)

cidades_estados2 = zip_longest(estados, cidades, fillvalue='Estado')

for indice, estados, cidade in cidades_estados:
    print(indice, estados, cidade)