primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")

# # if primeiro_valor > segundo_valor:
# #     print ("O primeiro valor = ", primeiro_valor, "é maior que o segundo valor = ",segundo_valor)

# elif primero_valor < segundo_valor:
#     print ("O segundo valor = ",segundo_valor, "é maior que o segundo valor = ", primeiro_valor)

# elif primeiro_valor == segundo_valor:
#     print ("Os valores são iguais")

if primeiro_valor == segundo_valor:
    print ("Os valores são iguais")
elif primeiro_valor > segundo_valor:
    print (f"O primeiro valor = {primeiro_valor} é maior que o segundo valor = {segundo_valor}")
else: 
    print (f"O segundo valor {segundo_valor} é maior que o primeiro valor {primeiro_valor}")