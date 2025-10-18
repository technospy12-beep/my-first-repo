def net_price(MRP,discounts,tax):
    return MRP*(1-discounts)*(1+tax)

print(net_price(int(input("Enter the MRP of the item: ")),int(input("Enter the discount of the item: ")),int(input("Enter the tax of the item: "))))