# Entrada de dados
estado = int(input("Digite o código do estado (1 a 5): "))
peso_ton = float(input("Digite o peso da carga (em toneladas): "))
codigo = int(input("Digite o código da carga (10 a 40): "))

# 1. Converter toneladas para quilos
peso_kg = peso_ton * 1000

# 2. Definir o preço por kg de acordo com o código
if 10 <= codigo <= 20:
    preco_kg = 100

elif 21 <= codigo <= 30:
    preco_kg = 250

else:  # 31 a 40
    preco_kg = 340

# 3. Calcular o preço da carga
preco_carga = peso_kg * preco_kg

# 4. Definir o percentual de imposto conforme o estado
if estado == 1:
    imposto_percentual = 35

elif estado == 2:
    imposto_percentual = 25

elif estado == 3:
    imposto_percentual = 15

elif estado == 4:
    imposto_percentual = 5

else:  # estado 5
    imposto_percentual = 0

# 5. Calcular o valor do imposto
imposto = preco_carga * (imposto_percentual / 100)

# 6. Calcular o valor total
total = preco_carga + imposto

# 7. Mostrar resultados
print("Peso da carga em kg:", peso_kg)
print("Preço da carga: R$", preco_carga)
print("Valor do imposto: R$", imposto)
print("Valor total: R$", total)