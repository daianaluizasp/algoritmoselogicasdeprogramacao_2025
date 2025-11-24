senha_cadastrada = "123"

senha_digitada = input ("Digite sua senha: ")
quantidade_tentativas = 1

while senha_digitada != senha_cadastrada:
    senha_digitada = input ("Senha incorreta, tente novamente: ")
    quantidade_tentativas += 1
    print (quantidade_tentativas)
    if quantidade_tentativas >= 3:
        print ("usuario bloqueado por 5 minutos")
        break

print ("bem-vindo ao sistema!")