idade = int(input("Digite a idade do cliente: ")) #  Define idade
renda = float(input("Digite a renda do cliente: ")) # Define renda

if renda <= 3000.0: # Confere se a renda é menor ou igual a 3000
    categoria = "Bronze" # Se sim, define Bronze
elif renda <= 6000.0: # Confere se a renda é menor ou igual a 6000
    categoria = "Prata" # Se sim, define Prata
elif renda <= 12000.0: # Confere se a renda é menor ou igual a 12000
    categoria = "Ouro" # Se sim, define Ouro
else: # Confere se as exigencias do anterior foram atendidas
    categoria = "Diamante" # Se não, define Diamante

print(f"Categoria: {categoria}") # Exibe o a categoria

# EM PORTUGOL

# programa
# {
#     funcao inicio()
#     {
#         // Declaração das variáveis
#         inteiro idade
#         real renda
#         cadeia categoria
# 
#         // Entrada de dados
#         escreva("Digite a idade do cliente: ")
#         leia(idade) // Define idade
# 
#         escreva("Digite a renda do cliente: ")
#         leia(renda) // Define renda
# 
#         // Estrutura condicional para definir a categoria
#         se (renda <= 3000.0) // Confere se a renda é menor ou igual a 3000
#         {
#             categoria = "Bronze" // Se sim, define Bronze
#         }
#         senao se (renda <= 6000.0) // Confere se a renda é menor ou igual a 6000
#         {
#             categoria = "Prata" // Se sim, define Prata
#         }
#         senao se (renda <= 12000.0) // Confere se a renda é menor ou igual a 12000
#         {
#             categoria = "Ouro" // Se sim, define Ouro
#         }
#         senao // Confere se as exigências do anterior foram atendidas
#         {
#             categoria = "Diamante" // Se não, define Diamante
#         }
# 
#         // Saída de dados
#         escreva("Categoria: ", categoria) // Exibe a categoria
#     }
# }