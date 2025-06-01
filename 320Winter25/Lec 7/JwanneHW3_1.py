""" Homework 3 Question 1   Developed by JC     01.29.25

This app computes the order price for books ordered.
Order price includes the shipping_or_tax_cost.
The order price depends on how many books are ordered and where they are ordered.
Books cost $15 each.
For books that are ordered offline, you multiply book_price by books_ordered, then add by the cost of tax, which is 0.075 * price. 
For books ordered online, you add the same base cost of order price to the cost of shipping, which further depends on the number of books ordered.
If user orders <= 10 books, shipping = 0.25 * books.
If user orders > 10 books, shipping = 0.3 * books. 
Once you have the shipping_or_tax_cost, you just add that to order price, thereby redeclarating order_price with a new value. 
Lastly, print the order price.

input: books_ordered (int), type_order (int)
output: order_price (float), shippingORtax_cost (float)
"""

#functions
def compute_shipping_or_tax_cost(price, books, type):
    if type == 0:
        rt = 0.075
        shipping_or_tax_cost = rt * price

    else:
        if books <= 10:
            rt = 0.25
        else:
            rt = 0.3
        shipping_or_tax_cost = rt * books 
    
    return shipping_or_tax_cost

#main
#initializations 
book_price = 15.0

#input
books_ordered = int(input('Enter books ordered\n>>'))
type_order = int(input('Enter 1 for online orders, Enter 0 for offline orders\n>>'))

#computations
#1 compute the order price based on books_ordered 
order_price = book_price * books_ordered

#2 compute shipping/tax_cost based on offline or online #in: 
shipping_or_tax_cost = compute_shipping_or_tax_cost(order_price, books_ordered, type_order)

#3 add shipping_or_tax to order price 
order_price += shipping_or_tax_cost 

#output
print(f'Order price is ${order_price:.2f}')