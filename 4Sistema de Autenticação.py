senha_correta = "1234" # Define a senha
tentativas = 0 # Define quantidade de tentativas

while tentativas < 3: # Define limite de tentativas no loop
    senha_digitada = input("Digite a senha: ") # pede a senha 
    tentativas += 1 # computa a  tentativa
    
    if senha_digitada == senha_correta: # Confere se a senha inserida é a correta
        print("Acesso Permitido!") # se sim, exibe que foi a correta
        break # encerra o loop 
    else: # Confere se a senha foi inserida corretamente
        print(f"Senha Incorreta. Tentativa {tentativas} de 3.") # Se não, exibe que a senha era incorreta
else: # Confere se a senha foi colocada corretamente após as 3 tentativas/break
    print("Acesso Bloqueado após 3 erros.") # Se não, exibe que o acesso foi bloqueado 


# EM PORTUGOL

# programa
# {
#     funcao inicio()
#     {
#         // Declaração das variáveis
#         cadeia senha_correta = "1234" // Define a senha
#         cadeia senha_digitada
#         inteiro tentativas = 0 // Define quantidade de tentativas
#         logico acesso_permitido = falso // Variável de controle auxiliar para o break/fim do loop
# 
#         // Define limite de tentativas no loop
#         enquanto (tentativas < 3 e acesso_permitido == falso)
#         {
#             escreva("Digite a senha: ")
#             leia(senha_digitada) // pede a senha
#             tentativas = tentativas + 1 // computa a tentativa
# 
#             se (senha_digitada == senha_correta) // Confere se a senha inserida é a correta
#             {
#                 escreva("Acesso Permitido!\n") // se sim, exibe que foi a correta
#                 acesso_permitido = verdadeiro // Define que deu certo para encerrar o loop
#             }
#             senao // Confere se a senha foi inserida corretamente
#             {
#                 escreva("Senha Incorreta. Tentativa ", tentativas, " de 3.\n") // Se não, exibe que a senha era incorreta
#             }
#         }
# 
#         // Confere se a senha foi colocada corretamente após as 3 tentativas (equivalente ao else do while no Python)
#         se (acesso_permitido == falso)
#         {
#             escreva("Acesso Bloqueado após 3 erros.\n") // Se não, exibe que o acesso foi bloqueado
#         }
#     }
# }