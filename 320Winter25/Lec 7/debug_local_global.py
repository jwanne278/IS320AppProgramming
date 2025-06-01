#we set a breakpoint at the call to print_tax()
#how: click on left gutter, left of line number to activate
#red dot
#we choose Run->Start Debugging instead of the play button
#(Your python version will need to be >= 3.7. Check lower
#right or left corner of VS Code)
#The code will run up until the breakpoint, and wait.
#The line with breakpoint will be the next to execute.
#On the left sidebar, click and expand Globals,
#Click + under Watch and type in tax and hit Return
#(we want to watch the value of the tax variable)
#When debugging, you can also mouse over variable names
#in code to see their current value.
#Top middle, a set of controls will show up.
#The down arrow, Step Into, or F11, is what you use to
# advance the program one line at a time.
#At each click or F11, one line will execute, and code
#will highlight the line that will execute next.
#We will click this, check values on left, click it
#again, keep repeating.
#you can also use the Stop button to end the session.
#As you go through, note in the left sidebar
# how and when the local variables
#become visible and invisible (in and out of scope)
#and how the global remains in scope,
#and when both the global and local tax variables
#are in scope, the code prefers the local tax.


def compute_tax_rate(inc):
    if inc > 100000.0:
        rt = 0.1
    else:
        rt = 0.15
    
    return rt


def print_tax():
    #global tax     (use this if you want to use the global variable for, effectively overriding the local version of tax on line 43)
    income = 200000.0
    tax_rate = compute_tax_rate(income)
    tax = income * tax_rate
    print(tax) #local tax will print


#main
tax = 125.0 #this variable is global
print('hello!')
print_tax()
tax = tax + 10.0
print(tax) #global tax will print
print('Bye!')
