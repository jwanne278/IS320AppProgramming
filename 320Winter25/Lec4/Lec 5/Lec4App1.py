"""Lecture 4 App 1.  Price computation.

User enters weight in pounds. App computes order price,
discount, at 3% when order price is above 100$,
tax at 8%, and shipping cost.
Shipping rate is 10 cents per pound up to and including 5 pounds,
15 cents upto and including 10 pounds, and 20 cents above that.
unit price is 15$ per pound.
Display order price, discount, tax, shipping cost, and the billed amount.
('order price' above does not include tax and shipping cost.)

input: weight (float)
outputs: order_price, discount_amount, tax, shipping_cost, and the billed_amount (floats)
"""

#inputs
weight = float(input('Enter weight in pounds >'))

#initializations
unit_price = 15.0
rate_discount = 0.03
tax_rate = 0.08
discount_amount= 0.0

#computations
#1 compute order proce  out: order_price    in: weight  (float)
#inputs - what you need to know (that you do not already know)
#unit price is already known to you 
order_price = weight * unit_price
#2 compute discount, if any.    out: discount_amount    in: order_price     (float)
if order_price > 100.0:
    discount_amount = order_price * rate_discount
# else:       #every if statemernt does not need an 'else' statement 
#     discount_amount = 0.0



#3 apply the discount (in this case subtract it)
order_price = order_price - discount_amount         #instead of using 'subtotal' coders reuse/override its previous values with the same variable 'order_price'
#order_price -= discount_amount
#order price is decrememnted by discount amount
#+=     /=  *=
#4 find the shipping rate   out: ship_rate      in: weight  (float)
if weight <= 5.0:
    ship_rate = 0.1
elif weight <= 10.0:
    ship_rate = 0.15
else:
    ship_rate = 0.2
#end if 


#5 compute the shipping cost    out: cost_ship      in: weight, ship_rate   (float)
cost_ship = weight * ship_rate
#6 compute the tax      out: tax        in: order_price (after discount is applied)     (float)
tax = order_price * tax_rate
#7 find the billed amount 
billed_amount = order_price + cost_ship + tax
#why did I not do: 
#order_price = order_price + cost_ship + tax

#outputs 
#DIY make the items below print one item per line, with tezt and formatting added. 
print(weight, order_price, discount_amount, cost_ship, tax, billed_amount)
#write multiple print statments when doing your output


#We start here:
#SEQUENCE (for developing an app)
#how do I represent the data (information?)
#what are the variables? and their types?
#  1 inputs?
#  2 outputs?
#  3 any other variables?
#info given to you, intermediate results

# read inputs
# solve the problem in stages
# code debug and verify in stages
# document and organize code as needed