import random
import string
import Account as ac
import DatabaseManagement as bd

class Client:
    def __init__(self):
        self.client_id = ""
        self.first_name = ""
        self.last_name = ""
        self.password = ""
        self.accounts = []

    def sign_up(self):
        self.first_name = input("Enter your first name : ")
        self.last_name = input("Enter your last name : ")
        self.password = input("Suggest a password for your account (more than 8 characters) : ")
        while (len(self.password) <= 8):
            self.password = input("A password with more than 8 characters : ")
        self.client_id = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        while (bd.search_user_db(self.client_id)):
            self.client_id = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        print("ID :", self.client_id, "- Client :", self.first_name, self.last_name, "- Password :", self.password)

        bd.add_client_db(self.client_id, self.first_name, self.last_name, self.password)

        while True:
            new_account = self.add_account(self.client_id)
            self.accounts.append(new_account)
            if input("More? 'Type Yes or No': ").lower() != "yes":
                print("")
                break

    def add_account(self, client_id):
        rib = ''.join(random.choices(string.digits, k=8))
        while bd.search_rib_db(rib):
            rib = ''.join(random.choices(string.digits, k=8))
        print("This is your RIB :", rib)
        balance = float(input("Give the balance which will you put in your account : "))
        new_account = ac.Account(client_id, rib, balance)
        bd.add_account_db(new_account.client_id, new_account.rib, new_account.balance)
        return new_account
    
    def other_account(self):
        while True:
            new_account = self.add_account(self.client_id)
            self.accounts.append(new_account)
            if input("More? 'Type Yes or No': ").lower() != "yes":
                print("")
                break
    
    def sign_in(self):
        client_id = input("Enter your ID: ")
        password = input("Enter your password: ")
        check = bd.check_authentication_db(client_id, password)
        if (check != None):
            print("Successfully signed in!\n")
            self.client_id = check[0]
            self.first_name = check[1]
            self.last_name = check[2]
            self.accounts = bd.load_accounts_db(self.client_id)
        else:
            print("Invalid client ID or password.\n")

    def show_info(self):
        print("\n#################################################")
        print("# ------------ Client Informations ------------ #")
        print("# ID : {:<40} #".format(self.client_id))
        print("# Client : {:<36} #".format(self.first_name + " " + self.last_name))
        print("# Accounts :                                    #")
        print("# +--------------------+----------------------+ #")
        print("# |         RIB        |        Balance       | #")
        print("# +--------------------+----------------------+ #")
        for i in self.accounts:
            print("# | {:<18} | {:<20} | #".format(str(i.rib), i.balance))
        print("# +--------------------+----------------------+ #")
        print("#################################################\n")

    def get_my_balance(self):
        somme = 0
        self.accounts = bd.load_accounts_db(self.client_id)
        for i in self.accounts:
            somme += float(i.balance)
        print("\n#################################################")
        print("# ------------------ Balance ------------------ #")
        print("# ID : {:<40} #".format(self.client_id))
        print("# Client : {:<36} #".format(self.first_name + " " + self.last_name))
        print("# Balance : {:<35} #".format(somme))
        print("# --------------------------------------------- #")
        print("#################################################\n")

    def make_transaction(self):
        self.show_info()
        rib_sender = input("Enter RIB FROM where you want make transaction (sender) : ")
        rib_receiver = input("Enter RIB TO where you want make transaction (receiver) : ")
        amount = float(input("Enter the amount to transfer : "))
        for i in self.accounts:
            if (i.rib == rib_sender):
                if (amount > float(i.balance)):
                    print("Error : The amount is greater than your balance !")
                i.transaction(self.client_id, rib_sender, rib_receiver, amount)
                self.accounts = bd.load_accounts_db(self.client_id)
                return
        print(f"Account with RIB {rib_sender} not found.")

    def show_transaction(self):
        transactions = bd.load_transactions_db(self.client_id)
        print("\n########################################################################")
        print("# ----------------------- Transactions history ----------------------- #")
        print("# ID : {:<63} #".format(self.client_id))
        print("# Client : {:<59} #".format(self.first_name + " " + self.last_name))
        print("# Transactions :                                                       #")
        print("# +--------------------+----------------------+----------------------+ #")
        print("# |     Sender RIB     |     Receiver RIB     |        Amount        | #")
        print("# +--------------------+----------------------+----------------------+ #")
        for i in transactions:
            print("# | {:<18} | {:<20} | {:<20} | #".format(str(i[1]), str(i[2]), str(i[3])))
        print("# -------------------------------------------------------------------- #")
        print("########################################################################\n")