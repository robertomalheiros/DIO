depositos = []
saques = []
limite_saques = 3
limite_valor_saque = 500.00
saldo = 0

def depositar(valor):
    global saldo
    saldo += valor
    depositos.append(valor)
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

def sacar(valor):
    global saldo, limite_saques
    if valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
        return
    if valor > limite_valor_saque:
        print(f"O valor máximo permitido por saque é R$ {limite_valor_saque:.2f}.")
        return
    if len(saques) >= limite_saques:
        print("Limite diário de saques atingido.")
        return
    saldo -= valor
    saques.append(valor)
    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

def exibir_extrato():
    global saldo
    print("Extrato:")
    if not depositos and not saques:
        print("Não foram realizadas movimentações.")
    else:
        for deposito in depositos:
            print(f"Depósito: R$ {deposito:.2f}")
        for saque in saques:
            print(f"Saque: R$ {saque:.2f}")
        print(f"Saldo atual: R$ {saldo:.2f}")

while True:
    print("1-Depositar\n2-Sacar\n3-Extrato\n4-Sair")
    operacao = int(input("Digite o número da operação desejada: "))
    if operacao == 1:
        valor = float(input("Digite o valor do depósito: "))
        if valor <= 0:
            print("O valor do depósito deve ser positivo.")
        else:
            depositar(valor)
    elif operacao == 2:
        valor = float(input("Digite o valor do saque: "))
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
        else:
            sacar(valor)
    elif operacao == 3:
        exibir_extrato()
    elif operacao == 4:
        break
    else:
        print("Operação inválida. Tente novamente.")