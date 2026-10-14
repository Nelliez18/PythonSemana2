soma = 0 # Define a variavel soma como 0
maior = None # Define a variavel maior como nula
menor = None # Define a variavel menor como nula

for i in range(1, 6): # Inicia um loop pedindo 5 vezes
    numero = float(input(f"Digite o {i}º número: ")) # Pede um valor
    soma += numero # Faz a adição do numero inserido com a variavel soma
    
    if maior is None or numero > maior: # Define o primeiro número do loop como maior e confere se o numero inserido após é  maior que a variavel maior
        maior = numero # se for maior ele é substituido
    if menor is None or numero < menor: # Define o primeiro número do loop como menor e confere se o numero inserido é  menor que a variavel menor
        menor = numero # se for menor ele é substituido

media = soma / 5 # faz a média dos 5 números

print(f"\nSoma: {soma}") # Exibe a soma
print(f"Média: {media:.2f}") # Exibe a média
print(f"Maior valor: {maior}") # Exibe o maior valor
print(f"Menor valor: {menor}") # Exibe o menor valor

# EM PORTUGOL

# programa
# {
#     inclua biblioteca Matematica --> mat // Biblioteca para formatar as casas decimais da média
# 
#     funcao inicio()
#     {
#         // Declaração das variáveis
#         real soma = 0.0 // Define a variavel soma como 0
#         real maior = 0.0 // No Portugol, iniciamos com 0 e testamos a primeira volta do laço
#         real menor = 0.0
#         real numero, media
#         inteiro i
# 
#         // Inicia um loop pedindo 5 vezes (de 1 até 5, avançando de 1 em 1)
#         para (i = 1; i <= 5; i++)
#         {
#             escreva("Digite o ", i, "º número: ")
#             leia(numero) // Pede um valor
# 
#             soma = soma + numero // Faz a adição do numero inserido com a variavel soma
#             
#             // No Portugol não existe 'None'. Verificamos se é a primeira volta (i == 1) para definir os valores iniciais
#             se (i == 1 ou numero > maior) // Define o primeiro número do loop como maior e confere se o numero inserido após é maior que a variavel maior
#             {
#                 maior = numero // se for maior ele é substituido
#             }
# 
#             se (i == 1 ou numero < menor) // Define o primeiro número do loop como menor e confere se o numero inserido é menor que a variavel menor
#             {
#                 menor = numero // se for menor ele é substituido
#             }
#         }
# 
#         media = soma / 5 // faz a média dos 5 números
# 
#         // Saída de dados
#         escreva("\nSoma: ", soma) // Exibe a soma
#         escreva("\nMédia: ", mat.arredondar(media, 2)) // Exibe a média com 2 casas decimais
#         escreva("\nMaior valor: ", maior) // Exibe o maior valor
#         escreva("\nMenor valor: ", menor) // Exibe o menor valor
#     }
# }