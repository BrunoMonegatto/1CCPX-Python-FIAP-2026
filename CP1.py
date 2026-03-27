produto = input("Digite o produto: ")
preco_unitario = float(input("Digite o preço unitário: "))
quantidade = int(input("Digite a quantidade: "))

percentual_desconto = input("Digite o percentual de desconto (ex: 10%): ")
percentual_desconto = percentual_desconto.replace("%", "")  # remove o %
percentual_desconto = float(percentual_desconto)

valor_bruto = preco_unitario * quantidade
valor_desconto = (valor_bruto * percentual_desconto) / 100
valor_final = valor_bruto - valor_desconto

print(f"O produto é {produto}")
print(f"O valor bruto é {valor_bruto}")
print(f"O desconto é de {percentual_desconto}% que dá {valor_desconto}")
print(f"O valor final será {valor_final}")