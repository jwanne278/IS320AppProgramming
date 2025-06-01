"""Homework 2 Question 2    Developed by JC     01.22.24

This app determines students Scaled Total Score and grade. 
The user enters the name, two test scores (each out of 30), and two homework scores (each out of 50). 
A scaled total score out of 100 is produced by the app, which assigns 60% of the total score to the homework and 40% to the test. 
The scaled score determines the grade: 
A gives you a 90.
B if your score is in between 80 and 90 (rewarding you with an upgrade to A if you score a 30 on one of your tests).
C for scores between 60 and 79.
D if you score under 60. 
The app produces an output that includes name, scores, Scaled Total Score, and grade.

inputs: name (str), hw1 (float), hw2 (float), test1 (float), test2 (float) 
outputs: name (str), hw1 (float), hw2 (float), test1 (float), test2 (float), scaled_total_score (float), grade (string)
"""

#Inputs
name = input('What is your name? >>')
hw1 = float(input('What is your homework 1 score out of 50? >>'))
hw2 = float(input('What is your homework 2 score out of 50? >>'))
test1= float(input('What is your test 1 score out of 30? >>'))
test2 = float(input('What is you test 2 score out of 30? >>'))

#Computations
#first we combine the total of the homework scores, then divide by 100 to find the unscaled score for homework
homework_total = (hw1 + hw2)/100

#next, we combine the total of the test scores, then divide by 60 to fiund the unsacaled score for tests 
test_total = (test1 + test2)/60

#then multiply homework_total by the scaled percetnage which is 60 
homework_total_scaled = homework_total * 60
#do the same for test_total by the scaled percetnage which is 40
test_total_scaled = test_total * 40

#Add both scaled homework and scaled test scores up 
scaled_total_score = homework_total_scaled + test_total_scaled



if scaled_total_score > 90.0:
    grade = 'A'
elif scaled_total_score >= 80.0:
    grade = 'B'
elif scaled_total_score >= 60.0:
    grade = 'C'
else:
    grade = 'D'

# For anyone who gets a B, if either of the test scores is 30, the grade changes to A. (Hint: avoid trying to use and to combine conditions here)
if grade == 'B':
    if test1 == 30.0:
        grade = 'A'
    elif test2 == 30.0:
        grade = 'A'


#Outputs
print(f'Name:\t{name:s}')
print(f'')
print(f'Homework 1:\t{hw1:.2f}/50')
print(f'Homework 2:\t{hw2:.2f}/50')
print(f'')
print(f'Test 1:     {test1:.2f}/30')
print(f'Test 2:     {test2:.2f}/30')
print(f'')
print(f'Scaled Total Score:\t{scaled_total_score:.2f}/100')
print(f'')
print(f'Grade:\t{grade:s}')