age=int(input("Enter your age: "))

while age<0 :
    print("it is not a valid age")
    age = int(input("Enter your age: "))

else :
    print(f"You are {age} years old")