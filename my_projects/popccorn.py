menu={"pizza": 120,
      "nachos":30,
      "popcorn":140,
      "fries": 75,
      "chips":30,
      "pretzel":350,
      "soda":100,
      "lemonade":45}
cart=[]
total=0
print("-------MENU-------")

print(menu)

print("------------------")
food=input("select an item(q to quit): ")
if food == "q":
               break
        else:
            cart.append(food)