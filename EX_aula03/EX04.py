# Lê as quatro notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3 + nota4) / 4

# Mostra a média
print("Média:", media)

# Verifica a situação do aluno
if media >= 7:
    print("Aprovado")

elif media >= 5:
    print("Em recuperação")

else:
    print("Reprovado")