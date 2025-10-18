weight=float(input("enter the weight :"))
unit=input("enter the unit : (kilogram/pounds:")
if unit == "kilogram":
    weight = weight * 2.205
elif unit == "pounds":
    weight = weight / 2.205
else:
    print(f"{unit} is an invalid unit")
print(f"your weight is: {weight}")
