# Programa Média por Sexo
soma_m = 0
cont_m = 0
soma_f = 0
cont_f = 0

for c in range(1, 11, 1):
    sexo = input('Digite o sexo (M/F): ')
    nota = float(input('Digite a nota: '))
    
    if sexo == 'M' or sexo == 'm':
        soma_m = soma_m + nota
        cont_m = cont_m + 1
    elif sexo == 'F' or sexo == 'f':
        soma_f = soma_f + nota
        cont_f = cont_f + 1

# Calculando e mostrando as médias (com verificação para evitar divisão por zero)
if cont_m > 0:
    media_m = soma_m / cont_m
    print('Média Masculina = ', media_m)

if cont_f > 0:
    media_f = soma_f / cont_f
    print('Média Feminina = ', media_f)
# final do programa