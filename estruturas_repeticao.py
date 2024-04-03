# ESTRUTURAS DE REPETIÇÃO

## FOR
texto = "Informe um texto: "
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()        
    print("Executa no final do laço")

for numero in range(0, 11):
    print(numero, end=" ")

print()

# Tabuada completa
for num in range(1, 6):
    print(f"Tabuada do {num}")
    for i in range(10):
        i += 1
        print(f"{num} x {i} = {num*i}")


## WHILE
opcao = 0 -1

while opcao != 3:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[3] Sair \n:"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")


while opcao != 3:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[3] Sair \n:"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por utilizar nosso sistema bancário!")


while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)