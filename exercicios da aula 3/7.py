from datetime import datetime

# Ano atual
ano_atual = datetime.now().year

# Entrada
ano_nascimento = int(input("Digite o ano de nascimento: "))

# Cálculo da idade
idade = ano_atual - ano_nascimento

print(f"Ano de nascimento: {ano_nascimento}")
print(f"Idade: {idade}")

# Verificação do tipo de voto
if idade < 16:
    print("Voto proibido")
elif 16 <= idade < 18 or idade >= 70:
    print("Voto opcional")
else:
    print("Voto obrigatório")