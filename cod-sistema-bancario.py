#Criar um sistema bancário com as operações: sacar, depositar e visualizar estrato.
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

#1.Codições:
#1.1.Sacar
#1.1.1.O sistema deve permitir realizar um máximo de 03 saques diários;
#1.1.2.Cada saque possui um limite máximo de R$500,00;
#1.1.3.Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo;
#1.1.4.Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.


#1.2.Depositar
#1.2.1.Só será permitido depositar valores positivo para conta;
#1.2.2.Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.


#1.3.Extrato
#1.3.1.Essa operação deve listar todos os depósitos e saques realizados na conta;
#1.3.2.No fim da listagem deve ser exibido o saldo atual da conta;
#1.3.3.Se o extrato estiver em branco, exibir a mensagem: "Não foram realizadas movimentações".
#1.3.4.Os valores devem ser exibidos utilizando o formato R$ xxx.xx.


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

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
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
