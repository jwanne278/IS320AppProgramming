"""jwanneHW7.py          Developed by JC      03.15.25

This program manages order data such as quanitities, price, tax, and
creates reports for online/offline orders for multiple countries.
Some features include an Order class for managing individual orders,
class/static/instance methods for aggregating data and reporting it back
to the user, and functions for user to input data, process data, search data, etc.
Countries Supported: US, CA
Tax Rates: US - 8%, CA - 3%
"""

#globals 
orderlist = []
needs_save = False

#classes
class Order:
    #class variables    one for the Order class, not one for each order object 
    count = 0   #this is: Order.count
    countoff = 0 
    counton = 0
    total_quantity = 0
    total_quantoff = 0

    rates = {'US':0.08, 'CA':0.03}

    """
        instance attributes: (instance = object = each order) 
            name, quantity, online_status(1/0)     (attributes of each instance of Order)
        instance methods: (functions that belong to the object, taxpayer/self)
                            (instance = object    method = function inside class)
            
            init, str, compute_tax, display_line, csv_line
        class variables:   count, count_hi
        class methods:
            compute_averages(), summary_report(), reset_data()
        staticmethods:  
            line, caption
    """
    def __init__(self,name,quantity,online_status,country):    #supports making object. inputs self + user inputs from submit
        self.name = name    #this taxpayer object has an attribute, name
        self.quantity = quantity
        self.online_statuscode = online_status
        self.country = country
        #computations 
        self.price = self.compute_price()
        self.tax = self.compute_tax()
        #update class variables
        Order.total_quantity += self.quantity
        Order.count = Order.count + 1
        if self.online_statuscode == 0:
            Order.countoff += 1 
            Order.total_quantoff += self.quantity
            self.online_status = 'Offline'
        else:
            Order.counton += 1
            self.online_status = 'Online'


    def __str__(self):  #supports the print, returns a string      
        return f'''
        Name\t\t:{self.name:s}
        Quantity\t:{self.quantity:d}
        Type\t\t:{self.online_status:s}
        Country\t\t:{self.country:s}
        Price\t\t:{self.price:.2f}
        Tax\t\t:{self.tax:.2f}
        '''
    
    def compute_price(self): 
        unit_price = 10.0
        self.price = unit_price * self.quantity

        return self.price


    def compute_tax(self):
        self.tax = self.price * Order.rates[self.country]       #US 0.08   CA 0.03
     
        return self.tax

    


    def display_line(self):
        """Returns a one line string for use by display.
        e.g|Adam | 10000.00|
        """
        return f'|{self.name:<10s}|{self.quantity:^10d}|{self.online_status:^10s}|{self.country:^10s}|{self.price:>10.2f}|{self.tax:>10.2f}|'
    
    def csv_line(self):
        """Returns a csv string of order attributes, for use by save"""
        return f'{self.name:s},{self.quantity:d},{self.online_status:s},{self.country:s},{self.price:.2f},{self.tax:.2f}'
    

    @classmethod
    def compute_averages(cls):
        """use total_quantity and count to find average quantity"""
        
        if cls.count > 0:
            avg = cls.total_quantity / cls.count
            if cls.countoff > 0:
                avg_quantoff = cls.total_quantoff / cls.countoff
            else:
                avg_quantoff = None
        else:
            avg = None
            avg_quantoff = None
        
        return avg, avg_quantoff 
        

    @classmethod
    def summary_report(cls):    
        """Return a string, to be printed by summary."""
        report = ''
        average_quantity, average_quantoff = cls.compute_averages()
        if average_quantity is not None:
            report += f'Average Quantity: {average_quantity:.1f}\n'
            if average_quantoff is not None:
                report += f'Average Offline Quantity: {average_quantoff:.1f}\n'
            else:
                report += f'No data for Offline Average Quantity.\n'
        else:
            report += f'No data to compute averages with.\n'

        report += f'Number of online orders: {cls.counton:d}'   
        
        return report
    

    @classmethod
    def reset_data(cls):
        
        cls.count = 0   
        cls.countoff = 0 
        cls.counton = 0
        cls.total_quantity = 0
        cls.total_quantoff = 0

    #static/utility functions for line and caption 
    @staticmethod   #static/utility methods which do not need access to the self (no access to other attribute)
    def line():
        width = 67
        return '-' * width
    
    @staticmethod       #'decorator'
    def caption():
        return f'|{"Name":^10s}|{"Quantity":^10s}|{"Status":^10s}|{"Country":^10s}|{"Price":^10s}|{"Tax":^10s}|'
#end class
    

#functions 
def process_line(line_in, sep=None):
    global orderlist, needs_save
    needs_save = True

    list_in = line_in.rstrip('\n').split(sep) #<------------------
    name = list_in[0]
    quantity = int(list_in[1])
    online_status = int(list_in[2])
    country = list_in[3] 

    #validations
    #online_status must be 1 or 0 
    while online_status not in {1,0}:  
        print(f'You entered {online_status:d} for online status. Please use 1 or 0')
        online_status = int(input('Enter 1 or 0 for online status >> '))

    #quantity must be above 0, inclusive.
    while quantity < 0:
        print(f'You entered {quantity:d} for quantity.')
        quantity = int(input('Please enter a quantity greter than 0 or above >> '))

    #make a order object
    order = Order(name,quantity,online_status,country)      #---------->init
    # add that to the global list
    orderlist.append(order)

    return order


