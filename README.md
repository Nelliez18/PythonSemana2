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
