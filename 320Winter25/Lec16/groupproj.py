#8:25

from os import name
import datetime
import random


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

def compute_price(products, quantity):# teamate 2
    unit_price = products['Unit_Price']

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


order_date = get_date()     #should we move this into submit?
# Format the date (for example: "23 January 2022")
order_date_string = order_date.strftime("%d %B %Y")
print(f'{order_date_string:15s}')





def submit_order():
    global products, order_id, orders
    price = 0
    #need to add/insert more order_details to the order dictionary.

    display_products()  # Displayed available products

    # menu = int(input('1.Submit Orders  2.Display Products  3.Exit\nChoose 1,2, or 3 for the product >> '))
    prod_id = int(input('Enter the product ID you wish to order >>> '))
    while prod_id not in products:
        print(f'You entered {prod_id:d} for your order. Please use 1001, 1002, or 1003')
        prod_id = int(input('Enter the product ID you wish to order >>> '))



    quantity = int(input('Enter the quantity to order >>>'))
    while quantity > products[prod_id]['Stock']:
            print(f'You entered {quantity:d} for your order. We have {products[prod_id]["Stock"]} available.')
            quantity = int(input('Enter the quantity you wish to order >>> '))

    #this needs to be verified using the key in prdoucts dictionary, how much quantity of product available?


    #compute price
    price = compute_price(products[prod_id], quantity)
    products[prod_id]['Stock'] = products[prod_id]['Stock']-quantity #updated available stock

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

    # return order_details
    # print(order_id,order_date,prod_id,name,quantity,price)
    # width = 34
    # line = '-' * width
    # print(line)
    # print(f'|{"Order ID":^10s}|{"Customer ID":^12s}|{"Date":^12s}|{"Product ID":^12s}|{"Product Name":^15s}|{"Quantity":^10s}|{"Price":^10s}|')
    # print(line)
    # for id in products:
    #   product_details = products[id]
    #   prod_id= product_details['ID']
    #   name = product_details['Product_Name']
    #   unit_price = product_details['Unit_Price']
    #   print(f'|{prod_id:^10d}|{name:^10s}|{unit_price:^10.2f}|')
    # print(line)
    # print('1.Apple, 2. Orange 3. Banana')

    # print(order_id, order_date, prod_id, name, quantity, price)
    width = 80
    line = '-' * width
    print(line)
    print(f'|{"Order ID":^10s}|{"Customer ID":^10s}|{"Order Date":^10s}|{"Product ID":^10s}|{"Product Name":^10s}|{"Quantity":^10s}|{"Price":^10s}|')
    print(line)
    #recommend hw 5 to insert attribute. get key first to get details, the taxpayer details is the next dictionary
    #need to
    for order_id in orders:
        order_details = orders[order_id]
        order_id = order_details['Order_ID']
        custom_id = order_details['Customer_ID']
        order_date = order_details['Date']
        prod_id = order_details['Product_ID']
        name = order_details['Product_Name']
        quantity = order_details['Quantity']
        price = order_details['Price']
    print(f'|{order_id:^10d}|{custom_id:^10d}|{prod_id:^10d}|{str(order_date):^10s}|{name:^10s}|{quantity:^10d}|{price:^10.2f}|')
    print(line)







    # #we need to print the current order in this.
    # while prod_id not in products:
    #     print(f'Product ID {prod_id:d} not found, please try again.')
    #     continue

    # if menu == 1:
    #    pass
    # elif menu ==2:
    #    display_products()
    # elif menu ==3:
    #    pass


def customer_login():
    global products, order_id, orders, custom_user_id

    customer_details = {
            101: {'ID': 101, 'Password': 'password101'},
            102: {'ID': 102, 'Password': 'password102'}
        }

    custom_user_id = int(input('Please enter your user ID >>>'))
    while custom_user_id not in customer_details:
        print(f'You entered {custom_user_id:d} as your customer user ID login. Please use 101, or 102')
        custom_user_id = int(input('Please enter your user ID >>>'))
    print(f'Great! You have a customer login ID. Now the next step.')

    custom_user_pass = str(input('Please enter your customer ID password >>>'))
    while custom_user_pass != customer_details[custom_user_id]['Password']:
        print(f'You entered {custom_user_pass:s} as your password. Please enter password101 or password102 for entry.')
        custom_user_pass = str(input('Please enter your customer ID password >>>'))
    print(f'Great! Now you have logged in. Great to see you user {custom_user_id:d} with password {custom_user_pass:s}')




    #while loop in for success or failed

