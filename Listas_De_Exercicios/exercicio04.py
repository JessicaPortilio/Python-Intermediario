import re

#verificar se o que usuário digitou pode ser convertido para float
def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False

#verificar se o que usuário digitou pode ser convertido para int
def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False

#verificar se o que usuário digitou pode ser convertido para numero
def is_number(val):
    return is_int(val) or is_float(val)

s_n = 's';
while s_n == 's':
    nota = input(f'Informe a primeira nota: ');
    if not is_number(nota):
        print(f'Isso não é um número!');
        continue;
    nota2 = input(f'Informe a segunda nota: ');
    if not is_number(nota2):
        print(f'Isso não é um número!');
        continue;
    nota3 = input(f'Informe a terceira nota: ');
    if not is_number(nota3):
        print(f'Isso não é um número!');
        continue;
    nota4 = input(f'Informe a quarta nota: ');
    if not is_number(nota4):
        print(f'Isso não é um número!');
        continue;
    nota = int(nota);
    nota2 = int(nota2);
    nota3 = int(nota3);
    nota4 = int(nota4);


    media = (nota + nota2 + nota3 + nota4) / 4
    print(f'As notas são: 1º {nota}, 2º {nota2}, 3º {nota3} e 4º {nota4}');
    print(f'A média da nota é {media}')
    s_n = input("Quer continuar? (s/n)");


