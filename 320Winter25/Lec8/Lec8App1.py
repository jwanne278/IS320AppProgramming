"""Functions, Globals, Summary, Averages. Revision of: Lecture 4 App 1
User enters weight in pounds. App computes order price,
discount, at 3% when order price is above 100$,
tax at 8%, and shipping cost.
Shipping rate is 10 cents per pound up to and including 5 pounds,
15 cents upto and including 10 pounds, and 20 cents above that.
unit price is 15$ per pound.
Display order price, discount, tax, shipping cost, and the billed amount.
('order price' above does not include tax and shipping cost.)
"""

#functions
def compute_order_price(wt):
    unit_price = 15.0
    price = wt * unit_price
    
    return price


def compute_discount(price):
    rate_discount = 0.03
    discount = 0.0
    if price > 100.0:
        discount = price * rate_discount

    return discount

def compute_tax(price):
    tax_rate = 0.08
    tax = price * tax_rate
    
    return tax


def submit():
    #inputs
    weight = float(input('Pounds ordered?>>'))
    #computations
    #1. compute price : input: weight output: price
    order_price = compute_order_price(weight)


    #2. compute discount, if any : input: order price output: discount
    discount_amount = compute_discount(order_price)
    
    #3. apply discount
    order_price -= discount_amount
    
    #4. compute tax input: order price output: tax
    tax = compute_tax(order_price)
    
    #5. find shipping rate input: weight output:ship rate
    
    
    #6. find the shipping cost input: rate, weight output: ship cost
    
    
    #7. find the billed amount
    billed_amount = order_price + tax



    #outputs
    print(f'''
    Weight(lb)\t:{weight:.2f}
    Order price\t:{order_price:.2f}
    Discount\t:{discount_amount:.2f}
    Tax Amount\t:{tax:.2f}
    Billed Amount\t:{billed_amount:.2f}

    ''')
#end submit 

#main
submit()

#NOTES

#average tax
#number of orders getting a discount 