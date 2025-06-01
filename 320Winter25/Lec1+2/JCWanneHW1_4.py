"""Homework 1 Question 2    Developed by JC 01.14.25 

Q4: Prompt the user for: name, weight in pounds of coffee 
ordered, one by one. One pound of coffee costs 18.5$. 
Compute order price. Orders are taxed at 7%. Compute tax. 
Shipping cost is charged at 75 cents per pound. Compute 
shipping cost. Billed amount is the sum of order price, 
tax, and shipping cost. Display Output: Hello <name>, 
you ordered <weight> pounds of coffee, and on the next 
line, and you owe <billed>$, including <ship>$ for 
shipping, and <tax>$ tax.

Input: name (string)  weight (float) in pounds        
Output: order_price (float)  ship_price (float)  tax_cost (float)  billed_amount (float)
"""

#Initializations
pound_coffee = 18.5
tax = 0.07
pound_ship_cost = 0.75

#Inputs
name = input('Enter your name \n>>')
weight = float(input('Enter the amount of coffee in pounds \n>>'))



#Calculations
order_price = pound_coffee * weight
tax_cost = order_price * tax
ship_price = pound_ship_cost * weight
billed_amount = order_price + tax_cost + ship_price


#Outputs
print(f'Hello {name:s}, you ordered {weight:.2f} pounds of coffee\nyou owe {billed_amount:.2f}$, including {ship_price:.2f}$ for shipping, and {tax_cost:.2f}$ for tax')