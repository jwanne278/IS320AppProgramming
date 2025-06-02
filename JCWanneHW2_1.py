"""Homework 2 Question 1     Developed by JC     01.22.24

This app finds the total_billed of all the food items ordered.
User inputs the weight of artichokes, carrots, and beets. 
We are given the unit prices for each of the food items.
By adding up the total price for each food item, we are given price (float).
If price is above 100 dollars, only then do you discount the price by 4% to get the actual price.
To find our outputs--shipping_cost and billed amount--we must do a few things.
Shipping_cost is the dependent variable of pounds_total.
For orders <= 10 pounds, shipping cost is 5.5 dollars.
For orders <= 20 pounds, shipping cost is 10 dollars.
For orders > 20 pounds, shipping costs is 9.5 plus (pounds_total * 0.1).
The billed_amount is found by adding the price by the shipping_cost. 

inputs: pounds_artichokes (float), pounds_carrots (float), pounds_beets (float)
output: price (float), shipping_cost (float), billed_amount (float)
"""

#Inititalizations
pound_price_artichokes = 2.67
pound_price_carrots = 1.89
pound_price_beets = .79

#Inputs
pounds_artichokes = float(input('How many pounds of artichokes did you order?\n>>'))
pounds_carrots = float(input('How many pounds of carrots did you order?\n>>'))
pounds_beets = float(input('How many pounds of beets did you order?\n>>'))

#Computations 
pounds_total = pounds_artichokes + pounds_carrots + pounds_beets

if pounds_total <= 10.0:
    shipping_cost = 5.5
elif pounds_total <= 20.0:
    shipping_cost = 10.0
else:
    shipping_cost = 9.5 + .10 * pounds_total
#Express price as one big price value before discount 
price = (pound_price_artichokes * pounds_artichokes + pound_price_carrots * pounds_carrots + pound_price_beets * pounds_beets)

#then re use the price variable, and then add the 4% discount if it applies, if not leave it as is 
if price > 100.0:
    discount = 0.04 * price
    price -= discount
else:
    discount = 0.0

# price = (pound_price_artichokes * pounds_artichokes + pound_price_carrots * pounds_carrots + pound_price_beets * pounds_beets)

billed_amount = price + shipping_cost 
# if price > 100.0:
#     billed_amount = 0.96 * price + shipping_cost
# else:
#     billed_amount = price + shipping_cost

#to find billed amount we need to know the price (that will determine wheather there is a discount or not)
#then we add the shipping_cost
#then we get the billed_amount


#Outputs
print(f'Your price before shipping is {price:.2f}$')
print(f'Your shipping cost is {shipping_cost:.2f}$')
print(f'The billed amount is {billed_amount:.2f}$')