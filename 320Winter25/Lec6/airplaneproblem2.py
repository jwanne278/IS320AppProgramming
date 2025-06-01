"""Lab 2 Airplane Problem 2     Developed by JC     01.27.25

Problem 2
Do this problem last, both because it follows a different pattern, and because it has one or two minor challenges.
Prompt the user and read two integers, one by one. Let us say they are a and b. Your program generates the following output: 
(one of these statements)
 a is a factor of b.   (when b % a equals zero, a is a factor of b)
 b is a factor of a.
 Neither is a factor of the other.
Test with 30, 300 and then 300, 30 and then 301, 30 to get the three outputs.
Now test with 300,300. Modify your if statement to add the output statement ‘each is a factor of the other’ and test again.
Now test with 300, 0. Modify your if statement so that if either input is zero, the output states: ‘Invalid Input’.

In the problem above, you don’t need to worry about separation of computations and outputs. You also don’t need to worry about documenting the ‘outputs’ in detail in the documentation header at the top in this program. The primary intention here is to practice the if statements and the check for factors.  

Input: number_a (float), number_b (float)
Outputs:
For inputs 30, 300:   a is a factor of b
For inputs 300, 30:   b is a factor of a
For inputs 300,300:   each is a factor of the other
For inputs 301, 30:   neither is a factor of the other
For inputs 300, 0:    Invalid input
For inputs 0, 300:    Invalid input
"""

#Initializations

#Inputs
number_a = float(input('Type in a number\n>>'))
number_b = float(input('Type in another number\n>>'))
number_c = float(input('Type in a third number\n>>'))
number_d = float(input('Type in a fourth number\n>>'))

#Computations
#1. Take the two numbers and 2 must calcualtions must be done: (a % b) and (b % a)
factor = number_b % number_a #300, 30
factor2 = number_a % number_b #30, 300
factor3 = number_a % number_a #30, 30
factor4 = number_a % number_c #30, 301
factor5 = number_d % number_b #0,300
factor6 = number_b % number_d #300, 0

if factor == True:
    factor = number_b % number_a
    factor = 0.0 
elif factor2 == True:
    factor2 = number_a % number_b
    factor2 = 0.0
elif factor3 == True:
    factor3 = number_a % number_a
    factor3 = 0.0



#2. if either of these are a factor of each other, none, or both, or its invalid, use an if statement to state just that

#3.  Output is almost exactly as stated in the prompt in a string that says something like "a is a factor of b"

#Outputs

print(f'For inputs {number_a:.2f}, {number_b:.2f}:   a is a factor of b')