""" PROPOSTA DE EXERCICIO
SOMA TODOS OS ITENS ADICIONADOS AO CARRINHO
USANDO LIST COMPRENHENSION
"""
carrinho = []

carrinho.append(('Skate', 90))
carrinho.append(('Café', 5))
carrinho.append(('Teclado', 220))
carrinho.append(('Mouse', 70))

soma = 0
for p, v in carrinho:
    soma += v

print(f'Soma ultilizando for :{soma}')

valor_total = sum([v[1] for v in carrinho])

print(f'Valor ultilizando list comp: {valor_total}') 