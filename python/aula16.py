# digitacao = input ('Digite um número:')
# numero = int(digitacao) 
# par = (numero % 2) == 0 
# if par == True:
#     print ("o número digitado é par")
# elif par == False:
#     print ("O número digitado é ímpar")
# else:  
#     print ("Você não digitou um número")

# if / elif      / else
# se / se não se / se não
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')

    print(12341234)
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair.')

print('FORA DOS BLOCOS')