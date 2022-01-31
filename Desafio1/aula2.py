"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""
def mensagem(saudacao, nome):
    print(f'{saudacao}, {nome}')
mensagem('Olá','Jessica')
"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles;
"""
def numero(num1, num2, num3):
    print(num1 + num2 + num3)
numero(2,4,1)
"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um 
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado 
do aumento do percentual do mesmo.
"""
def porcentual(num1, porcentagem):
    soma = num1 + (num1 * porcentagem / 100)
    return soma
resultado = porcentual(100,50)
print(resultado)
"""
4 - Fizz Buzz - Se o parâmentro da função for divisível por 3, retorne fizz, 
se o parâmentro da função for divisível por 5 retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return f'FizzBuzz, {num} é divisível por 3 e 5'
    if num % 5 == 0:
        return f'Buzz, {num} é divisível por 5'
    if num % 3 == 0:
        return f'Fizz, {num} é divisível por 3'
    return num

valor = fizzbuzz(15)
print(valor)

from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print( fizzbuzz(aleatorio))