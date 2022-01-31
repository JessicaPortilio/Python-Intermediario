"""
Funções - def
"""
print('Hello Wordl') # isso é uma função

# def  função():
#     print('Hello Wordl!')
#
# função()

# def função(msg):
#     print(msg)
# função('Mensagem')

# def saudacao(msg, nome):
#     print(msg, nome)
#
# saudacao('Olá', 'Jessica')
# saudacao('Hello', 'Vanessa')

# def saudacao(msg = 'Olá', nome= 'Jessica'):
#     nome = nome.replace('e', '3')
#     msg = msg.replace('e', '3')
#     print(msg, nome)
# saudacao()
# saudacao('Hello', 'Vanessa')

# def divisao(n1, n2):
#     if n1 == 0 and n2 == 0:
#         return
#
#     return n1 / n2
#
# divide = divisao(8,4)
# if divide:
#     print(divide)
# else:
#     print('Conta invalida')

# def dumb():
#     return 1
# print(dumb(), type(dumb()))

def f(var):
    print(var)
def dumb():
    return f

var = dumb()('E colocar o meu valor aqui')