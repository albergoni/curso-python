"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input ("Digite seu nome: ")
idade = input ("Digite sua idade: ")
letras = int(len (nome))

# if len (nome) == 0: 
#     print ("Você precisa digitar um nome para continuar")
# else:
#     print (f"O seu nome é: {nome}")
if len (nome) != 0:
    if len (idade) != 0:
        print (f"Seu nome é {nome} e sua idade é {idade}"),
        print (f"Seu nome invertido é: {nome[::-1]}")
        print (f"Seu nome possui {letras} letras")
        print (f"A primeira letra do seu nome é {nome[0]}")
        print (f"A última letra do seu nome é {nome[-1]}")
        if " " in nome: 
            print ("O seu nome contém espaço")
        else:
            print ("Seu nome não contém espaço")
    else: 
        print ("Você não digitou seu nome ou idade. Infelizmente não é possível continuar")
else: 
    print ("Você não digitou seu nome ou idade. Infelizmente não é possível continuar")


# nome = input('Digite o seu nome: ')
# idade = input('Digite sua idade: ')

# if nome and idade:
#     print(f'Seu nome é {nome}')
#     print(f'Seu nome invertido é {nome[::-1]}')

#     if ' ' in nome:
#         print('Seu nome contém espaços')
#     else:
#         print('Seu nome NÃO contém espaços')

#     print(f'Seu nome tem {len(nome)} letras')
#     print(f'A primeira letra do seu nome é {nome[0]}')
#     print(f'A última letra do seu nome é {nome[-1]}')
# else:
#     print("Desculpe, você deixou campos vazios.")