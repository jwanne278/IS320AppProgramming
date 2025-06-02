"""jwanneHW6.py       Developed by JC         2.27.25

This app is used to compute tax. 
Users can determine their tax bracket and tax amount 
by inputting factors like name, marriage status, and income. 
Details of each taxpayer are updated into a global dictionary, which 
is updated into a list containing all details of all taxpayers.

"""
#globals 
taxpayers = []  #the global list that is used to reference the taxpayer details dictionary, used for all functions 
tax_id = 10000   #used as a global key to reference taxpayer details for each taxpayer, used for all functions 
taxpayer_details = {}   #the global dictionary that is used to reference specific attributes about a specific taxpayer, associateed with an tax_id key 

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
    
    #initialize a dictionary for the taxpayer.
    taxpayer_details = {}
    #insert attributes         
    tax_id += 1 
    taxpayer_details['ID'] = tax_id
    taxpayer_details['Name'] = name
    taxpayer_details['Income'] = income
    taxpayer_details['Status'] = is_married
    if is_married == 1:
        status_string = 'Married'  
    else:
        status_string = 'Unmarried'
    taxpayer_details['Status'] = status_string
    taxpayer_details['Tax'] = tax
 
    #append taxpayer_details into the global list, taxpayers.
    taxpayers.append(taxpayer_details)

    return taxpayer_details


def submit():
    global taxpayers, tax_id, taxpayer_details
    #inputs
    line_in = input('Enter name, marital status(1/0), and income >> ')
   
    #process the line, to add an entry in the global students.
    taxpayer_details = process_line(line_in)  #<------------ no input for sep
   
    taxid = taxpayer_details['ID']                       #<--------
    name = taxpayer_details['Name']
    status_string = taxpayer_details['Status']
    income = taxpayer_details['Income']
    tax = taxpayer_details['Tax']

    print(f'ID\t:{taxid:d}\nName\t:{name:s}\nIncome\t:{income:.2f}\nStatus\t:{status_string:s}\nTax\t:{tax:.2f}')
 

def load():
    global taxpayers, taxpayer_details
    """read data from a text file with comma separated values:
    name,status(1/0),income. fill taxpayers list with matching data.
    """
    #1. prepare a text file, preferably in vs code. Adam,1,80
    #2. open the file for reading,
    #3. for each line in the file:
    #4 process the line.
#vs code: settings: search for Execute in File Dir. Ensure the box is checked.
#vs code: file: open new text file. save as: inputs.txt (choose any name.)
    count = 0
    with open('hw6inputs.txt', 'r') as loadfile:
        for line in loadfile:
            process_line(line, ',')
            count += 1 
    #fix this
    print(f'{count:d} taxpayers loaded from inputs.txt') #>------------update to: e.g 4 students loaded.


def display():
    global taxpayers

    #if the dict is empty, display a message

    if not taxpayers:    #empty check, mandatory 
        print('No data to display')
        return  #exit display function
    
    width = 54
    line = '-' * width 
    print(line)
    print(f'|{"ID":^5s}|{"Name":^10s}|{"Status":^13s}|{"Income":^10s}|{"Tax":^10s}|')
    print(line)
    for taxpayer_details in taxpayers:
        taxid = taxpayer_details['ID']
        name = taxpayer_details['Name']
        status_string = taxpayer_details['Status'] 
        income = taxpayer_details['Income']
        tax = taxpayer_details['Tax']
        print(f'|{taxid:^5d}|{name:<10s}|{status_string:^13s}|{income:>10.2f}|{tax:>10.2f}|')     # < left    > right     ^ center 
    print(line)


def save():
    """save the contents of the global list to a comma seperated text file.
    each line: 1001,Adam,100,A """
    global taxpayers
    if not taxpayers: #empty check, mandatory
        print('No data to save.')
        return #exit display function
    #initialize an empty master string
    #for each dictionary in the list:
    # get matching taxpayer details,
    # get attributes from the details dictionary (name etc)
    # compose a line (a string) combining the attributes,
    # append the line to the master string
    # after the loop,
    #open a text file for writing,
    # and write the master string to it.
    count = 0
    savefilename = 'hw6outputs.txt' #<--- can ask user to enter file name
    out_data = '' #the string that will be written to the file.
    for taxpayer_details in taxpayers: #for each dictionary in the global list #<---------
        taxid = taxpayer_details['ID']
        name = taxpayer_details['Name']
        income = taxpayer_details['Income']
        status_string = taxpayer_details['Status'] 
        tax = taxpayer_details['Tax']
        line_out = f'{taxid:d},{name:s},{income:.2f},{status_string:s},{tax:.2f}'
        out_data += line_out + '\n'
        count += 1
    #end loop
    with open(savefilename, 'w') as savefile:
        savefile.write(out_data.rstrip('\n')) 
    print(f'{count:d} taxpayers saved to hw6outputs.txt') # include a message like, 5 students saved to outputs.txt
    #implement a count as in averages function, to get the number of students saved


