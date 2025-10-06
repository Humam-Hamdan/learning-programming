item = input( "What is the item which you are buying?: " )

price = float ( input ( "What is the price for said item?: " ) )

quantity = int ( input ( "How many would you like?: " ) )

total =  price * quantity

print(f"the total amount for the {item}/s which you bought {quantity} of, is €{total}")
