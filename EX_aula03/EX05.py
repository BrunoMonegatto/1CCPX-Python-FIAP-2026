print("Você deverá inserir 5 números")

# Primeiro número
maior = float(input("Insira o primeiro número: "))

# Os outros 4 números
for i in range(4):
    numero = float(input("Insira um número: "))

    if numero > maior:
        maior = numero

print(f"O maior número digitado foi {maior}")