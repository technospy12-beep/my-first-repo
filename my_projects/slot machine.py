def spin_row():
    pass

def print_row():
    pass

def get_payout():
    pass

def main():
    balance=100

    print("Welcome to python slots")
    print("************************")
    print("Symbols: 🍒🍓🥭🍉🔔")
    print("************************")



    while balance>0:
        print(f"current balance: {balance}")

        bet=int(input("place your bet amount: "))


        if bet<=0:
            print("Bet must be grater than 0")





        bet=int(bet)




        if bet>balance:
            print("You dont have sufficient balance")
        continue



if __name__ == '__main__':
    main()