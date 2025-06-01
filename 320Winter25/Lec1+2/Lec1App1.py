"""Lecture 1 App1  Developed by JC 10.01.20.

    This app demonstates printing strings, and documentation(commenting).
    This paragraph could state the inputs, outputs, and describe the computations
    performed.
"""

print('Hello World!')    #print is a 'function' 'Hello World!' is a string 
#every print appends a new line to the end of a output
print("keep your distance") #strings in python allow both single quotes and double quotes 
print('''For your own safety!''')       #triple quotes are primarily for multi-line strings 
#You can also use triple double quotes!
#comments start with a hash, and act as 'documentation'

print('Hello\tWorld!')  #\t is for tab
print() #a print by itself produces a new line 
print('Hello\nWorld!')  #\n is for a new line   \ is an 'escape sequence'


print('Red', end = ',')
print('Green', end = ',')       #use " end = ',' " when you wnat to join things with commas when u run them 
print('Yellow')
print('Those are the three colors')

#DIY    print same output separated by tabs     Red     Green   Yellow

#exit() will exit the terminal or just x out of the terminal by clicking it 
or you can also type clear into the terminal to clear all the old things from the terminal