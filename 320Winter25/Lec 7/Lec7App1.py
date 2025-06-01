"""Lecture 7 App 1.  Illustrating local and global variables.

Uses dummy functions to illustrate visibility (scope) of variables.
"""
#globals #which variables need to visible across multiple functions #usually totals, total amount, total revenue, discount 
x = 10
y = 121

#functions
def function1():
    global y  #re-declaration, adding it to memory
    x = 100
    print('in function 1: x = ', x)
    y = 1
    print('in function 1: y = ', y)
    
    
def function2():
    global x
    x = x + 1
    print('in function 2: x = ', x)
    y = 100
    print('in function 2: y = ', y)

    #return None
    

#main
print('in main: x = ', x)
function1()
function2()
print('in main: x = ', x)
# print('in main: y = ', y)
function2()
function2()
function2()


#global variables can be modified 
#local variables can only be modified by the variables in the function 