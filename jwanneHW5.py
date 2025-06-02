"""Homework 5       Developed by JC         2.27.25


"""
#globals 
taxpayers = {}  #the global dictionary that is used to reference the taxpayer details dictionary, used for all functions 
tax_id = 1000   #used as a key to reference taxpayer details for each taxpayers, used for all functions  

#functions 
def compute_tax(income,is_married):
    if is_married:
        if income > 100000.0:
            rate = 0.2
        else:
            rate = 0.1
    else:
        if income > 70000:
            rate = 0.15
        else:
            rate = 0.08
    
    tax = income * rate 

    return tax


def process_line(line_in, sep=None): #<--------------- 'overloading'
    global taxpayers, tax_id

    list_in = line_in.split(sep)    #'Adam 1 88'
    name = list_in[0]
    is_married = int(list_in[1])
    income = float(list_in[2])

    
    #validations
    #is_married must be 1 or 0 
    while is_married not in {1,0}:  
        print(f'You entered {is_married:d} for marital status. Please use 1 or 0')
        is_married = int(input('Enter 1 or 0 for marital status >> '))

    #income must be in range 0 to 500000, inclusive.
    while income < 0 or income > 500000:
        print(f'You entered {income:.2f} for income.')
        income = float(input('Please enter an income in the range 0..500k >> '))

    #computations
    #compuite tax function 
    tax = compute_tax(income, is_married)
    
    #initialize a dictionary for the student.
    taxpayer_details = {}
    #insert attributes         
    taxpayer_details['Name'] = name
    taxpayer_details['Income'] = income
    taxpayer_details['Status'] = is_married
    taxpayer_details['Tax'] = tax
 
    #insert taxpayer_details into the glboal dictionary, taxpayers.
    tax_id += 1 
    taxpayers[tax_id] = taxpayer_details


def submit():
    global taxpayers, tax_id
    #inputs
    line_in = input('Enter name, marital status(1/0), and income >> ')
   
    #process the line, to add an entry in the global students.
    process_line(line_in)  #<------------ no input for sep
    
    
    #insert attributes
    taxpayer_details = taxpayers[tax_id]                       #<--------
    name = taxpayer_details['Name']
    is_married = taxpayer_details['Status']
    income = taxpayer_details['Income']
    tax = taxpayer_details['Tax']
    print(f'Name\t:{name:s}\nIncome\t:{income:.2f}\nStatus\t:{is_married:d}\nTax\t:{tax:.2f}')
 
    

def display():
    global taxpayers

    #if the dict is empty, display a message

    if not taxpayers:    #empty check, mandatory 
        print('No data to display')
        return  #exit display function
    
    width = 52
    line = '-' * width 
    print(line)
    print(f'|{"ID":^8s}|{"Name":^10s}|{"Income":^10s}|{"Status":^8s}|{"Tax":^10s}|')
    print(line)
    for taxid in taxpayers:
        taxpayer_details = taxpayers[taxid]
        name = taxpayer_details['Name']
        income = taxpayer_details['Income']
        is_married = taxpayer_details['Status'] 
        tax = taxpayer_details['Tax']
        print(f'|{taxid:<8d}|{name:^10s}|{income:>10.2f}|{is_married:^8d}|{tax:^10.2f}|')     # < left    > right     ^ center 
    print(line)


