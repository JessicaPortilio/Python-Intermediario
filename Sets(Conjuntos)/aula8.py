# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

s1 = {1,2,3,4,5}
print(s1)

for v in s1:
    print(v)

s2 = set() #se quiser criar um set(conjuto) vazio é assim
s2.add(1)
s2.add(2)
print(s2)
s2.discard(2)
print(s2)
s2.update('a')
print(s2)
s2.update('PYTHON')
print(s2)
s2.update([1,2,3,4,5], {5,6,7,8})
print(s2)

#observação o set não aceita elemento duplicado

l1 = [1,2,1,1,3,4,5,6,6,6,6,6,6,6,7,8,9,'Luiz','Luiz']
l1 = set(l1)
l1 = list(l1)

print(l1)

s3 = {1,2,3,4,5,7}
s4 = {1,2,3,4,5,6}
s5 = s3 | s4
print(s5)

s5 = s3 & s4 #Que tem em ambos set(conjuto)

print(s5)

s5 = s3 - s4 #só o que tem no set(conjunto) da esquerda

print(s5)

s5 = s3 ^ s4 #Só pega o que não tem em um e nem no outro

print(s5)

l3 = ['Maria', 'Carlos', 'Pedro']
l4 = ['Pedro', 'Carlos', 'Maria',
      'Pedro', 'Pedro', 'Pedro','Pedro']



if set(l3) == set(l4):
    print('L3 é igual L4')
else:
    print('L3 é diferente L4')