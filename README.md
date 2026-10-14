Exercício Guiado 1: Situação acadêmica
```python
nota = float(input("Digite a nota: "))
if nota >= 7:
  print("Aprovado")
elif nota >= 5:
  print("Recuperação")
else:
  print("Reprovado")
```
Exercício Guiado 2: Operações
```python
opcao = int(input("Escolha (1-3): "))
match opcao:
  case 1:
    print("Somando...")
  case 2:
    print("Subtraindo...")
  case 3:
    print("Multiplicando...")
  case _:
    print("Opção inválida")
```
Exercício Guiado 3: Repetição com for
```python
for i in range(1, 11):
  print(i)
```
Exercício Guiado 4: Repetição com while
```python
n = int(input("Digite um número (0 para sair): "))

while n != 0:
  print(f"Você digitou: {n}")
  n = int(input("Digite outro número: "))
```
Prática Independente

IF / ELIF / ELSE — Receber idade e renda e classificar o
cliente como: Bronze, Prata, Ouro, Diamante - Criar
versão em Portugol e Python.
```python
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
```
CASE — Criar um menu com 4 operações
matemáticas e executar a escolhida. Versão em
Portugol e Python (match-case).
```python
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
```
FOR — Ler 5 números e calcular: soma, média, maior,
menor, Versão em Portugol e Python.
```python
def analisar_cinco_numeros():
    """Lê 5 números e calcula soma, média, maior e menor valor."""
    numeros = []
    
    for i in range(5):
        num = float(input(f"Digite o {i+1}º número: "))
        numeros.append(num)
        
    soma = sum(numeros)
    media = soma / 5
    maior = max(numeros)
    menor = min(numeros)
    
    print(f"Soma: {soma} | Média: {media} | Maior: {maior} | Menor: {menor}")

# Para rodar: analisar_cinco_numeros()
```

```portugol
programa {
    funcao inicio() {
        real num, soma = 0.0, media, maior, menor
        inteiro i
        
        para (i = 1; i <= 5; i++) {
            escreva("Digite o ", i, "º número: ")
            leia(num)
            
            soma = soma + num
            
            se (i == 1) {
                maior = num
                menor = num
            } senao {
                se (num > maior) { maior = num }
                se (num < menor) { menor = num }
            }
        }
        media = soma / 5
        escreva("Soma: ", soma, " | Média: ", media, " | Maior: ", maior, " | Menor: ", menor)
    }
}

```
WHILE — Criar um sistema que: pede senha até o
usuário acertar. conta tentativas; bloqueia após 3 erros.
Versão em Portugol e Python.
```python
def sistema_login():
    """Valida a senha do usuário com limite de 3 tentativas."""
    senha_correta = "python123"
    tentativas = 0
    max_tentativas = 3
    
    while tentativas < max_tentativas:
        senha_digitada = input("Digite a senha: ")
        tentativas += 1
        
        if senha_digitada == senha_correta:
            print("Acesso concedido!")
            return True
            
        print(f"Senha incorreta! Tentativas restantes: {max_tentativas - tentativas}")
        
    print("Acesso bloqueado! Você excedeu 3 tentativas.")
    return False

# Para rodar: sistema_login()
```

