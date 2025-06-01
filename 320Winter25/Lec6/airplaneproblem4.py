"""Lab 2 Airplane Problem 4     Developed by JC     01.27.25

This app calculates the scaled calculated score and delivers a grade for a student that is taking a class.
A student inputs thier name, homework, and test scores, and then it ouputs a letter grade and number score.
By adding up the two homework scores you get a score out of 100.
By adding up the two test scores, you get a score out of 60. 
You are then left with a percentage for homeworks, which you scale by multiplying by 60.
You are also left with a percentage for tests, which you scale by multiplying by 40.
At this point, you add the two values together to get your scaled total score.
Your score is finally evaluated by >90 = 'A'
>=80 = 'B'
>=60 = 'C'
any other score is 'D'

inputs: name (string), hw1 (float), hw2 (float), test1 (float), test2 (float)
outputs: name (string), hw1 (float), hw2 (float), test1 (float), test2 (float), scaled_total_score (float), grade (string)
"""

#Initializations

#Inputs
name = input('What is your name?\n>>')
hw1 = float(input('What was your score on homework 1?\n>>'))
hw2 = float(input('What was your score on homework 2?\n>>'))
test1 = float(input('What was your score on test 1?\n>>'))
test2 = float(input('What was your score on test 2?\n>>'))

#Computations
#The goal is to figure out how to convert the individual scores of the homeworks and the tests to come up with scaled grading system
#since homeworks are out of 50 points, we could add the scores of both to get x/100 for example 
#that wold give us a percentage, then we multiply by 60 to scale it properly 
#We have to make homeworks be worth 60% and tests have to be worth 40%
homework_score = (hw1 + hw2)/100
scaled_hw_score = homework_score * 60
#We do the same process, but for tests (tests are out of 30 each so test_score will be out of x/60)
test_score = (test1 + test2)/60
scaled_test_score = test_score * 40 
#we also have to determine letter grade according to the tiered systems lsited in the prompt, once we have a scaled_total_score
scaled_total_score = scaled_hw_score + scaled_test_score

if scaled_total_score > 90.0:
    grade = 'A'
elif scaled_total_score >= 80.0:
    grade = 'B'
elif scaled_total_score >= 60.0:
    grade = 'C'
else:
    grade = 'D'

#I need one more if statement that says if they get a 'B' and one of there test scores were a perfect 30/30 to change the grade to an 'A'
if grade == 'B':
    if test1 == 30.0:
        grade = 'A'
    elif test2 == 30.0:
        grade = 'A'




#Ouputs
print(f'Name:   {name:s}')
print(f'')
print(f'Homework 1:     {hw1:.2f}/50')
print(f'Homework 2:     {hw2:.2f}/50')
print(f'')
print(f'Test 1: {test1:.2f}/30')
print(f'Test 2: {test2:.2f}/30')
print(f'')
print(f'Scaled Total Score:     {scaled_total_score:.2f}/100')
print(f'')
print(f'Grade:  {grade:s}')