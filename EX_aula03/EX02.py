# Lê um número digitado pelo usuário
numero = int(input("Digite um número: "))

# Verifica se o número é divisível por 2
# Se o resto da divisão por 2 for 0, ele é par
if numero % 2 == 0:
    print("O número é PAR")
else:
    print("O número é ÍMPAR")