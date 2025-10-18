import random

lowest_number=1
highest_number=int(input("enter the maximum number: "))
num=  random.randint(lowest_number,highest_number)

user_num=int(input("enter your guess: "))
while   num != user_num:
    print(f"wrong guess,It was {num}")
    highest_number = int(input("enter the maximum number: "))
    num= random.randint(lowest_number,highest_number)
    user_num = int(input("enter your guess: "))
if user_num==num:
    print("you guess right")
else:
    print(f"you guess wrong,It was {num}")