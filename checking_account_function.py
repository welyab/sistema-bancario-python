options = {
    "u": "Criar usuário",
    "c": "Criar conta corrente",
    "d": "Depositar",
    "s": "Sacar",
    "e": "Extrato",
    "q": "Sair",
}

menu = "\n".join([f"[{code}] {desc}" for (code, desc) in options.items()])

account_seed = 1
accounts = []
customers = []

# usario composto por:
# nome
# data de nascimento
# cpf
# endereco:
#    logradouro
#    número
#    bairro
#    cidade/uf

# deve armazenar contas em uma lista
# a conta é composta por agência, número e usuário
# número de conta é sequencia, iniciando em 1
# número da agencia é fixo em "0001"

def show_menu():
    print(menu)
    print()

def read_option():
    while True:
        option = input("Informe a opção desejada: ")
        if option in options:
            return option
        else:
            print(f"Erro! Opção '{option}' inválida")
            print()
            show_menu()

def create_customer(*, customers):
    print("Cadastro de cliente")
    while True:
        cpf = input("Informe o CPF (0 para sair): ")
        if cpf == "0":
            print()
            break
        if len(list(filter(lambda customer: customer["cpf"] == cpf, customers))) > 0:
            print(f"CPF {cpf} já cadastrado.")
            print()
            continue
        nome = input("Informe o nome: ")
        birth_date = input("Informe a data de nascimento: ")
        public_place = input("Informe o logradouro: ")
        house_number = input("Informe o número: ")
        neighborhood = input("Informe o bairro: ")
        city = input("Informe a cidade: ")
        uf = input("Informe a UF: ")
        customers.append(
            {
                "cpf": cpf,
                "nome": nome,
                "birth_date": birth_date,
                "public_place": public_place,
                "house_number": house_number,
                "neighborhood": neighborhood,
                "city": city,
                "uf": uf
            }
        )
        print("Cliente cadastrado com sucesso")
        print()
        break

def create_account(*, accounts, customers, account_number):
    print("Cadastro de conta corrente")
    while True:
        cpf = input("Informe o CPF do cliente (0 para sair): ")
        if cpf == "0":
            return False
        if len(list(filter(lambda costumer: costumer["cpf"] == cpf, customers))) == 0:
            print(f"Cliente com CPF {cpf} não encontrado")
            print()
            continue
        accounts.append(
            {
                "cpf": cpf,
                "branch_number": "0001",
                "account_number": account_number,
                "balance": 0.0,
                "withdrawal_count": 0
            }
        )
        print("Conta corrente cadastrada com sucesso")
        print()
        return True

# parameters by position placement
def deposit(accounts, /):
    print("Depósito")
    while True:
        branch_number = input("Informe o número da agência (0 para sair): ")
        account_number = input("Informe o número da conta: ")
        if len(list(filter(lambda account: account["branch_number"] == branch_number and account["branch_nyumber"] == account_number))) == 0:
            print(f"Conta {account_number} AG {branch_number} não encontrada")
            print()
            continue
        value = float(input("Informe o valor a ser depositado: "))
        account = list(filter(lambda account: account["branch_number"] == branch_number and account["branch_nyumber"] == account_number))[0]
        account["balance"] += value
        print("Depósito realizado com sucesso")
        print()
        return

# parameters by name only
def withdrawal(*, accounts):
    print("Saque")
    while True:
        branch_number = input("Informe o número da agência (0 para sair): ")
        account_number = input("Informe o número da conta: ")
        if len(list(filter(lambda account: account["branch_number"] == branch_number and account["branch_nyumber"] == account_number))) == 0:
            print(f"Conta {account_number} AG {branch_number} não encontrada")
            print()
            continue
        account = list(filter(lambda account: account["branch_number"] == branch_number and account["branch_nyumber"] == account_number))[0]
        if account["withdrawal_count"] > 3:
            print("Operação não pode ser realizada. Quantidade de saques atingida")
            print()
            return
        value = float(input("Informe o valor a ser sacada: "))
        account["balance"] += value
        print("Depósito realizado com sucesso")
        print()
        return

# balance parameter by position only
# account_statement by name only
def account_statement():
    None

def checking_account():
    while True:
        show_menu()
        option = read_option()
        if option == 'u':
            create_customer(
                customers = customers
            )
        elif option == 'c':
            global account_seed
            next_account_number = str(account_seed).ljust(4, "0")
            account_created = create_account(
                accounts = accounts,
                customers = customers,
                account_number = next_account_number
            )
            if account_created:
                account_seed += 1
        elif option == 'd':
            deposit()
        elif option == 's':
            withdrawal()
        elif option == 'e':
            account_statement()
        elif option == 'q':
            print("Programa encerrado")
            break

checking_account()
