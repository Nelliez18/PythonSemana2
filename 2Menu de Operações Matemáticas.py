num1 = float(input("Digite o primeiro número: ")) # Define o primeiro número
num2 = float(input("Digite o segundo número: ")) # Define o segundo número

print("\n--- MENU DE OPERAÇÕES ---\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão") # Exibe o menu
opcao = int(input("Escolha uma opção (1-4): ")) 

match opcao: # Define o menu vinculado a opção
    case 1: # Cria a primeira opção do menu
        print(f"Resultado: {num1 + num2}") # Define 1 como soma e exibe o resultado
    case 2: # Cria a segunda opção do menu
        print(f"Resultado: {num1 - num2}") # Define 2 como subtração e exibe o resultado
    case 3: # Cria a terceira opção do menu
        print(f"Resultado: {num1 * num2}") # Define 3 como multiplicação e exibe o resultado
    case 4: # Cria a quarta opção do menu
        if num2 != 0: # Verifica se o num2 não é 0
            print(f"Resultado: {num1 / num2}") # Define 4 como Divisão e exibe o resultado
        else:
            print("Erro: Divisão por zero!") 
    case _:
        print("Opção inválida!") # Da como invalido qualquer resposta que não seja 1, 2, 3 ou 4

# EM PORTUGOL

# programa
# {
#     funcao inicio()
#     {
#         // Declaração das variáveis
#         real num1, num2
#         inteiro opcao
# 
#         // Entrada de dados para os números
#         escreva("Digite o primeiro número: ")
#         leia(num1) // Define o primeiro número
# 
#         escreva("Digite o segundo número: ")
#         leia(num2) // Define o segundo número
# 
#         // Exibe o menu
#         escreva("\n--- MENU DE OPERAÇÕES ---\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n")
#         escreva("Escolha uma opção (1-4): ")
#         leia(opcao)
# 
#         // Estrutura de escolha (equivalente ao match/case do Python)
#         escolha (opcao) // Define o menu vinculado a opção
#         {
#             caso 1: // Cria a primeira opção do menu
#                 escreva("Resultado: ", num1 + num2) // Define 1 como soma e exibe o resultado
#                 pare
#                 
#             caso 2: // Cria a segunda opção do menu
#                 escreva("Resultado: ", num1 - num2) // Define 2 como subtração e exibe o resultado
#                 pare
#                 
#             caso 3: // Cria a terceira opção do menu
#                 escreva("Resultado: ", num1 * num2) // Define 3 como multiplicação e exibe o resultado
#                 pare
#                 
#             caso 4: // Cria a quarta opção do menu
#                 se (num2 != 0) // Verifica se o num2 não é 0
#                 {
#                     escreva("Resultado: ", num1 / num2) // Define 4 como Divisão e exibe o resultado
#                 }
#                 senao
#                 {
#                     escreva("Erro: Divisão por zero!")
#                 }
#                 pare
#                 
#             caso contrario:
#                 escreva("Opção inválida!") // Da como invalido qualquer resposta que não seja 1, 2, 3 ou 4
#         }
#     }
# }