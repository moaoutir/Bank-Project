import Client as cl

client = cl.Client()
connect = False

while (True):
    if connect == False:
        print("+------   Welcome   ------+")
        print("|       1 : Sign up       |")
        print("|       2 : Sign in       |")
        print("|       3 : Exit          |")
        print("+-------------------------+")
        cmp = int(input("\nEnter a digit : "))
        if(cmp == 1):
            client.sign_up()
        elif(cmp == 2):
            client.sign_in()
            if client.client_id:
                connect = True
        else:
            break
    else:
        print("+----------   MENU   ----------+")
        print("| 1 : Show your informations   |")
        print("| 2 : Create another account   |")
        print("| 3 : Your balance             |")
        print("| 4 : Make a transaction       |")
        print("| 5 : Transactions history     |")
        print("| 7 : Switch to another client |")
        print("| 8 : Set a balance alert      |")
        print("| 9 : Log out                  |")
        print("| 10: Exit                     |")
        print("+------------------------------+")
        cmp = int(input("\nEnter a digit : "))
        if(cmp == 1):
            client.show_info()
        elif (cmp == 2):
            client.other_account()
        elif(cmp == 3):
            client.get_my_balance()
        elif(cmp == 4):
            client.make_transaction()
        elif(cmp == 5):
            client.show_transaction()
        elif (cmp == 7):
            connect = False
            del client
            client = cl.Client()
            client.sign_in()
            if client.client_id:
                connect = True
        elif (cmp == 8):
            client.setBalanceAlerts()
        elif (cmp == 9):
            connect = False
            print("Successfully logged out!\n")
        else:
            break