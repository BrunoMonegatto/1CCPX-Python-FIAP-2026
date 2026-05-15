temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

maior_risco = 0
sala_maior_risco = 0

for i in range(len(temperaturas)):

    sala = temperaturas[i]

    soma = 0
    registros_criticos = 0

    for temp in sala:

        soma += temp

        if temp >= 33:
            registros_criticos += 1

    media = soma / len(sala)

    print(f"Sala {i + 1}")
    print(f"Média: {media}")
    print(f"Registros críticos: {registros_criticos}")
    print()

    if registros_criticos > maior_risco:
        maior_risco = registros_criticos
        sala_maior_risco = i + 1

print(f"Sala com maior risco: Sala {sala_maior_risco}")