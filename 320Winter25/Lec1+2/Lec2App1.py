"""Lec2App1.py by JC. 01.14.23.

User enter name, income.
User also enters age and number of people living in the same house.
App computes and display tax, at the rate 15%, and age.
inputs: (entered by the user)  name (str)   income (float)  age (int)   people (int)
outputs: (displayed to the user) tax (float)
"""
#initializations
tax_rate = 0.15

#inputs
name = input('Enter your name \n>>')
income = float(input('Enter your income \n>>'))
number_people = int(input('How many people live in your household? \n>>'))
age = int(input('And how old are you? \n>>'))

#computations
tax = income * tax_rate

#outputs
print(f'Hello {name:s}, your income was {income:.2f} dollars,')
print(f'and you are {age:d} years old,')
print(f'and you have {number_people:d} people lving in the same house,')
print(f'and you owe {tax:.2f} dollars in taxes.')




#Notes
#A program development sequence
#How do I represent my information? (data)
#Variables: (and their types)
#   inputs:
#   outputs:
#   anything else: tax_rate
#2 Solve the problem 
#3 code it. verify it. debug it. (avoid typos)
#4 document it 

#numeric types:
#integer    5      0   -10
#real numbers float    5.5  5.0  .2999
#does question specify int?
#if not, does the item in question imply it will NEVER have a fraction?
# do not base your type choices based on sample data given 

# output to be informative.
# output to be formatted.


#format specifiers  str 's'   float 'f', but always do .xf (count decimals you want),     int 'd'

#f''    strong.format(.....)    % formattting 
# not acceptable    print(tax, income)  print(str(tax))

#input/output   from/to terminal/console    always in the form of strings. 

#NameError means the variable does not exsist 
#TypeError means you have to change the type of a variable, likely from 'int' to 'float'



# income_str = input('Enter your income \n>>')    #'1000' --> 1000.0  str -> float
# income = float(income_str)   # this is a conversion, only used for inputs 
# income = float(input('Income'))

# y = log(x)
# q = sin(y)

# q = sin(log(x))






"""
Hello <...>, your income was <...> dollars,
and you owe <...> dollars in taxes 
"""

