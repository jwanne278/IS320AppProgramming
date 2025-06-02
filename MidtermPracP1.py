MidtermPracP1.py

#globals 

#functions 
# user inputs:  income, married or not (1/0)
# displayed output: tax

# married:   0.3 above 150000  0.2 otherwise
# not married:  0.2 above 100000 0.15 otherwise
"""Problem 1
summary output
displays:  average tax,   average tax for married people
functions:  one for each average.

"""
#global 
total_tax = 0.0     #sum of taxes, used for average
count = 0           #number of inputs, used for average
married_total_tax = 0.0     #total tax for married people, used for married average
married_count = 0       #number of inputs of married people, used for married average  



def compute_tax(inc, marr):
    global total_tax, count, married_total_tax, married_count
    #rate 
    if marr:
        if inc > 150000:
            rate = 0.3
        else:
            rate = 0.2
    else:
        if inc > 100000.0:
            rate = 0.2
        else:
            rate = 0.15 
    
    #tax
    tax = rate * inc

    return tax, rate 
    

def submit():
    global total_tax, count, married_total_tax, married_count
    income = float(input('Income >>'))
    #validation: do immediately after the input is read.
    if income <= 0: 
        print(f'You entered {income:.2f}. Please enter a positive value.')
        return      #exit submit, return to the main menu 
    
    married = int(input('1 for Married, 0 if not >>'))

    tax, tax_rate = compute_tax(income, married)
    #update globals
    total_tax += tax
    count += 1
    if married:
        married_total_tax += tax
        married_count += 1
    #outputs 
    # print(income, married)
    print(tax, tax_rate)  #"Tax: {tax:.2f}"


def compute_average_tax():
    global total_tax, count, married_total_tax, married_count

    if count > 0:
        avg = total_tax / count
    else: 
        avg = None
    
    return avg

def compute_md_avg_tax():
    global total_tax, count, married_total_tax, married_count
    
    if married_count > 0:
        avg = married_total_tax / married_count
    else: 
        avg = None
    
    return avg
    


def summary():
    global total_tax, count, married_total_tax, married_count
    
    average_tax = compute_average_tax()
    if average_tax is not None:
        print(f'average_tax: {average_tax:.2f}')
    else:
        print('No data for avg tax')
        
    married_avg_tax = compute_md_avg_tax()
    if married_avg_tax is not None:
        print(married_avg_tax)
    else:
        print('No married taxpayers')


    

def reset():
    global total_tax, count, married_total_tax, married_count
    
    total_tax = 0.0
    count = 0 
    married_total_tax = 0.0
    married_count = 0


#main
quit = False
while not quit:
   print('1.Submit 2.Summary 3.Reset. 4.Exit')
   print('Choose 1,2,3, or 4')
   choice = int(input('>>'))
   if choice == 1:
       submit()
   elif choice == 2:
       summary()
   elif choice == 3:
       reset()
   elif choice == 4:
       quit = True
   else:
       print('Invalid choice! Choose 1,2,3, or 4')
print('Bye!')
