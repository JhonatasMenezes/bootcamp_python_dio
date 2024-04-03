# ESTRUTURAS DCONDICIONAIS

## IF simples
MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")
else:
    print("Ainda não pode tirar CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer as aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar CNH.")


## IF aninhado
conta_normal = True
conta_universitaria = False

saldo = 2000
saque1, saque2 = 1500, 2450
cheque_especial = 450

if conta_normal:

    if saque1 <= saldo:
        print("Saque realizado com sucesso!")
    elif saque2 <= saldo:
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente!")
elif conta_universitaria:

    if saque1 <= saldo:
        print("Saque realizado com sucesso!")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente!")
else:

    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente!")


## IF ternário
status = "Sucesso" if saldo >= saque1 else "Falha"
print(f"{status} ao realizar o saque!")


