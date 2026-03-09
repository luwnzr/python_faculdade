# Programa Maior Preço
maior_preco = 0

for c in range(1, 21, 1):
    preco = float(input('Digite o preço do produto: '))
    
    if preco > maior_preco:
        maior_preco = preco

print('O maior preço é: ', maior_preco)
# final do programa