def manager_login():
    global products, order_id, orders, manager_user_id
    manager_user_pass = 0 #localizing for print
    manager_details = {
            1: {'ID': 1, 'Password': 'password1'},
            2: {'ID': 2, 'Password': 'password2'}
        }
    manager_user_id = int(input('Please enter your manager user ID >>>'))
    while manager_user_id not in manager_details:
        print(f'You entered {manager_user_id:d} as your customer user ID login. Please use 1, or 2')
        manager_user_id = int(input('Please enter your manager user ID >>>'))

    print(f'Great! You have a manager login ID. Now the next step.')

    manager_user_pass = str(input('Please enter your manager ID password >>>'))
    while manager_user_pass not in manager_details[manager_user_id]['Password']:
        print(f'You entered {manager_user_pass:s} as your password. Please enter password1 or password2 for entry.')
        manager_user_pass = str(input('Please enter your manager ID password >>>'))
    print(f'Great! Now you have logged in. Great to see you user: {manager_user_id:d}, with password: {manager_user_pass:s}')
    return True

def print_order(order_id): #teamate 2
    global orders

    if order_id not in orders:
        print(f'Order ID {order_id} not found.')
        return

    order = orders[order_id]
    print("\nOrder Details:")
    print(f"Order ID: {order_id}")
    print(f"Order Date: {order['Order Date'].strftime('%d %B %Y')}")
    print(f"Product ID: {order['Product ID']}")
    print(f"Product Name: {order['Product Name']}")
    print(f"Quantity: {order['Quantity']}")
    print(f"Order Price: ${order['Order Price']:.2f}")
    print(f"Customer ID: {order['Customer ID']}")

def display_orders():#teamate 3    #this is customer display orders
    global orders, products, order_details, custom_user_id

    if not orders:
        print('No orders to display.')
        return

    print({custom_user_id})

    has_orders = False #this is initializing it before we cna find a match in the loop

    width = 80
    line = '-' * width
    print(line)
    print(f'|{"Order ID":^10s}|{"Customer ID":^10s}|{"Order Date":^10s}|{"Product ID":^10s}|{"Product Name":^10s}|{"Quantity":^10s}|{"Price":^10s}|')
    print(line)
    for order_id in orders:
        order_details = orders[order_id]
        if order_details['Customer_ID'] == custom_user_id:
            has_orders = True
            order_id = order_details['Order_ID']
            custom_id = order_details['Customer_ID']
            order_date = order_details['Date']
            prod_id = order_details['Product_ID']
            name = order_details['Product_Name']
            quantity = order_details['Quantity']
            price = order_details['Price']
            print(f'|{order_id:^10d}|{custom_id:^10d}|{prod_id:^10d}|{str(order_date):^10s}|{name:^10s}|{quantity:^10d}|{price:^10.2f}|')
            print(line)
    if not has_orders:
        print(f'No orders were found. Sorry!')





def manager_display_products():
    global products, order_id, orders
    stock = 0# intializing for print

    # stock = products['Stock']
    width = 46
    line = '-' * width
    print(line)
    print(f'|{"ID":^10s}|{"Name":^10}|{"Unit Price":^10s}|{stock:^10d}|')
    print(line)
    for id in products:
        product_details = products[id]
        prod_id= product_details['ID']
        name = product_details['Product_Name']
        unit_price = product_details['Unit_Price']
        stock = product_details['Stock']
        print(f'|{prod_id:^10d}|{name:^10s}|{unit_price:^10.2f}|{stock:^10}|')
    print(line)

    #instock

def manager_view_orders():
    global products, order_id, orders

    if not orders:
        print('No orders to see.')
        return

    print(orders)
    width = 80
    line = '-' * width
    print(line)
    print(f'|{"Order ID":^10s}|{"Customer ID":^10s}|{"Order Date":^10s}|{"Product ID":^10s}|{"Product Name":^10s}|{"Quantity":^10s}|{"Price":^10s}|')
    print(line)
    for order_id in orders:
        order_details = orders[order_id]
        order_id = order_details['Order_ID']
        custom_id = order_details['Customer_ID']
        order_date = order_details['Date']
        prod_id = order_details['Product_ID']
        name = order_details['Product_Name']
        quantity = order_details['Quantity']
        price = order_details['Price']
        print(f'|{order_id:^10d}|{custom_id:^10d}|{prod_id:^10d}|{str(order_date):^10s}|{name:^10s}|{quantity:^10d}|{price:^10.2f}|')
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


        while True:
            new_unit_price = float(input(f'Enter a new price for {products[prod_id_change]["Product_Name"]} you wish to change >>>'))
            if new_unit_price <= 0:
                print(f'Invalid, it needs to be a positive value, try agian.')
                continue
            break

        products[prod_id_change]['Unit_Price'] = new_unit_price
        print(f'Price is now updated for {products[prod_id_change]["Product_Name"]} now costs ${new_unit_price:.2f}.')





def inventory_reorder():
    manager_display_products()

def customer_logout():
    return

def manager_logout():
    return









# MAIN
#set up while llops and if statements,
#tupe line inside customer login and its done.
#blank function that returns manger id or customer login.

#1) start main or do submit

