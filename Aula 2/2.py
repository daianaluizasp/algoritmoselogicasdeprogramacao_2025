numero = int (input("Digite o numero para fatorial"))

contador = 1
fatorial = 1

while contador <= numero:
    fatorial = fatorial * contador
    contador += 1
print (f"O fatorial de {numero} é: {fatorial}")