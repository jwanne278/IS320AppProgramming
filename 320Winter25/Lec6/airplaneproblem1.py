"""Lab 2 Airplane Problem 1     Developed by JC     01.27.24

This app calculates the total billed price of 3 food items
The user inputs the weight in pounds of each food item they order 
By multiplying the unit prices per pound by the # of pounds, we arrive at a total_price.
If the total price exceeds $100, then we apply a 4% discount.
Now we have computed a new value for total_price.
We must add shipping_charge to total_price.
If the total_weight is <= 10 it is a flat $5.5.
For <= 20 it is a flat rate of $10.
For > 20 it is 9.5 + 0.1 * total_weight.
Finally, you add the selected shipping charge to the total_price to acheive billed_amount.

Inputs: weight_artichokes (float), weight_carrots (float), weight_beets (float) 
Outputs: price (the number after applying discount) (float), shipping_charge (float), billed_amount (float)
"""

#Initializations
artichoke_pound_price = 2.67
carrot_pound_price = 1.89
beet_pound_price = 0.79

#Inputs
weight_artichokes = float(input('How many pounds of artichokes did you buy?\n>>'))
weight_carrots = float(input('How many pounds of carrots did you buy?\n>>'))
weight_beets = float(input('How many pounds of beets did you buy?\n>>'))

#Computations

#1.Take inputs of the weight, then multiply by price per pound 
price_artichokes = artichoke_pound_price * weight_artichokes
price_carrots = carrot_pound_price * weight_carrots
price_beets = beet_pound_price * weight_beets
total_price = price_artichokes + price_carrots + price_beets

#2. If this number is above 100, include the 4% discount 
if total_price > 100.0:
    discount = total_price * 0.04
    total_price -= discount

#3. find the shipping cost and add it to the price, based on the total weight of the order, using if statement
total_weight = weight_artichokes + weight_carrots + weight_beets

if total_weight <= 10.0:
    shipping_charge = 5.5
elif total_weight <= 20.0:
    shipping_charge = 10.0
else:
    shipping_charge = 9.5 + 0.1 * total_weight

#4. Calcualte total to get final billed_amount
billed_amount = total_price + shipping_charge

#Outputs
print(f'Your price before shipping is {total_price:.2f}$')
print(f'Your shipping cost is {shipping_charge:.2f}$')
print(f'Your total billed amount is {billed_amount:.2f}')