A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

if A == 0 or B == 0:
    print("Não é possível verificar com zero")
elif A % B == 0 or B % A == 0:
    print("São Múltiplos")
else:
    print("Não são Múltiplos")
