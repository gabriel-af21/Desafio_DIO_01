menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao=input(menu)

    if opcao == "d":
        deposito = float(input("Digite a quantia que deseja depositar "))
        if deposito <= 0:
            print("Você inseriu um valor inválido. Por favor insira um valor positivo.")
            print("----------------------------------------------------------------------------------")
        else:
            saldo += deposito
            print(f"Seu depósito no valor de R${deposito:.2f} foi registrado! Obrigado pela preferência.")
            extrato += f"Depósito - R${deposito:.2f}\n"
            print("----------------------------------------------------------------------------------")
    
    elif opcao == "s":
        if saldo == 0:
            print("Seu saldo será creditado.Deseja continuar?")
            escolha = int(input("[1] para sim; [2] para não;\n"))
            if escolha == 2:
                continue
        if numero_saques < LIMITE_SAQUES:
            saque= float(input("Digite a quantia que deseja sacar "))
            if saque > 500:
                print("Seu limite de saque é R$500,00. Por favor insira um valor menor.")
                print("----------------------------------------------------------------------------------")
            elif saque <= 0:
                print("Você inseriu um valor inválido. Por favor insira um valor positivo.") 
                print("----------------------------------------------------------------------------------")
            else:
                saldo -= saque
                print(f"Seu saque no valor de R${saque:.2f} foi registrado! Obrigado pela preferência.")
                extrato += f"Saque - R${saque:.2f}\n"
                numero_saques += 1
                print("----------------------------------------------------------------------------------")
        else:
            print("Você atingiu o número máximo de saques diários. Tente novamente amanhã.")
    elif opcao == "e":
        print("-------------EXTRATO-------------\n")
        if extrato == "":
            print("Não houveram movimentações na conta bancária.")
        else:
            print(extrato)
            print(f"Saldo: R${saldo:.2f}")
        print("---------------------------------\n")
    elif opcao == "q":
        print ("Operação finalizada.")
        break
    else:
        print("Operação inválida! Tente Novamente.")
        print("----------------------------------------------------------------------------------")