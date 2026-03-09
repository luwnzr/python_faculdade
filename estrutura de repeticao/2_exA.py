# Programa  Recebe o Preço de 30 Produtos e Mostra o Total a ser Pago
c = 0
soma = 0
while c < 30:
    c = c + 1
    preco = float(input ('Digite o preço do produto: '))
    soma = soma + preco
print('Total =', soma )