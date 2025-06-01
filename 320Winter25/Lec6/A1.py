"""A1:In Class Coding Assignment    Devloped by JC      01.21.24

Q1: User types in weight ordered (in pounds).  User also specifies mode of shipment (express or standard) by 
typing in 1 for express and 0 for standard shipping.  (Every order is either express, or standard shipment)
The unit price per pound is 5 dollars. For express shipping, rate of shipping is 50 cents per pound for 
weights at or below 10 pounds, and 70 cents per pound  otherwise. For standard shipping, rate is 20 
cents per pound for weights at or below 20 pounds,  and 40 cents per pound otherwise. Your code finds 
the shipping rate matching the weight and the mode of shipment. 
Your app computes:    order price and the shipping cost.   (shipping cost is a simple multiplication by the selected rate)
You app displays:    weight ordered,  order_price and the shipping cost.

inputs: weight (float), 


"""

#Initializations
unit_price_pound = 5.0
#for express shipping:  rate_shipping_pound = .5 as long as weight <= 10.0 (otherwise if weight > 10.0, then rate_shipping_pound = 0.7
#for standard shipping:   rate_shipping
#Inputs
weight = float(input(f'How many pounds did you order?\n>>'))
mode_shipment = int(input('Enter 1 for express shipping, and 0 for standard shipping\n>>'))

if mode_shipment == 1:
    if weight <= 10.0:
        rate_shipping_pound = 0.5
    else:
        rate_shipping_pound = 0.7

else:
    if weight <= 20.0:
        rate_shipping_pound = 0.2
    else:
        rate_shipping_pound = 0.4


#Computations 
shipping_cost = weight * rate_shipping_pound
order_price = shipping_cost * unit_price_pound

#Output
print(f'The weight of your order is {weight:.2f} pounds')
print(f'Your order price is {order_price:.2f}')
print(f'The shipping cost is {shipping_cost:.2f}')
