menu = """
Escolha a operação a ser realizada
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

withdrawal_limit = 500.0
withdrawal_counter = 0
balance = 0.0
account_statement = []

while True:
    operation_type = input(menu)
    if operation_type == "q":
        break

    if operation_type == "d":
        while True:
            try:
                value = float(input("Informe o valor do depósito: "))
                if value <= 0.0:
                    raise TypeError()
                break
            except Exception:
                print("Valor inválido. Informe um valor positivo.")
        balance += value
        account_statement.append(f"Depósito: R$ {value: .2f}")
        print("Depósito realizado com sucesso!")
        print(f"Novo saldo: R$ {balance: .2f}")
        continue
    
    if operation_type == "s":
        if withdrawal_counter > 3:
            print("Saque não permitido. Limite de 3 saques por dia antingido.")
            continue
        
        available_balance = 500 if balance > 500 else balance
        while True:
            try:
                value = float(input(f"Informe o valor do saque (máximo R$ {available_balance: .2f}): "))
                if value <= 0.0 or value > withdrawal_limit:
                    raise TypeError()
                break
            except Exception:
                print(f"Valor inválido. Informe um valor positivo com máximo de R$ {available_balance: .2f}.")
        balance -= value
        account_statement.append(f"Saque: R$ {value: .2f}")
        withdrawal_counter += 1
        print("Saque realizado com sucesso!")
        print(f"Novo saldo: R$ {balance: .2f}")
        continue 
    
    if operation_type == 'e':
        print("##### Extrato de Conta Corrente #####")
        if len(account_statement) == 0:
            print("Conta sem movimentação para o periodo")
        else:
            for transaction in account_statement:
                print(transaction)
        print()                
        print(f"Saldo: {balance: .2f}")
        print("##### FIM do EXTRATO #####")
        continue

    print("Operação inválida")

