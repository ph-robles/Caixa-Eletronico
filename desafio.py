''' Operação de deposito 
deve ser possivel depositar valores positivos para a minha conta bancaria. A v1 do projeto trabalha apenas 
com 1 usuario , dessa forma não precisamos nos preocupar em identificar qual é o numero da agencia e conta bancaria. 
todos os depositos devem ser armazenados em uma variavel '''



menu = """

[d] depositar 
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
        

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! você não tem saldo suficiente. ")

        elif excedeu_limite:
            print("Operação negada! você ultrapassou o limite diário. ")

        elif excedeu_saques:
            print("Operação negada! Número maximo de saques excedido. ")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! o valor informado é invalido. ")            


    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas operações. "if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("============================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")        