# Importa o ano atual
from datetime import datetime

# Pega o ano atual automaticamente
ano_atual = datetime.now().year

# Lê o ano de nascimento
ano_nascimento = int(input("Digite seu ano de nascimento: "))

# Calcula a idade
idade = ano_atual - ano_nascimento

# Verifica a situação do voto
if idade < 16:
    print("Voto proibido")

elif idade == 16 or idade == 17 or idade >= 70:
    print("Voto opcional")

else:
    print("Voto obrigatório")