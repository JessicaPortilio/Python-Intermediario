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

num = input(f'Iforme um número: ');
num2 = input(f'Iforme o segundo número: ');
if is_number(num) and is_number(num2):
    num = int(num);
    num2 = int(num2);
    soma = num + num2
    print(f'{soma}');
else:
    print(f'Isso não é um número');
