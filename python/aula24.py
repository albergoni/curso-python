# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
# nome = 'Otávio'
# print(nome[2])
# print(nome[-4])
# print('vio' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('zero' not in nome)

# nome = input('Digite seu nome: ')
# encontrar = input('Digite o que deseja encontrar: ')

# if encontrar in nome:
#     print(f'{encontrar} está em {nome}')
# else:
#     print(f'{encontrar} não está em {nome}')

# numero = 10

# if numero > 1:
#     if numero > 2:
#         if numero > 3:
#             print('Número maior que 3')
#         else:
#             print('Número menor que 3')
#     else:
#         print('Número menor que 2')
# else:
#     print('Número menor que 1')

numero = int(input ("Digite um número:")) 

if not (numero == 0):
    if  (numero < 10 and numero > 1): 
        print (f"O número {numero} está entre 1 e 10!!!")
    else:
        print (f"O número {numero} está abaixo de 1 ou acima de 10")
    print (f"O número digitado foi {numero}")
else:
    print ("Você digitou ZERO!")