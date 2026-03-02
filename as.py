valida_login = 0
# Criar usuário e senha
print ("################################################")
print("\n")
print("\n Bem-vindo! Faça seu cadastro ")

# Solicitar login ao usuário
valida_usuario = input("\n Crie seu nome de usuário: ")
while True:
    try:
        valida_senha = int(input("\nDigite sua senha:"))
        break
    except ValueError:
        print("\n A senha deve conter apenas números")

# Validar as entradas

# Se informações corretas: redirecionar para a tela de login
    print("\n redirecionando para a tela de login...")
while valida_login == 0:
    usuario = input("\n Digite seu nome de usuário: ")
    while True:
        try:
            senha = int(input("\n Digite sua senha:"))
            break
        except ValueError:
            print("A senha deve conter apenas números") 
    if usuario == valida_usuario and senha == valida_senha:
        print("\n Login concluído com sucesso!")
        valida_login = 1
    else: 
        print("\n Usuário ou senha incorretos. Tente novamente!")
print("\n") 
print ("################################################")      

# Se não, redefinir a senha