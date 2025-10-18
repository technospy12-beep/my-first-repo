import random

options=["rock","paper","scissors"]
com=random.choice (options)
user=input("enter your guess(rock,paper or scissors): ")
print(f"computer was {com},and you was {user}")

if user==com:
    print("its a tie!!")
elif user =="rock" and com=="scissors":
    print("you won")
elif user =="paper" and com=="scissors":
    print("you lost")
elif user =="scissors" and com=="paper":
    print("you won")
elif user =="paper" and com=="rock":
    print("you won")
else:
    print("you entered nothing")

    choices=["rock","paper","scissors"]
while user=="rock" or "paper" or "scissors":
    user=input("enter your guess(rock, paper or scissors): ")
comp = random.choice(choices)
print(f"computer was {com},and you was {user}")

