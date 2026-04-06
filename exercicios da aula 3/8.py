salario = float(input("Digite o salário do colaborador: R$ "))

# Definindo percentual
if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
else:
    percentual = 5

# Cálculos
aumento = salario * (percentual / 100)
novo_salario = salario + aumento

# Saída
print(f"Salário antes do reajuste: R$ {salario:.2f}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")