#f-strings

nome = "Davi Souza Antunes"
altura = 1.86
peso = 103
imc = peso / (altura * altura)

linha = f'{nome} tem {altura}m de altura, pesa {peso} e seu IMC é {imc:.2f}'

print (linha)
