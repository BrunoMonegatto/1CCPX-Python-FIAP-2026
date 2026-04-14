print("Você deverá inserir 5 números para a soma")

soma = 0

for i in range(5):
    numero = float(input("Insira um número: "))
    soma = soma + numero

print(f"O resultado da soma dos 5 números é {soma}")