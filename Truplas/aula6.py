t1 = (1,2,3, 'a', 'Jessica')
t2 = []

print(type(t1))
print(type(t2))
print(t1[2])

for v in t1:
    print(v)

print(t1[:4])

t4 = 1,2,'Jessica', 'b'
t5 = 3,4,5,6
t6 = t4 + t5

print(t6)

n1, n2, n3, *_ = t4
print(n3)

#Truplas não tem como editar então se eu precisar editar tenho que fazer assim
tr1 = (1,2,3,4,5)
tr1 = list(tr1) #transformei em lista
tr1[3] = 3
tr1 = tuple(tr1) #retorna ele para trupla
print(tr1)
