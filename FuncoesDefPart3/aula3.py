"""
Funções (def)
args **Kwargs
"""

# def func(*args):
#     print(args)
#     print(args[0])
#     print(args[-1])
#     print(len(args))
#     args = list(args)
#     args[0] = 20
#     print(args)
#
#
#
# func(1,2,3,4)
#
# lista = [1,2,3,4,5]
# n1, n2, *n = lista
# print(n1, n2, n)
# print(lista)
# print(*lista)

# def func(*args):
#     print(args)
#
lista = [1, 2, 3, 4, 5]
lista2 = [100, 200, 300]
#
# func(*lista, 10, 20, 30, *lista2)

# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     print(kwargs['nome'], kwargs['sobrenome'])
#
# func(*lista, *lista2, nome='Paula', sobrenome= "Miranha")


def func(*args, **kwargs):
    print(args)
    nome = kwargs.get('nome')
    if nome is not None:
        print(nome)
    else:
        print('Nome não existe')
    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)
    else:
        print('Idade não existe')

func(*lista, *lista2, nome='Paula', sobrenome= "Miranha")

