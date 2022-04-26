carrinho = []

carrinho.append(('produto', 30))
carrinho.append(('produto1', 40))
carrinho.append(('produto2', 10))

total = sum([float(y) for x,y in carrinho])

print(carrinho)
print(total)