# Main Loop (Screen 1)
quit = False
while not quit :
    print('0. Login for customer   1. Login for manager   2. Quit')
    main_choice = int(input('Enter 0, 1, or 2 >>> '))

    # Screen 2A: Customer Menu
    if main_choice == 0:
        customer_login()


        # Setup customer details (could be used later in a login function)

        # 101: 102
        #login verification for customer. Where ID and passcode needs to be accessed. May want to store this away in a function.
        #similar to uname situation
        #if password_in == password:

        # Screen 2A: Customer Menu
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
                # Call customer_logout() if implemented
                print("Logging out customer...")
                break  # Exit customer menu and return to main menu
            elif cust_choice == 4:
                quit = True
                break # Exit the entire program (DONT USE EXIT) will need more than the break.
            else:
                print("Invalid option. Please try again.")


    # Screen 2B: Manager Menu
    elif main_choice == 1:
        # Setup manager details (could be used later in a login function)
        manager_login() # if it returns a true or false then you can use it to continue.
        #login has to succeed before displaying menu - validation
        # login
        #validation
        # Screen 2B: Manager Menu
        while True:
            print("\nManager Menu:")
            print("1. View all orders")
            print("2. Edit prices")
            print("3. Reorder inventory")
            print("4. Logout")
            print("5. Quit")
            mgr_choice = int(input("Enter 1, 2, 3, 4, or 5 >>> "))
            if mgr_choice == 1:
                manager_view_orders()
            elif mgr_choice == 2:
                edit_prices()
            elif mgr_choice == 3:
                inventory_reorder()
            elif mgr_choice == 4:
                manager_logout()
                break  # Exit manager menu and return to main menu
            elif mgr_choice == 5:
                quit = True
                print('You chose to quit!')
                break
                      # Exit the entire program, this needs to be not exit #make a print statment too
            else:
                print("Invalid option. Please try again.")

    elif main_choice == 2:
        quit = True  # Quit the main loop

    else:
        print("Invalid choice. Please choose 0, 1, or 2.")

print("Goodbye!")










     # customer_details = {}
    # # customer_password = customer_details['Password']
    # # customer_id = customer_details['ID']
    # manager_details = {}
    # # manager_id = manager_details['ID']
    # # manager_password = manager_details['Password']
    # # print("1. Submit Order, 2. View Orders, 3. Logout, 4. Quit")
    # # print("Enter 1,2,3, or 4")
    # #True is always true . infinite loop ==> provide a break to exit
    # while True: #screen 2a, this will become an inner loop in the main
    #     print('1.Submit Order 2. Display Orders 3. Exit')
    #     choice = int(input('1 2 or 3 >>>  '))
    #     if choice == 1:
    #         submit_order()
    #     elif choice == 2:
    #         display_orders()
    #     elif choice == 3:
    #         break
    #         # elif choice < 1 or choice > 3:
    #         #    print('Invalid choice! Please Choose 1,2, or 3')
    #         #    continue
    #     print('Goodbye!')














"""Make Two dictionaries.
1 Products - already filled with data.
Attributes of products: id, name, unit price, stock (quantity available)
Make up your own products. Minimum 3 products. You can use id as the key.

2 Orders - Initialized as an empty dictionary, and filled
as the program runs.
key - order id starts with 10001
Value is a dictionary/list with attributes order date,
product id, product name, quantity, order price.

You will be adding a customer id attribute to each order later.
You may want to include a customer id as a dummy value (say 1001)
now, so that you don't need to edit your prints or recalculate widths
later.


Customer is presented with a choice using a loop:
1. Submit Order 2.View Orders 3. Done

1.
A submit_order() function will:
-display products to the user
-prompt user to select a product, validating their selection
-prompt user to enter quantity ordered
-compute order price
-generate an order date (random date in the interval 2021 to 2023)
-make an order details dictionary
-add that to the orders dictionary
-print order details

2.
A display_orders() function will:
- display all the orders, nicely presented including
width, justification, captions etc.
- the order date is stored in the dictionary as a date (not a string)
- display_orders will convert the date to a string first, before displaying the orders.clear


Date:
- a get_date() function will return a random date in the interval 1/1/2021 through
12/31/2023. submit will use this to generate order date, and store it as a date.
- display will first convert this date to a string before printing.
- References for doing both are given to you below. When you start, if this
code is not ready, you can leave the date as a random string value, printed
with reasonable width, for example ^12s.
get_date()
Independent Task:  Generate an order_date using a get_date() function.
 Can be done independently by a team member.
  Parameters - start date, end date, or implement without parameters.
Returns - a random date within the range.
Return a date, not a string version of the date.
Submit_orders() calls the get_date() function to get an order date
- defined as a random date within a specified range of years (for example: 2021-2023).
You can use this reference:- Reference to generate a random date Links to an external site.
Submit will include the order date as an attribute in the order (as a date, without converting to a string)"""