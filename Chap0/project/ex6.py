# calculate money after invest years by 5% interest
def interest10(x, year):
    x = x*(1 + 0.1)**year
    print(f"the total amount is {x}")

# calculate money after invest years by 10% interest
def interest05(x, year):
    x = x*(1+0.05)**year
    print(f"the total amount is {x}")

# calculate money after invest years by 15% interest
def interest15(x, year):
    x = x*(1+0.15)**year
    print(f"the total amount is {x}")

interest10(100000, 10)

interest15(100000, 2)

interest05(100000, 2)
