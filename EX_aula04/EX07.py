n = int(input("Digite um número positivo: "))

while n <= 0:
    print("Valor inválido! Digite um número positivo.")
    n = int(input("Digite um número positivo: "))

soma = 0

for i in range(1, n + 1):
    soma += i

print(f"A soma de 1 até {n} é: {soma}")