string = '01234567890123456789012345678901234567890123456789012345678901234567890123456789'
n = 10
comp = [i for i in range(0, len(string), n)] #primeiro temos os contadores para saber a quantidade de vezes que vamos pular
print(comp)
comp = [(i, i + n) for i in range(0, len(string), n)] #somos o i + 10 para gera as tuplas de inicio
print(comp)
lista = [f'string[{i}:{i + n}]' for i in range(0, len(string), n)] #fizemos o fatiamento da string de 0 a 10, de 10 a 20 e por aí vai
print(lista)
lista = [string[i:i + n] for i in range(0, len(string), n)] #aqui temos o resultado do que vimos ali em cima o range começa em zero e vai com o tamanho da string pulando de 10 em 10
print(lista)
retorno = '.'.join(lista) #aqui usamos o join para juntar a lista colocando o .
print(retorno)
