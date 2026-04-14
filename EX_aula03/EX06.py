# Lê dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Lê a operação (+, -, *, /)
operacao = input("Digite a operação (+, -, *, /): ")

# Verifica qual operação foi escolhida
if operacao == "+":
    resultado = num1 + num2

elif operacao == "-":
    resultado = num1 - num2

elif operacao == "*":
    resultado = num1 * num2

elif operacao == "/":
    # Verifica se não vai dividir por zero
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: divisão por zero")
        resultado = None

else:
    print("Operação inválida")
    resultado = None

# Mostra o resultado se for válido
if resultado is not None:
    print("Resultado:", resultado)