def search():
    global taxpayers, taxpayer_details

    if not taxpayers:
        print('No data to search in.')
        return
    
    while True:
        menu = int(input('1 search by id  2 search by name 3 done searching >>'))
        if menu == 1:
            taxid_in = int(input('Enter taxpayer id to search for >> '))
            found_taxid = False
            for taxpayer_details in taxpayers:
                taxid = taxpayer_details['ID']
                if taxid == taxid_in:
                    found_taxid = True
                    name = taxpayer_details['Name']
                    status_string = taxpayer_details['Status']
                    income = taxpayer_details['Income']
                    tax = taxpayer_details['Tax']
                    
                    width = 54
                    line = '-' * width
                    print(line)
                    print(f'|{"ID":^5s}|{"Name":^10s}|{"Status":^13s}|{"Income":^10s}|{"Tax":^10s}|')
                    print(line)
                    print(f'|{taxid:^5d}|{name:<10s}|{status_string:^13s}|{income:>10.2f}|{tax:>10.2f}|')     # < left    > right     ^ center 
                    print(line)
                
                #break
            if not found_taxid:
                print(f'Taxpayer with ID as {taxid_in:d} not present in our database')

        #taxid search over 
        elif menu == 2:
        #search for marital status 
            name_in = (input('Enter your name >> '))
            found_name = False
            # for taxpayer_details in taxpayers:
            for taxpayer_details in taxpayers:
                name = taxpayer_details['Name']
                if name == name_in:
                    found_name = True
                    taxid = taxpayer_details['ID']
                    income = taxpayer_details['Income']
                    status_string = taxpayer_details['Status']
                    tax = taxpayer_details['Tax']
                    # print(f'ID: {taxid:d}\nName: {name:s}\nIncome: {income:.2f}\nStatus: {is_married:d}\nTax: {tax:.2f}')
                    width = 54
                    line = '-' * width 
                    print(line)
                    print(f'|{"ID":^5s}|{"Name":^10s}|{"Status":^13s}|{"Income":^10s}|{"Tax":^10s}|')
                    print(line)
                    print(f'|{taxid:^5d}|{name:<10s}|{status_string:^13s}|{income:>10.2f}|{tax:>10.2f}|')     # < left    > right     ^ center 
                    # print(f'|{taxid:<8d}|{name:^10s}|{income:>10.2f}|{is_married_in:^8d}|{tax:^10.2f}|')
                    print(line)
            
            if not found_name:
                print(f'No taxpayer with name {name_in:s} in our database')
    
        else:
            return
        #is_married search over 


def compute_averages():
    global taxpayers, taxpayer_details

    count = 0
    total_tax = 0
    count_mlower = 0
    count_m = 0
    total_for_m = 0
    
    for taxpayer_details in taxpayers:
        status_string = taxpayer_details['Status']
        income = taxpayer_details['Income']
        tax = taxpayer_details['Tax']

        total_tax += tax
        count += 1
        if status_string == 'Married':
            count_m += 1 
            total_for_m += tax
            if income <= 100000.0:
                count_mlower += 1
        
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

    return avg, avg_m, count_mlower
    #end if 


def summary():
    global taxpayers, taxpayer_details
    #display average tax, average tax for married, count of married taxpayers in lower tax bracket.

    average_tax, average_for_m, count_mlower = compute_averages()
    if average_tax is not None:
        print(f'Average tax: {average_tax:.2f}')    
        if average_for_m is not None:
            print(f'Average Tax Married taxpayers: {average_for_m:.2f}')
        else:
            print('No data for average tax of married taxpayers')
    else:
        print('No taxpayers to compute averages with') 
        # print('No data for average tax of married taxpayers')

    print(f'Number of married taxpayers in the lower tier: {count_mlower:d}') 


def reset():
    global taxpayers

    taxpayers.clear()
    print(f'Ready for new data')

    

#main
functions = {
   1:submit,
   2:load,
   3:display,
   4:save,
   5:search,
   6:summary,
   7:reset,
}


while True :
   print('1.Submit 2.Load 3.Display 4.Save 5.Search 6.Summary 7.Reset 8.Exit')
   choice = int(input('Enter 1, 2, 3, 4, 5, 6, 7 or 8 >>'))
   if choice == 8:
       break
   if choice < 1 or choice > 8:
       print('Invalid choice!')
       continue
   functions[choice]()




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