def search():
    global taxpayers

    if not taxpayers:
        print('No data to search in.')
        return
    
    while True:
        menu = int(input('1 search by id  2 search by status 3 done searching >>'))
        if menu == 1:
            taxid_in = int(input('Enter taxpayer id to search for >> '))
            # found_id = False
            if taxid_in in taxpayers:
                taxpayer_details = taxpayers[taxid_in]
                name = taxpayer_details['Name']
                is_married = taxpayer_details['Status']
                income = taxpayer_details['Income']
                tax = taxpayer_details['Tax']
            
            # for taxpayer_details in taxpayers:
            #     taxid = taxpayer_details['ID']
            #     if taxid == taxid_in:
            #         found_id = True
            #         name = taxpayer_details['Name']
            #         is_married = taxpayer_details['Status']
            #         income = taxpayer_details['Income']
            #         tax = taxpayer_details['Tax']
                    
                width = 52
                line = '-' * width
                print(line)
                print(f'|{"ID":^8s}|{"Name":^10s}|{"Income":^10s}|{"Status":^8s}|{"Tax":^10s}|')
                print(line)
                print(f'|{taxid_in:<8d}|{name:^10s}|{income:>10.2f}|{is_married:^8d}|{tax:^10.2f}|')     # < left    > right     ^ center 
                print(line)
                
                #break
            
            # if not found_id:
            else:
                print(f'Taxpayer with id as {taxid_in:d} not present in our database')

        #taxid search over 
        elif menu == 2:
        #search for marital status 
            is_married_in = int(input('Enter your marital status(1/0) >>'))
            found_status = False
            # for taxpayer_details in taxpayers:
            for taxid in taxpayers:
                # is_married = taxpayer_details['Status']
                taxpayer_details = taxpayers[taxid]
                is_married = taxpayer_details['Status']
                if is_married == is_married_in:
                    found_status = True
                    name = taxpayer_details['Name']
                    income = taxpayer_details['Income']
                    tax = taxpayer_details['Tax']
                    # print(f'ID: {taxid:d}\nName: {name:s}\nIncome: {income:.2f}\nStatus: {is_married:d}\nTax: {tax:.2f}')
                    width = 52
                    line = '-' * width 
                    print(line)
                    print(f'|{"ID":^8s}|{"Name":^10s}|{"Income":^10s}|{"Status":^8s}|{"Tax":^10s}|')
                    print(line)
                    print(f'|{taxid:<8d}|{name:^10s}|{income:>10.2f}|{is_married_in:^8d}|{tax:^10.2f}|')     # < left    > right     ^ center 
                    # print(f'|{taxid:<8d}|{name:^10s}|{income:>10.2f}|{is_married_in:^8d}|{tax:^10.2f}|')
                    print(line)
            
            if not found_status:
                print(f'No taxpayer with marital status {is_married_in:d} in our database')
    
        else:
            return
        #is_married search over 


def compute_averages():
    global taxpayers

    count = 0
    total_tax = 0
    count_u = 0
    count_m = 0
    total_for_m = 0
    
    for taxid in taxpayers:
        taxpayer_details = taxpayers[taxid]
        # name = taxpayer_details['Name']
        is_married = taxpayer_details['Status']
        # income = taxpayer_details['Income']
        tax = taxpayer_details['Tax']

        total_tax += tax
        count += 1
        if is_married == 1:
            count_m += 1 
            total_for_m += tax
        else:
            count_u += 1 
    #end of for loop
    
    if count > 0:
        avg = total_tax / count
        if count_m > 0:
            avg_m = total_for_m / count_m
        else:
            avg_m = None
    else:
        avg = None
        avg_m = None

    return avg, avg_m, count_u
    #end if 


def summary():
    global taxpayers
    #display average tax, average tax for married, count of unmarried taxpayers.

    average_tax, average_for_m, count_u = compute_averages()
    if average_tax is not None:
        print(f'Average tax: {average_tax:.2f}')    
        if average_for_m is not None:
            print(f'Average Tax Married taxpayers: {average_for_m:.2f}')
        else:
            print('No data for average tax of married taxpayers')
    else:
        print('No taxpayers to compute averages with') 
        # print('No data for average tax of married taxpayers')

    print(f'Count U: {count_u:d}') 


def reset():
    global taxpayers

    taxpayers.clear()
    

#main
quit = False
while not quit :
   print('1.Submit 2.Display 3.Search 4.Summary 5.Reset 6.Exit')
   choice = int(input('Enter 1, 2, 3, 4, 5 or 6 >>'))
   if choice == 1:
       submit()
   elif choice == 2:
       display()
   elif choice == 3:
       search()
   elif choice == 4:
       summary()
   elif choice == 5:
       reset()
       print('Ready for a new series of inputs.')
   elif choice == 6:
       quit = True




# print(line)
#             for taxid in taxpayers:
#                 taxpayer_details = taxpayers[taxid]
#                 name = taxpayer_details['Name']
#                 income = taxpayer_details['Income']
#                 is_married = taxpayer_details['Status'] 
#                 tax = taxpayer_details['Tax']
#                 print(f'|{taxid:<8d}|{name:^10s}|{income:>10.2f}|{is_married:^8d}|{tax:^10.2f}|') 



 # if taxid in taxpayers:
        #     taxpayer_details = taxpayers[taxid]
        #     name = taxpayer_details['Name']
        #     is_married = taxpayer_details['Status']
        #     income = taxpayer_details['Income']
        #     tax = taxpayer_details['Tax']
        #     print(f'Name: {name:s}\nIncome: {income:.2f}\nMarital Status: {is_married:d}\nTax: {tax:.2f}')
        # else:
        #     print(f'Taxpayer with id as {taxid:d} not present in our database')
