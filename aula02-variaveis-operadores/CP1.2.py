nome = input("Digite nome do colaborador: ")
hora = float(input("Digite o valor da hora trabalhada: "))
hora_mes = float(input("Digite a quantidade de horas trabalhadas no mês: "))
bonus = float(input("Digite o bônus fixo do mês: "))

percentual_desconto = input("Digite o desconto fixo do mês (ex: 10%): ")
percentual_desconto = percentual_desconto.replace("%", "")  # remove o %
percentual_desconto = float(percentual_desconto)

salario_bruto = (hora * hora_mes) + bonus
salario_liquido = (salario_bruto * percentual_desconto) /100

print(f"A colaboradora é {nome}")
print(f"O salário bruto é {salario_bruto}")
print(f"O salário líquido é  {salario_liquido}")