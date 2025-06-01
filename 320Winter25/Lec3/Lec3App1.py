"""Lec3App1.py developed by JC 01.14.25

Q1: user enters income. app displays tax.
tax rate is 10% if the income is less than 100,000.
20% otherwise.
input: income: float 
outcome: tax: float 

Q2: user enters weight(in pounds). app displays shipping cost.
ship rate is 10 cents per lb for weights at or below 10 pounds,
15 cents per pound otherwise.
input: weight (float)
output: cost_ship (float)
"""

# #Q1
# #inputs
# income = float(input('Enter income >'))

# #computations
# #1 Find tax rate out: tax_rate (float) in: income (float)
# if income < 100000.0:           #If= 'if'   #Then= 'else'
#     tax_rate = 0.1
# else: 
#     tax_rate = 0.2

# #end if

# #2 compute the tax out: tax (float) in: income, tax_rate (float)
# tax= income * tax_rate
# #outputs
# print(f'Income: {income:.2f}')
# print(f'Tax: {tax:.2f}')

#CTRL -/ or CMMD-/ will comment out a block of lines 

#structured programming

#Q2
weight = float(input('Enter weight/n>>'))

#1 find shipping rate out: ship_rate in: weight (float)
if weight <= 10.0:  #a 'condition' True or False boolean
    ship_rate = 0.1
else:
    ship_rate = 0.15

#end if 

#2 compute shipping cost out: cost_ship in: weight, ship_rate (float)
cost_ship = weight * ship_rate

print(f'Weight/t:{weight:.1f}')
print(f'Shipping Cost/t:{cost_ship:.2f}')


#Conditions are boolean expressions.

# < >
#<. >=
#is the score equal to 100?
# if score == 100
# == 'double equals'    /'equals equals'
#!=     not equals
#the ! usually means negate what follows

#score = 100  #assignment  
#if score == 100:   a question