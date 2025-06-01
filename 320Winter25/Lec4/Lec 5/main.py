"""
Lecture 5 App 1     Functions + Lec4App1

Lecture 4 App 1 Price Computation 

- function - named program unit
-1. define the function = make it 
-2. call the function = make it run (envoking it)


Lecture 4 App 1.  Price computation.

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
#functions  (keep functions above the main)
#1 compute order price  out: order_price    in: weight  (float)
def compute_order_price(wt):
    unit_price = 15.0
    price = wt * unit_price

    return price
#end function 

#2 compute discount, if any.    out: discount_amount    in: order_price     (float)

def compute_discount(price):
    #pass
    rate_discount = 0.03
    discount = 0.0
    if price > 100.0:
        discount = price * rate_discount 

    return discount
    

#4 find the shipping rate   out: ship_rate      in: weight  (float)
def find_ship_rate(wt):   #'header'
    if wt <= 5.0:
        rate = 0.1
    elif wt <= 10.0:
        rate = 0.15
    else:
        rate = 0.2
    #end if 
    return rate 
    #1 send value of rate back to main 
    #2 terminates the function 

#5 compute the shipping cost    out: cost_ship      in: weight, ship_rate   (float)

def compute_ship_cost(wt, rate):
    cost = wt * rate

    return cost
#end function
#the function must use the inputs it is fgiven (i.e. paramerters unside the parenthesis)
#if there is a result, the function must return it.
#have a single return statement, make it the last line in function.
#in particular, do not place return statements inside if statements. 
    
#6 compute the tax      out: tax        in: order_price (after discount is applied)     (float)
def compute_tax(price):
    tax_rate = 0.08
    tax = price * tax_rate

    return tax
#end function





#'main'
#inputs
weight = float(input('Enter weight in pounds >'))

#initializations



#computations
#1 compute order price  out: order_price    in: weight  (float)
order_price = compute_order_price(weight)
#when a function returns a value, store it in a variable, and then use that 
#variable in the lines after 
#inputs - what you need to know (that you do not already know)
#unit price is already known to you 

#2 compute discount, if any.    out: discount_amount    in: order_price     (float)

discount_amount = compute_discount(order_price)




#3 apply the discount (in this case subtract it)
order_price = order_price - discount_amount         #instead of using 'subtotal' coders reuse/override its previous values with the same variable 'order_price'
#order_price -= discount_amount
#order price is decrememnted by discount amount
#+=     /=  *=
#4 find the shipping rate   out: ship_rate      in: weight  (float)

ship_rate = find_ship_rate(weight)      #wt = weight    ' parameter = argument '

#5 compute the shipping cost    out: cost_ship      in: weight, ship_rate   (float)
cost_ship = compute_ship_cost(weight, ship_rate)

#6 compute the tax      out: tax        in: order_price (after discount is applied)     (float)
tax = compute_tax(order_price)  #argument is order_price    parameter is: price

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