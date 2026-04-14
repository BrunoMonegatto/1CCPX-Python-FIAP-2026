# Lê dois números inteiros
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

# Verifica se são múltiplos
# Se A dividido por B ou B dividido por A tiver resto 0, então são múltiplos
if a % b == 0 or b % a == 0:
    print("São Múltiplos")
else:
    print("Não são Múltiplos")