from os import name
import datetime
import random

"""This program is a product order managment system that manages an inventory of products and facilitates order processing for customers. It includes 
features for displaying available products, handling customer/manager logins, submitting and tracking 
orders, and updating stock levels. This progam contains user authentication for more secute usage. A dictionary is used to store all details about previous orders.
"""

# Products dictionary
products = {
    1001: {'ID':1001,'Product_Name': 'Apple', 'Unit_Price': 2, 'Stock': 30,'InStock':True },   #include the "inStock=True"
    1002: {'ID':1002,'Product_Name': 'Orange', 'Unit_Price': 4, 'Stock': 60,'InStock':True},
    1003: {'ID':1003,'Product_Name': 'Banana', 'Unit_Price': 6, 'Stock': 90,'InStock':True}
}

#globals
order_id = 10000 #starting at 10001
orders = {} #initializing as empty dictionary
manager_user_id = 0 #globalizing the manager ID to be tracked
custom_user_id = 0 #glbalizing the customer ID to be tracked  

'''
orders = {
  10001: {'Order_ID':10001,'Customer_ID':dummyval,'Order_date':randomday,'product_id': 1001, 'product_name':'name','Quantity':100,'Order_Price':5},
  10002: {'Order_ID':10002,'Customer_ID':dummyval,'Order_date':randomday,'product_id': 1002, 'product_name':'name','Quantity':100,'Order_Price':5},

}
'''

def compute_price(prod_id, quantity):
    unit_price = products[prod_id]['Unit_Price'] #Edit #2

    price = unit_price * quantity
    return price

def display_products(): #teamate 3
    global products, orders, product_details

    if not products:    #empty check
        print('No data to display')
        return  #exit display products function


    width = 34
    line = '-' * width
    print(line)
    print(f'|{"ID":^10s}|{"Name":^10}|{"Unit Price":^10s}|')
    print(line)
    for id in products:
      product_details = products[id]
      prod_id= product_details['ID']
      name = product_details['Product_Name']
      unit_price = product_details['Unit_Price']
      print(f'|{prod_id:^10d}|{name:^10s}|{unit_price:^10.2f}|')
    print(line)
    print('1.Apple, 2. Orange 3. Banana')


def get_date(): #teamate 1
    start_date = datetime.date(2022, 1, 1)
    end_date = datetime.date(2023, 12, 31)

    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date)
        current_date += datetime.timedelta(days=1)
    return random.choice(dates)

#new function
def can_meet_order_of(prod_id, quantity):
    return products[prod_id]['Stock'] >= quantity 

#new function

def update_stock(product, quantity):
    product['Stock'] += quantity
    product['InStock'] = product['Stock'] > 0

def submit_order():
    global products, order_id, orders
    price = 0
    #need to add/insert more order_details to the order dictionary.

    display_products()  # Displayed available products

    # menu = int(input('1.Submit Orders  2.Display Products  3.Exit\nChoose 1,2, or 3 for the product >> '))
    prod_id = int(input('Enter the product ID you wish to order >>> '))
    while prod_id not in products or products[prod_id]["Stock"] ==0:
        if prod_id not in products:
            print(f'You entered {prod_id:d} for your order. Please use 1001, 1002, or 1003')
        else:
            print(f'Sorry, the product: {products[prod_id]["Product_Name"]} is out of stock!') #checking if its out of stock
        prod_id = int(input('Enter a different product ID you wish to order >>> '))

    quantity = int(input('Enter the quantity to order >>>'))
    while not can_meet_order_of(prod_id, quantity):
            print(f'You entered {quantity:d} for your order. We cannot fulfill the order because we have {products[prod_id]["Stock"]} available.')
            quantity = int(input('Enter the quantity you wish to order >>> '))

    #this needs to be verified using the key in prdoucts dictionary, how much quantity of product available?
    
    #compute price
    price = compute_price(prod_id, quantity) # Corrected here

    #deducting order quantity from stock using update_stock 
    update_stock(products[prod_id], -quantity) 


    #get date 
    order_date = get_date()
    #initialize order details dictionary 
    order_details = {}
    #insert attributes

    order_id +=1
    # order_details = orders[order_id]
    order_details['Order_ID'] = order_id
    order_details['Customer_ID'] = custom_user_id
    order_details['Date'] = order_date
    order_details['Product_ID'] = prod_id
    order_details['Product_Name'] = products[prod_id]['Product_Name']
    order_details['Quantity'] = quantity
    order_details['Price'] = price
    
    orders[order_id] = order_details
    print_order(order_id) #Edit #7


