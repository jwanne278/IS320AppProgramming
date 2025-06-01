"""oop1.py + oop2.py revision of oop1.py (class Taxpayerinit, str, display, save)

New: processline, load
add lines and headers to display 
    search <<
    update display with line, caption
    tax
    summary and reset 
    include tax in all outputs functions. <<csv line, str, update line, caption
    

class Taxpayer 
instance attributes: name, income, tax      (instance = object = each taxpayer) 
                                        (attributes of each instance of Taxpayer)

instance methods: (functions that belong to the object, taxpayer/self)
                    (instance = object    method = function inside class)
    init, str, compute_tax, display_line, csv_line

class variables:   count, count_hi
class methods:  compute_averages(), summary_report(), reset_data()
staticmethods:  line, caption

inside class: No prints, no input statements 
No reference to the list from inside the class.

count
"""

#globals
taxpayerlist = []

#classes
class Taxpayer:
    
    
    
    """
    instance attributes: (instance = object = each taxpayer) 
        name, income, tax     (attributes of each instance of Taxpayer)
    instance methods: (functions that belong to the object, taxpayer/self)
                        (instance = object    method = function inside class)
        
        init, str, compute_tax, display_line, csv_line
    class variables:   count, count_hi
    class methods:
        compute_averages(), summary_report(), reset_data()
    staticmethods:  
        line, caption
    """
    #class variables    one for the Taxpayer class, not one for each taxpayer object 
    count = 0   #this is: Taxpayer.count
    count_hi = 0 #income above 100000
    total_tax = 0.0

    cutoffs = {'WA':80000, 'OR':100000.0}

#------instance methods 
    def __init__(self, name, income, state):   #supports making object. inputs self + user inputs from submit 
        self.name = name    #this taxpayer object has an attribute, name
        self.income = income
        self.state = state
        #computations 
        self.tax = self.compute_tax()
        #update class variables
        Taxpayer.total_tax += self.tax
        Taxpayer.count = Taxpayer.count + 1
        if self.income > 100000.0:
            Taxpayer.count_hi += 1 

    #end init
    def __str__(self):  #supports the print, returns a string 
        return f'''
        Name\t: {self.name:s}
        Income\t:{self.income:.2f}
        State\t:{self.state:s}
        Tax\t:{self.tax:.2f}
        '''
    
    def compute_tax(self):
        if self.income > Taxpayer.cutoffs[self.state]:  #WA 80000   OR 100000
            rate = 0.1
        else:
            rate = 0.2

        return self.income * rate 
    
    
#main 
# txp1 = Taxpayer('Adam',10000.0)
# print(txp1)
# txp2 = Taxpayer('Ben', 2000.0)
# taxpayerlist.append(txp1)
# taxpayerlist.append(txp2)

# print(taxpayerlist)

# for taxpayer in taxpayerlist:
#     print(taxpayer)


#|Adam | 10000.00| for display
#we need a custom output? make a new method.
    
    def display_line(self):
        """Returns a one line string for use by display.
        e.g|Adam | 10000.00|
        """
        return f'|{self.name:<10s}|{self.income:>10.2f}|{self.state:^7s}|{self.tax:>10.2f}|'
    
    def csv_line(self):
        """Returns a csv string of taxpayer attributes, for use by save"""
        return f'{self.name:s},{self.income:.2f},{self.state:s},{self.tax:.2f}'
    
    
#class methods  work with class variables   (only)
    @classmethod
    def compute_averages(cls):
        """use total_tax and count to find average tax"""
        if cls.count > 0:
            avg = cls.total_tax / cls.count
        else:
            avg = None
        return avg  
    
    @classmethod
    def summary_report(cls):    #cls = class = Taxpayer
        """Return a string, to be printed by summary."""
        report = ''
        average_tax = cls.compute_averages()
        if average_tax is not None:
            report += f'Average Tax is {average_tax:.2f}'
        else:
            report += f'No data for average tax.'
        report += f'\nThe number of taxpayers is {cls.count:d}'   #not Taxayer.count
        report += f'\nThe number of taxpayers with high income is {cls.count_hi:d}'

        return report
    
    @classmethod
    def reset_data(cls):    #<--------check this before submission
        cls.count = 0
        cls.count_hi = 0
        cls.total_tax = 0.0

    #static/utility functions for line and caption 
    @staticmethod   #static/utility methods which do not need access to the self (no access to other attribute)
    def line():
        width = 42
        return '-' * width
    
    @staticmethod       #'decorator'
    def caption():
        return f'|{"Name":^10s}|{"Income":^10s}|{"State":^7s}|{"Tax":^10s}|'
