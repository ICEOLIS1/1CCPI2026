#LOGICA E (AND)
#EMAIL          SENHA           LOGIN(RESULTADO)
#TRUE            TRUE            True
#TRUE           FALSE           FALSE
#FALSE          TRUE            FALSE
#FALSE          FALSE           FALSE

verifica_email = True
verifica_senha = True
verifica_login = verifica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print("entra no programa... executa...")

#lógica ou (or)
logica_ou = False or False or False
print(logica_ou)
#operador de negação (not)
negação = not False
print (negação)
if not verifica_login:
    print ("loga ai...")


