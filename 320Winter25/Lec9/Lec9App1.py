"""Lecture 9 App 1  Developed by JC     02.04.25






User specifies the number of books ordered, and if the order is online, or not
in: num_books, is_online(1/0) (int)
out: 
    submit: order price, inclusive of shipping/tax (float)
    summary: number of online orders (online_count:int), number of offline orders (offline_count:int), 
average revenue across all orders (average_revenue:float)
"""

#globals 
total_revenue = 0.0 #sum of order prices, excluding ship/tax, for average rev calculation
online_count = 0    #number of online orders
offline_count = 0   #number of offline orders 

#functions
def cost_ship_cost(books):
    if books <= 10:
        rt = 0.25
        cost = rt * books
    else:
        cost = 5.0

    return cost
    

def compute_tax(price):
    tax_rate = 0.08
    tax = price * tax_rate 
    
    return tax
#do not do books * unit_price * tax_rate here   #dont separate variables  

def submit():
    global total_revenue, online_count, offline_count #'re-declaration'
    #inputs
    num_books = int(input('Enter number of books >>'))
    is_online = int(input('Enter 1 if online, 0 for offline >>'))

    #computations
    ship_cost = 0.0
    tax = 0.0
    #1 compute the price 
    unit_price = 15.0
    order_price = num_books * unit_price
    total_revenue += order_price
    #2 if online order:
        #compute the shipping cost 
    # otherwise:
    #   compute the tax 
    if is_online:   # if is_online == 1
        ship_cost = cost_ship_cost(num_books)
        online_count += 1
    else:
        tax = compute_tax(order_price)
        offline_count += 1
   
   #we have combined the two if statements since both were asking if order is online 

   #3 add ship/tax to order price 
    order_price = order_price + ship_cost + tax 

   
        


    #outputs
    # print(f'Order price, inclusive of ship/tax: {order_price:.2f}')
#end submit
#order price (inclusive), and ship cost 
#order price (inclusive), and tax

    if is_online:
        print(f'Order price (inclusive) = {order_price:.2f}\nShip cost = {ship_cost:.2f}') 
    else: 
        print(f'Order price (inclusive) = {order_price:.2f}\nTax = {tax:.2f}') 
        



def compute_average_revenue():
    global total_revenue, online_count, offline_count

    order_count = online_count + offline_count      #we dont make order_count global
    if order_count > 0:
        avg = total_revenue / order_count
    else:
        avg = None

    return avg


def summary():
    global total_revenue, online_count, offline_count
    
    average_revenue = compute_average_revenue()
    
    if average_revenue is not None:     # dont use !=
        print(f'Average Revenue: {average_revenue:.2f}')
    else:
        print('No data for average revenue.')
    
    print(f'Online orders: {online_count:d}')
    print(f'Offline orders: {offline_count:d}')  #DIY add text, and {:d}
    #if your globals were order_count and online_count, you could find offline_count
    #here in summary by subtraction 
    #prints for the counts can be insuide or outside the if. choose based on context
#end summary 

def reset():
    global total_revenue, online_count, offline_count

    total_revenue = 0.0
    online_count = 0
    offline_count = 0




#main
quit = False
while not quit: #quit == False: #infinite loop with an exit #repeated 'if' is 'while' 
    print('1.Submit 2.Summary 3.Reset 4.Exit')
    print('Enter 1,2,3, or 4 >>')
    choice = int(input('Choice >>'))
    if choice == 1: 
        submit()
    elif choice == 2:
        summary()
    elif choice == 3:
        reset()
        print('Ready for a new batch...')
    elif choice == 4:
        quit = True 
    else:
        print('Invalid choice!')

print('Goodbye!')

"""
summary()
submit()    #each submit here is an order. 
submit()
submit()
summary()
#wish to start a new batch of orders.
reset()
print('Ready for a new batch...')
summary()
submit()
submit()
summary()
"""