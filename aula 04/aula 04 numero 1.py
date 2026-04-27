def validar_nota (nota):
    while nota < 0 or nota > 10:
        print("A nota deve estar entre 0 e 10")
    nota = float(input('digite novamente a nota:'))
    return nota

    notaA = float(input("digite a 1' nota :"))
    notaA = validar_nota (notaA)



notaA = float(input("digite a 1' nota: "))
while notaA < 0 or notaA >10:
    print ("A nota deve estar entre 0 e 10")
notaA = float (input('digite novamente a nota:'))