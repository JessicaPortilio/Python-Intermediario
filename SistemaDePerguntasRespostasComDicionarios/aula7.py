print()
print(f'Bem Vindo as perguntas, para responder as perguntas é simples. ')
print(f'Você vai ter algumas opções. ')
print(f'Ex: ')
print(f'[a]: 4 ')
print(f'[b]: 5 ')
print(f'[c]: 10 ')
print(f'Suponhamos que vc quer escolher a resposta 5, basta digitar a letra que corresponde o número desejado ')
print(f'que nesse caso seria a letra b ')

perguntas = {
    'Pergunta 1':{
        'pergunta': 'Quanto é 2+2?? ',
        'respostas' : {
            'a' : '1',
            'b' : '4',
            'c' : '5',
        },
        'resposta_certa' : 'b',
    },
    'Pergunta 2':{
        'pergunta': 'Quanto é 3 * 2?? ',
        'respostas' : {
            'a' : '4',
            'b' : '10',
            'c' : '6',
        },
        'resposta_certa' : 'c',
    },
    'Pergunta 3':{
        'pergunta': 'Quanto é 2-2?? ',
        'respostas' : {
            'a' : '0',
            'b' : '4',
            'c' : '5',
        },
        'resposta_certa' : 'a',
    },
    'Pergunta 4':{
        'pergunta': 'Quanto é 10 / 2?? ',
        'respostas' : {
            'a' : '4',
            'b' : '5',
            'c' : '6',
        },
        'resposta_certa' : 'b',
    },
}
print()
respostas_certas = 0
for chave_pergunta, values_pergunta in perguntas.items():
    print(f'{chave_pergunta} = {values_pergunta["pergunta"]}')
    print('Respostas: ')
    for chave_resposta, values_resposta in values_pergunta['respostas'].items():
        print(f'[{chave_resposta}]: {values_resposta}')
    resposta_usuario = input('Qual é sua resposta: ')

    if resposta_usuario == values_pergunta['resposta_certa']:
        print('EHHHHHHH!!! VOCÊ ACERTOU""""""')
        respostas_certas += 1
    else:
        print('IXIIIII!!! VOCÊ ERROU!!!!')
    print()

qtd_perguntas = len(perguntas)
porcetagem_acerto = respostas_certas /  qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas')
print(f'Sua porcentagem de acerto foi de {porcetagem_acerto}%')