def submit():
    global orderlist, needs_save

    line_in = input('Name, quantity, online/offline (1/0 >>) and country (US or CA) >> ')

    order = process_line(line_in)

    print(order)
   

def load():
    global orderlist, needs_save 

    count = 0
    filename = 'hw7_inputs.txt'
    with open(filename, 'r') as load_file:
        for line in load_file:
            process_line(line, ',')
            count += 1 
    print(f'{count:d} orders loaded from {filename:s}')


def summary():
    report = Order.summary_report()
    print(report)


def display():
    global orderlist

    if not orderlist:
        print(f'No data to display')
        return
    
    print(Order.line())  
    print(Order.caption())
    print(Order.line())
    for order in orderlist:
        print(Order.display_line(order))      
    print(Order.line())



def save():
    """Saves the data only if necessary."""
    global needs_save
    
    if not orderlist:
        print(f'No data to save')
        return
    
    if needs_save:
        count = 0
        savefilename = input('Enter name of file to save to >> ')
        out_data = ''
        for order in orderlist:
            out_data += order.csv_line() + '\n'
            count += 1
        with open (savefilename,'w') as savefile:
            savefile.write(out_data.rstrip('\n'))

        print(f'{count} orders saved to {savefilename}.') 
        needs_save = False  # Reset save flag after saving
    else:
        print("No changes to save.")
        

def search():
    global orderlist
    if not orderlist:
        print(f'No data to search in')
        return
    
    while True:
        menu = int(input('1 Search by Name  2 Search by Status 3 Done. 1,2 or 3 >> '))
        while menu not in {1,2,3}:
            print(f'You entered {menu:d} for searching. Please use 1,2 or 3')
            menu = int(input('Enter 1,2 or 3 for searching >> '))
        if menu == 1:
        #search by name
            name_in = input('Name to search for >> ')
            found = False
            for order in orderlist:
                if name_in.upper() == order.name.upper():    #case-insensitive search - all inputs return the same uppercase result 
                    found = True
                    width = 67
                    line = '-' * width 
                    print(line)
                    print(f'|{"Name":^10s}|{"Quantity":^10s}|{"Status":^10s}|{"Country":^10s}|{"Price":^10s}|{"Tax":^10s}|')
                    print(line)
                    print(f'|{order.name:<10s}|{order.quantity:^10d}|{order.online_status:^10s}|{order.country:^10s}|{order.price:>10.2f}|{order.tax:>10.2f}|')     # < left    > right     ^ center 
                    print(line)
                    
            if not found:
                print(f'No order with name {name_in:s}')
            
        elif menu == 2:
        #search by status
            status_in = int(input('Enter 1/0 to search for Online/Offline Orders >> '))
            
            while status_in not in {1,0}:  
                print(f'You entered {status_in:d} for online status. Please use 1 or 0')
                status_in = int(input('Enter 1 or 0 for online status >> '))

            found = False
            for order in orderlist:
                if status_in == order.online_statuscode:    #case-insensitive search - all inputs return the same uppercase result 
                    found = True
                    width = 67
                    line = '-' * width 
                    print(line)
                    print(f'|{"Name":^10s}|{"Quantity":^10s}|{"Status":^10s}|{"Country":^10s}|{"Price":^10s}|{"Tax":^10s}|')
                    print(line)
                    print(f'|{order.name:<10s}|{order.quantity:^10d}|{order.online_status:^10s}|{order.country:^10s}|{order.price:>10.2f}|{order.tax:>10.2f}|')     # < left    > right     ^ center 
                    print(line)
                
            if not found:
                print(f'No order with online status {status_in:s}')
        
        else:
            return

#.lower()   .upper()    .title()    .capitalize()   str functions

    
    
def reset():
    global needs_save
    if needs_save:
        save()
        needs_save = False  # Reset save flag after saving
    
    clear_data()
    Order.reset_data()
    # reset()
    print('Data cleared. Ready for new series...')


def clear_data():
    global orderlist
    orderlist.clear()


#main
quit = False
while not quit:
    print('1.Submit 2.Load 3. Summary 4.Save 5. Display 6.Search 7.Reset 8.Exit')
    choice = int(input('Enter choice:  '))
    if choice == 1:
        submit()
    elif choice == 2:
        load() 
    elif choice == 3:
        summary()
    elif choice == 4:
        save()
    elif choice == 5:
        display()
    elif choice == 6:
        search()
    elif choice == 7:
        reset()
    elif choice == 8:
        if needs_save:
            save()
            needs_save = False
        quit = True
    else:
        print('Invalid Choice!')
