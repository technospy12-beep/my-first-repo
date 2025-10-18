operator=input("enter an operator (+-/*) :")
num1=int(input("enter the  1st number :"))
num2=int(input("enter the 2nd number :"))
if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
else:
    print("invalid operator")


if operator =="":
    print("you didnt type a operator")
    