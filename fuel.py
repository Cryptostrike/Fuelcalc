print("Fuel calculator - Simple cost per litre to cost per gallon")
try:
    costperlitre = input("Please input cost per litre (eg 0.99 is £0.99): £")
    costpergallon = float(costperlitre) * 4.54609

    x = format((costpergallon),'.2f' )
    print("Cost per gallon: £%s" % x)
    input("Press enter to exit")

except ValueError:
    print("Error: That's an invalid value, you should enter a price in decimal form")
    input("Press enter to exit")