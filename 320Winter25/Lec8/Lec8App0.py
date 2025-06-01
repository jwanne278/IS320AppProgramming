"""Lec 8 App 0
NEW:
    1. Mandatory zero division check in compute_average_tax.
    2. Matching if statement in summary, and error message.
    3. reset() function to get ready for a new series of data.
    Steps 1 and 2 above are required in all future submissions, and zero division
protection is required for all division operations.

in: income
out: tax at 10%.




submit: output: tax (float)
summary: outputs: average tax (float)
"""

#globals
total_tax = 0.0 #sum of tax amount, for average computation
count_inputs = 0 #number of inputs, for average computaitons 


#functions


def submit():
    global total_tax, count_inputs
    #inputs
    income = float(input('Enter your income>>'))

    #computations 
    #A. pricess current input(s)
    tax_rate = 0.1
    tax = income * tax_rate
    
    #B. update globals
    #update total_tax by adding the new value of tax t the old valie of total_tax
    total_tax = total_tax + tax    #choose your preferred style (total_tax += tax)
    #update count_inputs by adding 1 to it.
    count_inputs += 1
    
    #outputs 
    print(income)
    print(tax)
#end submit


def compute_average_tax():  #do not send in globals as parameters to a function 
    global total_tax, count_inputs
    #The zero division check below is manadatory for every submission, for every division 
    if count_inputs > 0:
        avg = total_tax / count_inputs
    else:
        avg =  None     #using None her is mandatory as well

    return avg
    #do not print anything within this function


def summary():
    global total_tax, count_inputs
    
    average_tax = compute_average_tax()
    #summary must have a second if statement as below
    if average_tax is not None:
        print(average_tax)
    else:
        print('No data for computing average tax.')

    print(count_inputs)     #this can be inside or outside the if 
#main
summary()
submit()    #count 0-->1
submit()    #count 1-->2    => count has to remember 
#its value => GLOBAL
submit()
summary()



#NOTES
#average tax: total / count
#a computation => a function
#variables for total_tax and count_inpputs - float / int
#global?
#critera for making a variable global:
# do we need to extend its visibility? (extend beyond what?)
# do we need to extend its lifetime?
#you always get both advantages: the global will remember its value, and be visible 
#to all functions 

#Global
#0. apply criteria to decide which variables are global. => keep globals to the minimum
#1. initialize them at the top, flushed left, signify type when initializing (eg 0.0)
#2. add a comment after each, explaining its purpose
#3. add a global line at the start of each function. 
#       -this is a 're-declaration'
#       -you need this line only in fucntions that *modify* the globals.
#       best practice: add the line to all functions that *use* the globals.
#       easy and recommended: just add it to every function  

#None - lack of a value, nothing.
#has its own type - NoneType
#Maps to NULL in databases

#if x == None Incorrect     you say:    if x is None  Correct 
#if x != None is replaced by: if x is not None
#this mirrors SQL: if id is null    / if id is not null

#lines below are for use later:

#print('1.Submit 2.Summary 3.Reset')
#choice = int('Enter 1,2,or 3 >>')
#if choice == 1:
