# Entrada de dados
estado = int(input("Digite o código do estado (1 a 5): "))
peso_ton = float(input("Digite o peso da carga (em toneladas): "))
codigo = int(input("Digite o código da carga (10 a 40): "))

# Converter toneladas para kg
peso_kg = peso_ton * 1000

# Definir preço por kg
if 10 <= codigo <= 20:
    preco_kg = 100
elif 21 <= codigo <= 30:
    preco_kg = 250
elif 31 <= codigo <= 40:
    preco_kg = 340
else:
    preco_kg = 0

# Calcular preço da carga
preco_carga = peso_kg * preco_kg

# Definir imposto por estado
if estado == 1:
    imposto = preco_carga * 0.35
elif estado == 2:
    imposto = preco_carga * 0.25
elif estado == 3:
    imposto = preco_carga * 0.15
elif estado == 4:
    imposto = preco_carga * 0.05
elif estado == 5:
    imposto = 0
else:
    imposto = 0

# Valor total
total = preco_carga + imposto

# Saída
print(f"Estado: {estado}")
print(f"Peso informado (toneladas): {peso_ton}")
print(f"Peso em kg: {peso_kg:.2f}")
print(f"Código da carga: {codigo}")
print(f"Preço da carga: R$ {preco_carga:.2f}")
print(f"Imposto: R$ {imposto:.2f}")
print(f"Valor total transportado: R$ {total:.2f}")
