"""Dictionaries Intro Submission        Developed by JC     02.20.25 


"""


#TASK  1

#Store unit prices in a dictionary with keys Artichokes, Carrots, Beets
unit_prices = {}
unit_prices['Artichokes'] = 1.5
unit_prices['Beets'] = 2.5
unit_prices['Carrots'] = 1.0

#unit_prices =
print(unit_prices)

#Prompt user to input weights for each produce item
wt_a = float(input('Weight for artichokes >>'))
wt_b = float(input('Weight for beets >>'))
wt_c = float(input('Weight for carrots>>'))

#price =
price = unit_prices['Artichokes'] * wt_a + unit_prices['Beets'] * wt_b + unit_prices['Carrots'] * wt_c
print(f'Total Price is ${price:.2f}')





#TASK 2

#prices in dictionary
weights = {} #initialize empty dictionary

#fill weights dictionary with inputs
#for example,
# weights['Artichoke'] = float(input('Weight for artichokes >>'))

weights['Artichoke'] = float(input('Weight for artichokes >> '))
weights['Beets'] = float(input('Weight for beets >> '))
weights['Carrots'] = float(input('Weight for carrots >> '))


#use both dictionaries, the one for unit prices from previous cell, and the
unit_prices = {}
unit_prices['Artichokes'] = 1.5
unit_prices['Beets'] = 2.5
unit_prices['Carrots'] = 1.0

#weights dictionary, to compute the price below.
price1 = weights['Artichoke'] * unit_prices['Artichokes'] 
price2 = weights['Beets'] * unit_prices['Beets']
price3 = weights['Carrots'] * unit_prices['Carrots']
price = price1 + price2 + price3

print(f'Price: ${price:.2f}')

#Review the code, and consider: can we use the for loop?

#Essentially we want a loop that calculates price 3 times 
#based on 3 different food items 
produce = {
    1: {'Name': 'Artichoke', 'unit price': 1.5, 'price': price1},
    2: {'Name': 'Beets', 'unit price': 2.5, 'price': price2},
    3: {'Name': 'Carrots', 'unit price': 1.0, 'price': price3}
}

for id in produce:
  a_produce = produce[id]
  name = a_produce['Name']
  unit_price = a_produce['unit price']
  price = a_produce['price']
  print(f'|{id}|{name:<10s}|{unit_price:>10.2f}|{price:>10.2f}|')





#TASK 3

unit_price = {}
unit_price['Artichokes'] = 1.5
unit_price['Beets'] = 2.5
unit_price['Carrots'] = 1.0

choice = int(input('1.Artichokes 2 Beets 3 Carrots. Enter 1 2 or 3 >> '))
weight_a = float(input('Enter weight ordered in lb >> '))
weight_b = float(input('Enter weight ordered in lb >> '))
weight_c = float(input('Enter weight ordered in lb >> '))

orders = {
    1: {'product': 'Artichoke', 'weight': weight_a, 'price': weight_a * unit_price['Artichokes']},
    2: {'product': 'Beets', 'weight': weight_b, 'price': weight_b * unit_price['Beets']},
    3: {'product': 'Carrots', 'weight': weight_c, 'price': weight_c * unit_price['Carrots']}
}

for id in orders:
  a_order = orders[id]
  product = a_order['product']
  weight = a_order['weight']
  price = a_order['price']
  print(f'|{product:10s}|{weight:10.2f}|{price:10.2f}|')

#more efficient way to code the above 
# for id in orders:
#   print(orders[id]['product'], orders[id]['weight'], orders[id]['price'])