#end class
#Note: staticmethod in python is not the same as static method in java/c++/c#
#functions

def process_line(line_in, sep=None):
    global taxpayerlist
    list_in = line_in.rstrip('\n').split(sep) #<------------------
    name = list_in[0]
    income = float(list_in[1])
    state = list_in[2]

    #validations, if any 

    #make a taxpayer object
    taxpayer = Taxpayer(name,income,state)      #---------->init
    # add that to the global list
    taxpayerlist.append(taxpayer)

    return taxpayer


def submit():
    line_in = input('Enter name, income, and state >> ')

    taxpayer = process_line(line_in)

    #print details of the taxpayer 
    print(taxpayer)
    


def load():
    global taxpayerlist

    filename = 'oop2in.txt'
    with open(filename, 'r') as load_file:
        for line in load_file:
            process_line(line, ',')

    print(f'Data loaded from {filename:s}')    #include count and filename in the print 


def display():
    global taxpayerlist

    if not taxpayerlist:
        print('No data to display')
        return
    
    print(Taxpayer.line())  #you call staticmethod using the class name 
    print(Taxpayer.caption())
    print(Taxpayer.line())
    for taxpayer in taxpayerlist:
        print(taxpayer.display_line())      # becomes display_line(taxpayer)     self = taxpayer
    print(Taxpayer.line())
#inside class - self.name  self.display_line())
#outside class - taxpayer.name      e.g. taxpayer.display_line()     <= you must have a 'taxpayer' to be able to do this
# u must alrady have an object to call for this 'for' function to work  

def summary():
    report = Taxpayer.summary_report()
    print(report)

    #print(Taxpayer.summary_report())

    
def save():
    if not taxpayerlist:
        print('No data to save')
        return
    #initialize an empty string
    #for each taxpayer,
    #add a csv line to the string 
    #open file, write string
    out_data = ''
    for taxpayer in taxpayerlist:
        out_data += taxpayer.csv_line() + '\n'
    with open('results.txt','w') as savefile:
        savefile.write(out_data.rstrip('\n'))


def reset():
    clear_data()
    Taxpayer.reset_data()


def clear_data():
    global taxpayerlist
    taxpayerlist.clear()

def search():
    global taxpayerlist
    if not taxpayerlist:
        print('No data to search in')
        return
    
    #search by name
    name_in = input('Enter name to search for >> ')
    found = False
    for taxpayer in taxpayerlist:
        if name_in.upper() == taxpayer.name.upper():    #case-insensitive search - all inputs return the same uppercase result 
            found = True
            print(taxpayer)
    if not found:
        print(f'No taxpayer with name {name_in:s}')
#.lower()   .upper()    .title()    .capitalize()   str functions



#main
quit = False
while not quit:
   print('1.Submit 2.Load 3.Summary 4.Save 5.Display 6.Search 7. Reset 8. Exit')
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
       print('Data cleared. Ready for new series...')
   elif choice == 8:
       quit = True   
       clear_data()     #emptying out global data structures 
   else:
       print('Invalid Choice!')



#CODE TO Deal with FILE LOCATION ISSUES
#ENSURE input file is in same folder as .py file.
""" To Make your code work with text files in same folder as the .py files regardless of environment and editor used:
use this code. (the import statement goes as the first line in your .py file, the rest goes where you do the file open and read, and replace the .txt with your filename
this assumes your input file is in same folder as .py file

import os.path   #first line up top in .py

filepath = os.path.dirname(__file__)
filename = os.path.join(filepath, 'test.txt')  # replace test.txt with what you need

with open(filename, 'r') etc..


student.name
"""