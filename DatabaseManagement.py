import Account as ac

def connect_to_file(file_name):
    return open(file_name, "a+")

def search_user_db(client_id):
    with connect_to_file("accounts.txt") as file:
        file.seek(0)
        for i in file.readlines():
            if client_id == i.split(",")[2]:
                return True
    return False

def search_rib_db(rib):
    with connect_to_file("accounts.txt") as file:
        file.seek(0)
        for i in file.readlines():
            if rib == i.split(",")[1]:
                return True
    return False

def add_client_db(client_id, first_name, last_name, password):
    with connect_to_file("clients.txt") as file:
        file.seek(0)
        data = f"{client_id},{first_name},{last_name},{password}\n"
        file.write(data)

def add_account_db(client_id, rib, balance):
    with connect_to_file("accounts.txt") as file:
        file.seek(0)
        data = f"{client_id},{rib},{balance}\n"
        file.write(data)

def check_authentication_db(client_id, password):
    with connect_to_file("clients.txt") as file:
        file.seek(0)
        for i in file.readlines():
            client_data = i.strip().split(',')
            if (client_data[0] == client_id and client_data[3] == password):
                return client_data

def load_accounts_db(client_id):
    accounts = []
    with connect_to_file("accounts.txt") as file:
        file.seek(0)
        for i in file.readlines():
            account_data = i.strip().split(',')
            if account_data[0] == client_id:
                new_account = ac.Account(account_data[0], account_data[1], account_data[2])
                accounts.append(new_account)
    return accounts

def modify_balance_db(rib, amount):
    with open("accounts.txt", 'r') as file:
        lines = file.readlines()
    for i in range(len(lines)):
        account_data = lines[i].strip().split(',')
        if account_data[1] == rib:
            account_data[2] = str(float(account_data[2]) + amount)
            lines[i] = ','.join(account_data) + "\n"
            with open("accounts.txt", 'w') as file:
                file.writelines(lines)
            print(f"New balance for account {rib}: {account_data[2]}")
            break

def transaction_db(client_id, rib_sender, rib_receiver, amount):
    with connect_to_file("transactions.txt") as file:
        file.seek(0)
        data = f"{client_id},{rib_sender},{rib_receiver},{amount}\n"
        file.write(data)

def load_transactions_db(client_id):
    transactions = []
    with connect_to_file("transactions.txt") as file:
        file.seek(0)
        for i in file.readlines():
            account_data = i.strip().split(',')
            if account_data[0] == client_id:
                transactions.append(account_data)
    return transactions