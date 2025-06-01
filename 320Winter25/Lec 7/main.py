"""New:    1. A faster way to do functions

             2. New uses for functions -  Organize code,  Reuse Code, Improve Efficiency 
            (converting globals to locals improved both efficiency and security)

             3. Global variables. (all our variables  from before become local variables, and we bring in new global variables)

 

Specification:  User enters income.  Tax rate is 10% at or below 100,000 dollars, 15% otherwise.

Use two functions, one for tax rate and the other for tax, and display tax.

Extended Spec:  Modify the program to support multiple inputs, and compute the average tax across this 
series of inputs.
average tax = total tax / number of inputs
total_tax (float)
num_inputs (int)
"""
#globals
total_tax = 0.0     # sum of tax values to calculate average tax with 
num_inputs = 0  #count inputs, to calcuate average tax with 

#functions
def compute_tax_rate(inc):
    if inc <= 100000.0:
        rate = 0.1
    else:
        rate = 0.15

    return rate


def compute_tax(inc, rate):
    tax = inc * rate

    return tax

def submit():
    global total_tax, num_inputs
    
    income = float(input('Enter income >> '))
    #computations 
    #1 find the tax rate    out:tax_rate (float)    in: income (float)
    tax_rate = compute_tax_rate(income)
    #2 compute the tax    out: tax    in: income, tax_rate (float)
    tax = compute_tax(income, tax_rate)
    #3 update totals
    total_tax += tax
    num_inputs += 1

    #output
    print(f'Income: {income:.2f}')
    print(f'Tax: {tax:.2f}')
    print(total_tax, num_inputs)


#main
submit()
submit()
submit()





# did not type a return statement?
#your function will return 'None'


#Local variable - defined inside a function
 
#the main cant see the variables in the functions 
#think about as if the variables wt, inc are in a black box, u cant see whats inside the black box
#its scope is limited 
#the variable is used for the function and then deletes right after 
#if code runs again, it will be used, and then delete again
# the variables do not remember their values from previous runs of the function.


#Global variable - defined outside of all functions 

# globally visible. every function can 'see' them, modify them as well.
# an input is an example
# think of them a standing out in a yard or a billboard, 
#for everyone to see.

#Criteria for globals:
#1 does the variable need to REMEMBER its value after the function is over? 
#2 does the variable nneed to be seen by multiple functions?