

while True:
    print("Olá, Mundo")
    resposta = input("Deseja exibir novamente? (s/n): ").lower()
    if resposta != 's':
        print("Fim")
        break