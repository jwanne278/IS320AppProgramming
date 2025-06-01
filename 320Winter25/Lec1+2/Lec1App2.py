"""Lecture 1 App2 Developed by JC 01.13.25

This app computes the order price, assuming the number of
books ordered, and the unit price.
Inputs: None
Outputs: Displays order price, number of books ordered and unit price.
"""

#Initializations
unit_price = 1.5    #float
number_books = 10   #int

#Computations
order_price = unit_price * number_books

#Output
#The order price for 10 books at 1.5$ per book, is, 15 dolalrs. 
print(f'The order price for {number_books:d} books at {unit_price:.2f}$ per book, is, {order_price:.2f} dolalrs.')  #f'...'  inside:     {variable:format specifier}     f for float     s for string    d for int 




#int    integer     no decimal point
#float  floating point number   decimal point and digits after
#str    string
# bool  logical types True or False.

# '=' is assignment operator.
#assigns the value on the right to the variable on the left. 
# name your variables informatively
# unit_price    dont do 1price, but price1 is okay  


""" STEPS DONE ON PYTHON INTERPRETER IN TERMINAL
>>> 10+2
12
>>> 4.5+1.5
6.0
>>> type(4)
<class 'int'>
>>> type(4.5)
<class 'float'>
>>> type('Hello')
<class 'str'>
>>> type('h')
<class 'str'>
>>> type(true)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> yes
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'yes' is not defined
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> x=10
>>> x
10
>>> y=20
>>> x+y
30
>>> x/y
0.5
>>> product = x * y 
>>> product 
200
>>> color = 'Red'
>>> color
'Red' 
"""