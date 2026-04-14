# Pede o primeiro número
num1 = int(input("Digite o primeiro número: "))

# Pede o segundo número
num2 = int(input("Digite o segundo número: "))

# Verifica qual é maior
if num1 > num2:
    print("O maior número é:", num1)

# Verifica se o segundo é maior
elif num2 > num1:
    print("O maior número é:", num2)

# Caso sejam iguais
else:
    print("Os dois números são iguais")