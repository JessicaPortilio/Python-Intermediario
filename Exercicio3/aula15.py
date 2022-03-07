carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

print(carrinho[0][1])


total = 0
for produto in carrinho:
    total += produto[1]

print(total)

total = []
for produto in carrinho:
    total.append(produto[1])

print(sum(total))

produto, preco = carrinho[0]
print(produto, preco)

total2 = [(x , y) for x, y in carrinho]
print(total2)

#RESOLUÇÃO
total2 = sum([y for x, y in carrinho])
print(total2)

#Posso transforma o valor em um float se eu quiser
total2 = sum([float(y) for x, y in carrinho])
print(total2)
