# Lê os três lados
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

# Coloca os valores em ordem decrescente (maior para menor)
lados = sorted([a, b, c], reverse=True)

A, B, C = lados  # Agora A é o maior

# Verifica se forma triângulo
if A >= B + C:
    print("NAO FORMA TRIANGULO")

else:
    # Verifica o tipo quanto aos ângulos
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")

    elif A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")

    elif A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")

    # Verifica o tipo quanto aos lados
    if A == B == C:
        print("TRIANGULO EQUILATERO")

    elif A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")