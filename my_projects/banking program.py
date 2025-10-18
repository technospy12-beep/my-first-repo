balance = 0
x = 0.0

def show_balance():
    print(f"your balance is {x:.2f}")


def deposit():
    amount = float(input("enter deposit amount: "))

    if amount < 0:
        print("Thats' an invalid deposit")
    else:
        return amount


def withdraw():
    amount=int(input("enter the amount to be  withdrawn : "))



is_running = True


while is_running:
    print("Banking program")
    print("________________")
    print("1.Show balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    choice = input("Enter your choice(1-4): ")

    if choice == "2":
        x = float(input("enter deposit amount: "))

    elif choice == "3":
        amount = int(input("enter the amount to be  withdrawn : "))
        h = x + balance
        if amount > h:
            print("You dont have sufficient balance")
        else:
           h= h-amount

    elif choice == "1":
          h = x + balance
          print(h)

    elif choice == "4":
          is_running = False
          print("Thank you,Have a nice day")

    else:
          print("Invalid choice")
