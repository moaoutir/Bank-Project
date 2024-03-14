import DatabaseManagement as bd

class Account:
    def __init__(self, client_id, rib, balance=0):
        self.threshold = 0.0
        self.client_id = client_id
        self.rib = rib
        self.balance = balance
    
    def transaction(self, client_id, rib_sender, rib_receiver, amount):
        if (bd.search_rib_db(rib_sender) and bd.search_rib_db(rib_receiver)):
            bd.modify_balance_db(rib_sender, - amount)
            bd.modify_balance_db(rib_receiver, amount)
            bd.transaction_db(client_id, rib_sender, rib_receiver, amount)
            print("Transaction successful.")