def customer_login():
    global custom_user_id #Edit #3

    customer_details = {
            101: {'ID': 101, 'Password': 'password101'},
            102: {'ID': 102, 'Password': 'password102'}
        }
    
    custom_user_id = int(input('Please enter your customer ID >>>')) #get rid of the comments that tell you the answer 
    while custom_user_id not in customer_details:
        print(f'You entered {custom_user_id:d} as your customer user ID login. Please use a valid customer login for entry.')
        custom_user_id = int(input('Please enter your user ID >>>'))
    print(f'Great! You have a customer login ID. Now the next step.')

    custom_user_pass = str(input('Please enter your customer ID password >>>'))#get rid of the comments that tell you the answer
    while custom_user_pass != customer_details[custom_user_id]['Password']:
        print(f'You entered {custom_user_pass:s} as your password. Please enter a valid customer password for entry.')
        custom_user_pass = str(input('Please enter your customer ID password >>>'))
    print(f'\nGreat! Now you have logged in. Great to see you user {custom_user_id:d}!')


    

    #while loop in for success or failed

def manager_login():
    global products, order_id, orders, manager_user_id
    manager_user_pass = 0 #localizing for print
    manager_details = {
            1: {'ID': 1, 'Password': 'password1'},
            2: {'ID': 2, 'Password': 'password2'}
        }
    manager_user_id = int(input('Please enter your manager user ID >>>'))#get rid of the comments that tell you the answer
    while manager_user_id not in manager_details:
        print(f'You entered {manager_user_id:d} as your customer user ID login. Please enter a valid manager user id for entry.')
        manager_user_id = int(input('Please enter your manager user ID >>>'))
    
    print(f'Great! You have a manager login ID. Now the next step.')

    manager_user_pass = str(input('Please enter your manager ID password >>>'))#get rid of the comments that tell you the answer
    while manager_user_pass != manager_details[manager_user_id]['Password']:
        print(f'You entered {manager_user_pass:s} as your password. Please enter a valid manager password for entry.')
        manager_user_pass = str(input('Please enter your manager ID password >>>'))
    print(f'\nGreat! Now you have logged in. Great to see you user {manager_user_id:d}!')
    return True 

def print_order(order_id): #teamate 2
    global orders

    if order_id not in orders:
        print(f'Order ID {order_id} not found.')
        return

    order = orders[order_id]
    print("\nOrder Details:")
    print(f"Order ID: {order['Order_ID']}") #Edit #4
    print(f"Order Date: {order['Date'].strftime('%d %B %Y')}")
    print(f"Product ID: {order['Product_ID']}")
    print(f"Product Name: {order['Product_Name']}")
    print(f"Quantity: {order['Quantity']}")
    print(f"Order Price: ${order['Price']:.2f}")
    print(f"Customer ID: {order['Customer_ID']}")

def display_orders():#teamate 3    #this is customer display orders
    global orders, products, order_details, custom_user_id

    if not orders:
        print('No orders to display.')
        return
    
    has_orders = False #this is initializing it before we cna find a match in the loop

    width = 90
    line = '-' * width
    print(line)
    print(f'|{"Order ID":^10s}|{"Customer ID":^10s}|{"Order Date":^16s}|{"Product ID":^10s}|{"Product Name":^15s}|{"Quantity":^10s}|{"Price":^10s}|')
    print(line)
    for order_id in orders:
        order_details = orders[order_id]
        if order_details['Customer_ID'] == custom_user_id:
            has_orders = True
            order_id = order_details['Order_ID']
            custom_id = order_details['Customer_ID']
            order_date = order_details['Date'].strftime('%d %B %Y') #Edit #9
            prod_id = order_details['Product_ID']
            name = order_details['Product_Name']
            quantity = order_details['Quantity']
            price = order_details['Price']
            print(f'|{order_id:^10d}|{custom_id:^11d}|{order_date:^16s}|{prod_id:^10d}|{name:^15s}|{quantity:^10d}|{price:^10.2f}|')
            print(line)
    if not has_orders:
        print(f'No orders were found. Sorry!')




def manager_display_products():
    global products, order_id, orders
    stock = 0# intializing for print

    # stock = products['Stock']
    width = 56
    line = '-' * width
    print(line)
    print(f'|{"ID":^10s}|{"Name":^10}|{"Unit Price":^10s}|{"In Stock":^10s}|{"Stock":^10s}|') #EDIT #1
    print(line)
    for id in products:
        product_details = products[id]
        prod_id= product_details['ID']
        name = product_details['Product_Name']
        unit_price = product_details['Unit_Price']
        stock = product_details['Stock']
        in_stock = 'Yes' if product_details['InStock'] else 'No' #Edit #6
        print(f'|{prod_id:^10d}|{name:^10s}|{unit_price:^10.2f}|{in_stock:^10s}|{stock:^10d}|')
    print(line)



def manager_view_orders():
    global products, order_id, orders

    if not orders:
        print('No orders to see.')
        return
    
    width = 90
    line = '-' * width
    print(line)
    print(f'|{"Order ID":^10s}|{"Customer ID":^10s}|{"Order Date":^16s}|{"Product ID":^10s}|{"Product Name":^15s}|{"Quantity":^10s}|{"Price":^10s}|')
    print(line)
    for order_id in orders:
        order_details = orders[order_id]
        order_id = order_details['Order_ID']
        custom_id = order_details['Customer_ID']
        order_date = order_details['Date'].strftime('%d %B %Y') #Edit #10
        prod_id = order_details['Product_ID']
        name = order_details['Product_Name']
        quantity = order_details['Quantity']
        price = order_details['Price']
        print(f'|{order_id:^10d}|{custom_id:^11d}|{order_date:^16s}|{prod_id:^10d}|{name:^15s}|{quantity:^10d}|{price:^10.2f}|')
        print(line)