```portugol
programa {
    funcao inicio() {
        cadeia senha_correta = "python123"
        cadeia senha_digitada
        inteiro tentativas = 0
        logico acessou = falso
       
        enquanto (tentativas < 3 e acessou == falso) {
            escreva("Digite a senha: ")
            leia(senha_digitada)
            tentativas = tentativas + 1
            
            se (senha_digitada == senha_correta) {
                escreva("Acesso concedido!")
                acessou = verdadeiro
            } senao {
                escreva("Senha incorreta! Tentativas usadas: ", tentativas, "/3\n")
            }
        }
        
        se (acessou == falso) {
            escreva("Acesso bloqueado! Você excedeu 3 tentativas.")
        }
    }
}

```
Mini-desafios Bônus
Criar um programa que:
1. Usa if/elif/else para validar idade mínima (≥ 18).
2. Usa case/match para escolher o tipo de cadastro:
1. 1 = Aluno
2. 2 = Professor
3. 3 = Funcionário
3. Usa for para registrar N cadastros.
4. Usa while para permitir que o usuário continue cadastrando até digitar “sair”.
Saída esperada:
• Quantidade total de cadastros
• Quantidade por categoria
• Lista dos nomes cadastrados
```python
def sistema_cadastro():
    """Gerencia o cadastro de usuários validando idade e categoria."""
    # Inicialização dos contadores e listas
    total_cadastros = 0
    categorias = {"Aluno": 0, "Professor": 0, "Funcionário": 0}
    nomes_cadastrados = []

    print("=== SISTEMA DE CADASTRO ===")

    # 4. WHILE — Loop principal que roda até o usuário digitar 'sair'
    while True:
        comando = input("\nDigite 'prosseguir' para cadastrar ou 'sair' para encerrar: ").strip().lower()
        
        if comando == "sair":
            break
        elif comando != "prosseguir":
            print("Opção inválida! Digite 'prosseguir' ou 'sair'.")
            continue

        # 3. FOR — Pede quantos cadastros serão feitos nesta rodada
        try:
            quantidade_rodada = int(input("Quantos cadastros deseja realizar nesta rodada? "))
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
            continue

        for i in range(quantidade_rodada):
            print(f"\n--- Cadastro {i + 1} de {quantidade_rodada} ---")
            nome = input("Nome completo: ").strip()
            
            try:
                idade = int(input("Idade: "))
            except ValueError:
                print("Idade inválida! Cadastro cancelado para este registro.")
                continue

            # 1. IF / ELIF / ELSE — Validação de idade mínima
            if idade < 18:
                print(f"Cadastro recusado: {nome} tem menos de 18 anos.")
                continue  # Pula para o próximo ciclo do FOR

            print("Categorias disponíveis:\n1 = Aluno\n2 = Professor\n3 = Funcionário")
            opcao_categoria = input("Escolha a categoria (1-3): ").strip()

            # 2. CASE / MATCH — Atribuição do tipo de cadastro
            match opcao_categoria:
                case "1":
                    tipo = "Aluno"
                case "2":
                    tipo = "Professor"
                case "3":
                    tipo = "Funcionário"
                case _:
                    print("Categoria inválida! Cadastro cancelado para este registro.")
                    continue

            # Atualização dos dados após validação completa
            categorias[tipo] += 1
            total_cadastros += 1
            nomes_cadastrados.append(f"{nome} ({tipo})")
            print(f"Sucesso: {nome} cadastrado como {tipo}!")

    # Exibição do relatório final (Saída esperada)
    print("\n" + "="*30)
    print("       RELATÓRIO FINAL        ")
    print("="*30)
    print(f"Quantidade total de cadastros: {total_cadastros}")
    print("\nQuantidade por categoria:")
    for cat, qtd in categorias.items():
        print(f" - {cat}: {qtd}")
    
    print("\nLista dos nomes cadastrados:")
    if nomes_cadastrados:
        for nome_completo in nomes_cadastrados:
            print(f" • {nome_completo}")
    else:
        print(" • Nenhum usuário cadastrado.")
    print("="*30)

# Para executar o programa:
if __name__ == "__main__":
    sistema_cadastro()

```
```portugol
programa {
    funcao inicio() {
        cadeia comando = ""
        cadeia nome, tipo
        inteiro idade, opcao_categoria, quantidade_rodada, i
        
        // Contadores e armazenamento de dados
        inteiro total_cadastros = 0
        inteiro qtd_aluno = 0, qtd_professor = 0, qtd_funcionario = 0
        cadeia nomes_cadastrados[100] // Vetor com limite inicial seguro de 100 posições
        
        escreva("=== SISTEMA DE CADASTRO ===\n")
        
        // 4. WHILE — Loop principal baseado na palavra-chave
        enquanto (comando != "sair") {
            escreva("\nDigite 'prosseguir' para cadastrar ou 'sair' para encerrar: ")
            leia(comando)
            
            se (comando == "sair") {
                pare
            } senao se (comando == "prosseguir") {
                escreva("Quantos cadastros deseja realizar nesta rodada? ")
                leia(quantidade_rodada)
                
                // 3. FOR — Laço estruturado para N cadastros
                para (i = 1; i <= quantidade_rodada; i++) {
                    escreva("\n--- Cadastro ", i, " de ", quantidade_rodada, " ---\n")
                    escreva("Nome completo: ")
                    leia(nome)
                    escreva("Idade: ")
                    leia(idade)
                    
                    // 1. IF / ELIF / ELSE — Validação de maioridade
                    se (idade < 18) {
                        escreva("Cadastro recusado: ", nome, " tem menos de 18 anos.\n")
                    } senao {
                        escreva("Categorias disponíveis:\n1 = Aluno\n2 = Professor\n3 = Funcionário\n")
                        escreva("Escolha a categoria (1-3): ")
                        leia(opcao_categoria)
                        
                        logico cadastro_valido = verdadeiro
                        
                        // 2. CASE — Seleção do perfil
                        escolha (opcao_categoria) {
                            caso 1:
                                tipo = "Aluno"
                                qtd_aluno = qtd_aluno + 1
                                pare
                            caso 2:
                                tipo = "Professor"
                                qtd_professor = qtd_professor + 1
                                pare
                            caso 3:
                                tipo = "Funcionário"
                                qtd_funcionario = qtd_funcionario + 1
                                pare
                            caso contrario:
                                escreva("Categoria inválida! Registro cancelado.\n")
                                cadastro_valido = falso
                                pare
                        }
                        
                        se (cadastro_valido) {
                            nomes_cadastrados[total_cadastros] = nome + " (" + tipo + ")"
                            total_cadastros = total_cadastros + 1
                            escreva("Sucesso: ", nome, " cadastrado como ", tipo, "!\n")
                        }
                    }
                }
            } senao {
                escreva("Opção inválida!\n")
            }
        }
        
        // Saída esperada (Relatório)
        escreva("\n==============================")
        escreva("\n       RELATÓRIO FINAL        ")
        escreva("\n==============================")
        escreva("\nQuantidade total de cadastros: ", total_cadastros)
        escreva("\n\nQuantidade por categoria:")
        escreva("\n - Aluno: ", qtd_aluno)
        escreva("\n - Professor: ", qtd_professor)
        escreva("\n - Funcionário: ", qtd_funcionario)
        
        escreva("\n\nLista dos nomes cadastrados:\n")
        se (total_cadastros == 0) {
            escreva(" • Nenhum usuário cadastrado.\n")
        } senao {
            para (i = 0; i < total_cadastros; i++) {
                escreva(" • ", nomes_cadastrados[i], "\n")
            }
        }
        escreva("==============================\n")
    }
}
```
