"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

#PROGRAMA 1
numero_digitado = input ("Digite um número inteiro:")
try:
    numero = int (numero_digitado)
    if numero % 2 == 0:
        print (f"O número {numero} é par")
    else:
        print (f"O número {numero} é ímpar")
    ...
except:
    print ("Você não digitou um número inteiro")
    ...
# #PROGRAMA 2
# horas = input ("Que horas são? Digite o horário correto, por favor:")

# #PROGRAMA 3
nome = input ("Digite seu primeiro nome:")
nome_int = len(nome)
if nome_int <= 4: 
    print ("Seu nome é curto")
elif nome_int == 5 or nome_int == 6:
    print ("Seu nome é normal")
else:
    print ("Seu nome é comprido")