def edit_prices():
    global products, order_id, orders
    manager_display_products()

    while True:
        prod_id_change = int(input('Enter the product ID you wish to change or 0 if you want to exit>>> '))
        if prod_id_change == 0:
            print('Exiting price editing')
            return 
        
        while prod_id_change not in products:
            print(f'You entered {prod_id_change:d} for your order. Please use 1001, 1002, or 1003')
            prod_id_change = int(input('Enter the product ID you wish to order >>> '))
        
        current_price = products[prod_id_change]['Unit_Price']
        product_name = products[prod_id_change]["Product_Name"]
        print(f'\nThe current price for {product_name:s} is ${current_price:.2f}.')
        
        while True:
            new_unit_price = float(input(f'Enter a new price for product {products[prod_id_change]["Product_Name"]} you wish to change to >>>'))
            if new_unit_price <= 0:
                print(f'Invalid, it needs to be a positive value, try again.')
                continue
            break

        products[prod_id_change]['Unit_Price'] = new_unit_price
        print(f'Price is now updated for {products[prod_id_change]["Product_Name"]}, which now costs ${new_unit_price:.2f}.')

def inventory_reorder():
    global products, order_id, orders
    manager_display_products()

    while True:
        prod_id_restock = int(input('Enter the product ID you wish to restock or 0 if you want to exit>>> '))
        if prod_id_restock== 0:
            print('Exiting price editing')
            return 
        
        while prod_id_restock not in products:
            print(f'You entered in {prod_id_restock:d} for your order. Please use 1001, 1002, or 1003')
            prod_id_restock = int(input('Enter the product ID you wish to restock >>> '))

        while True:
            restock_quantity = int(input(f'Enter the quantity to add for {products[prod_id_restock]["Product_Name"]} >>>'))
            if restock_quantity <= 0:
                print(f'Invalid, it needs to be a positive number')
                continue 
            break

        #increase stock using update_stock()
        update_stock(products[prod_id_restock], restock_quantity)

        print(f'Stock is now updated to your specified {products[prod_id_restock]["Stock"]:d} units.')


def customer_logout():
    global custom_user_id
    custom_user_id = 0
    print("Customer logged out.")

def manager_logout():
    global manager_user_id
    manager_user_id = 0
    print("Manager logged out.")


# Main Loop (Screen 1)
quit_program = False

while not quit_program:
    print("\nMain Menu:")
    print("1. Login")
    print("2. Quit")
    choice = int(input("Choose 1 or 2 >>> "))

    if choice == 1:
        # Step 1: Ask if Manager or Customer
        print("\nLogin Menu:")
        print("1. Customer Login")
        print("2. Manager Login")
        login_type = int(input("Choose 1 or 2 >>> "))

        if login_type == 1:
            # Perform customer login
            customer_login()
            if custom_user_id != 0:
                # If successful, show Customer Menu
                while True:
                    print("\nCustomer Menu:")
                    print("1. Submit Order")
                    print("2. View Orders")
                    print("3. Logout")
                    print("4. Quit")
                    cust_choice = int(input("Enter 1, 2, 3, or 4 >>> "))
                    if cust_choice == 1:
                        submit_order()
                    elif cust_choice == 2:
                        display_orders()
                    elif cust_choice == 3:
                        customer_logout()
                        break  # back to Main Menu
                    elif cust_choice == 4:
                        quit_program = True
                        break
            else:
                print("Customer login failed. Returning to Main Menu...")

        elif login_type == 2:
            # Perform manager login
            if manager_login():  # returns True if successful
                if manager_user_id != 0:
                    # Show Manager Menu
                    while True:
                        print("\nManager Menu:")
                        print("1. Display Products")
                        print("2. View Orders")
                        print("3. Edit Prices")
                        print("4. Reorder Inventory")
                        print("5. Logout")
                        print("6. Quit")
                        manager_choice = int(input("Enter 1, 2, 3, 4, 5, or 6 >>> "))
                        if manager_choice == 1:
                            manager_display_products()
                        elif manager_choice == 2:
                            manager_view_orders()
                        elif manager_choice == 3:
                            edit_prices()
                        elif manager_choice == 4:
                            inventory_reorder()
                        elif manager_choice == 5:
                            manager_logout()
                            break  # back to Main Menu
                        elif manager_choice == 6:
                            quit_program = True
                            break
                else:
                    print("Manager login failed. Returning to Main Menu...")
            else:
                print("Manager login failed. Returning to Main Menu...")

        else:
            print("Invalid login choice. Returning to Main Menu...")

    elif choice == 2:
        quit_program = True
    else:
        print("Invalid choice. Please choose 1 or 2.")
