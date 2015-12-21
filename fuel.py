print("Fuel calculator - Simple cost per litre to cost per gallon\n")

# Calculates the cost per gallon from the cost per litre
try:
    costperlitre = input("Please input cost per litre (eg 0.99 is £0.99): £")
    costpergallon = float(costperlitre) * 4.54609

    formattedcostpergallon = format((costpergallon),'.2f' )
    print("Cost per gallon: £%s\n" % formattedcostpergallon)

except ValueError:
    print("Error: That's an invalid value, you should enter a price in decimal form")


# Converts litres to gallons and then provides a summary for litres and gallons including total costs
try:
    litres = input("Please input number of litres: ")

    gallons = float(litres) / 4.54609
    formattedgallons = format((gallons),'.2f' )

    litrecost = float(costperlitre) * float(litres)
    formattedlitrecost = format((litrecost),'.2f' )

    gallonscost = costpergallon * gallons
    formattedgallonscost = format((gallonscost),'.2f' )

    print("%s litres = %s gallons \n" % (litres, formattedgallons))

    print("Summary:")
    print("%s litres @ £%s/l gives total £%s" % (litres, costperlitre, formattedlitrecost))
    print("%s gallons @ £%s/gal gives total £%s\n" % (formattedgallons, formattedcostpergallon, formattedgallonscost))


    input("Press enter to exit")

except ValueError:
    print("Error: That's an invalid value")

    input("Press enter to exit")
