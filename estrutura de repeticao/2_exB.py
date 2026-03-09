# Programa Contador de Sexo
c = 0
homens = 0
mulheres = 0

while c < 20:
    c = c + 1
    sexo = input('Digite o sexo da pessoa (M para Masculino, F para Feminino): ')
    
    # Verifica se o que foi digitado foi M (maiúsculo) ou m (minúsculo)
    if sexo == 'M' or sexo == 'm':
        homens = homens + 1
    
    # Verifica se o que foi digitado foi F (maiúsculo) ou f (minúsculo)
    elif sexo == 'F' or sexo == 'f':
        mulheres = mulheres + 1

print('Quantidade de homens = ', homens)
print('Quantidade de mulheres = ', mulheres)
# final do Programa