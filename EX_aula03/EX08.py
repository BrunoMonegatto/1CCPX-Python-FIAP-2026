# Lê o salário do colaborador
salario = float(input("Digite o salário: "))

# Verifica a faixa salarial e define o percentual
if salario <= 280:
    percentual = 20

elif salario <= 700:
    percentual = 15

elif salario <= 1500:
    percentual = 10

else:
    percentual = 5

# Calcula o valor do aumento
aumento = salario * (percentual / 100)

# Calcula o novo salário
novo_salario = salario + aumento

# Mostra os resultados
print("Salário antes do reajuste: R$", salario)
print("Percentual de aumento:", percentual, "%")
print("Valor do aumento: R$", aumento)
print("Novo salário: R$", novo_salario)
