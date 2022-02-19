import copy

d1 ={'chave1': 'valor da chave'}
d1['nova_chave'] = 'Valor da nova chave'
print(d1)
print(d1['chave1'])

d2= dict(chave1='Valor da chave', chave2='Valor da chave2')
print(d2['chave1'])

d3 = {1: 'valor numero um', 2: 'valor do numero dois', 3: 'valor do numero tres'}
print(d3[2])

d4={
    'str' : 'valor',
    123 : 'Outro valor',
    (1,2,3,4) : 'Trupla',
}
print(   d4[(1,2,3,4)]  )

d4['naoexiste'] = 'Agora existe'
if 'naoexiste' in d4:
    print(d4['naoexiste'])

print('OI')

if d4.get('nomedachave') is not None:
    print(d4.get('nomedachave'))

print('-------')
"""Atualizar um dicionário"""

d4['str'] = 'Outra coisa qualquer'
print(d4['str'])
print('Fazendo update!!!')
d4.update({'nova_chave':'novo_valor'})
print(d4)

"""Apagar algo dentro do dicionário"""
print('Deletando!!!!')
del d4['naoexiste']
print(d4)

d5={
    'str' : 'valor',
    123 : 'Outro valor',
    (1,2,3,4) : 'Trupla',
}
print('str' in d5)
print('str' in d5.keys())
print('valor' in d5.values())

print(len(d5))

print('-----------------')
clientes = {
    'cliente1': {
        'nome' : 'Maria',
        'sobrenome' : 'Santos',
    },
'   cliente2': {
        'nome' : 'Fernando',
        'sobrenome' : 'Santos',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

d = {'k1':[1,2,3,{'café':['banana','mulher','colher',{'alvo':[1,2,3,'olá']}]}]}
###FAZER A COPIA DE UM DICIONARIO
v= d.copy()

print(d['k1'][3]['café'][3]['alvo'][3])


d10 = {1: 'a', 2: 'b', 3: 'c', 'd' : ('Maria', 'Clisvania')}
v = d10.copy()
v[1] = 'Jessica'
v['d'] = 'Olá'
print(d10)
print(v)

lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]
d11 = dict(lista)
print(d11)

d12 = {
    1 : 2,
    2 : 3,
    4 : 5,

}

d13 = {
    'a' : 'b',
    'c' : 'd',
    'e' : 'f',

}

d12.update(d13)


print(d12)
d12.pop(4)
print(d12)
d12.popitem()
print(d12)

