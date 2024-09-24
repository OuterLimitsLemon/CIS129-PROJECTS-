#Filename: cis129_lab03_coffeeShop.py
#Project: Module 3, Lab 'Coffee Shop Simulator' 
#Author: Oscar E. Saenz
#Professor: Troy Adams
#Class/CRN: 11616 CIS129 
#Date: 09/23/2024 21:01
#Description: This is an interactive text based coffee shop simulator that calculates a receipt based on how many items the user wants to order. 
#Usage: When prompted, input a quantity of coffees sold and a quantity of muffins sold. 
 


#Visual formatting for the top of the receipt
print('*************************************** \nMy Coffee and Muffin Shop \n')


#This section defines the price of a cup of coffee ($5) and a single muffin ($4)
price_of_coffee = 5
price_of_muffin = 4


#This prompt asks the user to input the number of coffees and muffins bought by the patron.
quantity_of_coffees_sold = int(input('Number of coffees bought? \n'))
quantity_of_muffins_sold = int(input('Number of muffins bought? \n'))


#Visual formatting for the center of the receipt.
print('*************************************** \n\n*************************************** \nMy Coffee and Muffin Shop Receipt \n')


#This generates a line item total. It multiplies the quantities of coffees and muffins sold by their respective prices. 
coffee_line_item = (price_of_coffee * quantity_of_coffees_sold)
muffin_line_item = (price_of_muffin * quantity_of_muffins_sold)


#This generates a tax line item by multiplying the coffee and muffin line items by 6% (the tax rate in this scenario).
subtotal = (coffee_line_item + muffin_line_item)
tax_total = subtotal * .06


#This is your final total. It is your tax line item added to your coffee and muffin line items. 
total_bill = (subtotal + tax_total)


#Visual formatting for the bottom of the receipt.
print(quantity_of_coffees_sold, 'Coffee at $5 each: $',coffee_line_item,'.00 \n')
print(quantity_of_muffins_sold, 'Muffins at $4 each: $',muffin_line_item,'.00 \n')
print('6% tax: $',tax_total, '\n')
print('--------- \n')
print('$',total_bill)
print('***************************************')