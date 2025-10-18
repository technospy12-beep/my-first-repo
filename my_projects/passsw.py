
password="heyyo"

m=input("enter your password.(if you forgot your password click fp): ")

if m== "fp":
    password=input("enter your reseting password: ")
    f = input("enter your reseted password.(if you forgot your password click fp): ")
    if f==password:
        print("your password is correct")
    else:
        print("your password is incorrect")
elif m==password:
    print("your password is correct")
elif m != password:
    print("your password is incorrect")







