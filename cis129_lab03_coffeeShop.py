#cis129_lab03_coffeeShop.py
#Module 3, Lab 'Coffee Shop Simulator' 
#Oscar E. Saenz
#Professor Troy Adams
#11616 CIS129 
#09/23/2024 22:01
#Description: This is an interactive text based coffee shop simulator that calculates a receipt based on how many items the user want to order. 
#Usage: When prompted, input a quantity of coffees sold, bananas sold, lightsabers and a quantity of muffins sold. The program is Star Wars themed. 
#Version: 2. This update includes 2 additional menu items (bananas and lightsabers) as well as some visual tweaks. 
 


#Visual formatting for the top of the receipt
print('*************************************** \nTatooine Coffee and Lightsabers \n')


#This section defines the price of a cup of coffee ($5), a single muffin ($4), a banana ($1) and a lightsaber ($7)
price_of_coffee = 5
price_of_muffin = 4
price_of_banana = 1
price_of_lightsaber = 7


#This prompt asks the user to input the number of coffees and muffins bought by the patron.
quantity_of_coffees_sold = int(input('Number of Star Coffee(s) bought? \n'))
quantity_of_muffins_sold = int(input('Number of Luke Muffin(s) bought? \n'))
quantity_of_bananas_sold = int(input('Number of Darth Banana(s) bought? \n'))
quantity_of_lightsabers_sold = int(input('Number of Lightsaber(s) bought? \n'))


#Visual formatting for the center of the receipt.
print('*************************************** \n\n*************************************** \nYour receipt, sire... \n')


#This generates a line item total. It multiplies the quantities of coffees, bananas, lightsabers and muffins sold by their respective prices. 
coffee_line_item = (price_of_coffee * quantity_of_coffees_sold)
muffin_line_item = (price_of_muffin * quantity_of_muffins_sold)
banana_line_item = (price_of_banana * quantity_of_bananas_sold)
lightsaber_line_item = (price_of_lightsaber * quantity_of_lightsabers_sold)


#This generates a tax line item by multiplying the coffee, banana, lightsaber and muffin line items by 6% (the tax rate in this scenario).
subtotal = (coffee_line_item + muffin_line_item + banana_line_item + lightsaber_line_item)
tax_total = subtotal * .06


#This is your final total. It is your tax line item added to your coffee, banana, lightsaber and muffin line items. 
total_bill = (subtotal + tax_total)


#Visual formatting for the bottom of the receipt.
print(quantity_of_coffees_sold, 'Star Coffee(s) at $5 each: $',coffee_line_item,'.00 \n')
print(quantity_of_muffins_sold, 'Luke Muffin(s) at $4 each: $',muffin_line_item,'.00 \n')
print(quantity_of_bananas_sold, 'Darth Banana(s) at $1 each: $',banana_line_item,'.00 \n')
print(quantity_of_lightsabers_sold, 'Lightsaber(s) at $7 each: $',lightsaber_line_item,'.00 \n')
print('6% tax: $',tax_total, '\n')
print('--------- \n')
print('$',total_bill)
print('***************************************')
print('Join the darkside! \nAsk about our Tatooine-Bean rewards! \n\nGive this project an "A" \nand your next lightsabers on us!')

