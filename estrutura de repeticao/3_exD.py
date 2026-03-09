# Programa Classificação de Idades
criancas = 0
jovens = 0
adultos = 0

for c in range(1, 21, 1):
    idade = int(input('Digite a idade: '))
    
    if idade <= 13:
        criancas = criancas + 1
    elif idade >= 14 and idade <= 24:
        jovens = jovens + 1
    elif idade > 24:
        adultos = adultos + 1

print('Quantidade de Crianças: ', criancas)
print('Quantidade de Jovens: ', jovens)
print('Quantidade de Adultos: ', adultos)
# final do programa