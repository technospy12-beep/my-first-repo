def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()

    return first+" "+last

full_name=create_name(input("enter your first name"),input("enter your last name"))

print(full_name)

