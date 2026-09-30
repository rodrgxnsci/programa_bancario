
saldo = 0
limite = 500
saques = 0
LIMITE_SAQUES = 3
extrato = ""

while True:
    print("\n===== MENU BANCÁRIO =====")
    print("[d] Depositar")
    print("[s] Sacar")
    print("[e] Extrato")
    print("[q] Sair")

    opcao = input("Escolha uma opção: ").lower()

    if opcao == "d":
        valor = float(input("Digite o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido! O depósito deve ser maior que zero.")

    elif opcao == "s":
        valor = float(input("Digite o valor do saque: R$ "))

        if valor <= 0:
            print("Valor inválido!")

        elif valor > saldo:
            print("Saldo insuficiente!")

        elif valor > limite:
            print("O limite por saque é de R$ 500,00.")

        elif saques >= LIMITE_SAQUES:
            print("Limite de 3 saques atingido!")

        else:
            saldo -= valor
            saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
            print("Saque realizado com sucesso!")

    elif opcao == "e":
        print("\n===== EXTRATO =====")

        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)

        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "q":
        print("Obrigado por utilizar nosso sistema bancário!")
        break

    else:
        print("Opção inválida! Tente novamente.")