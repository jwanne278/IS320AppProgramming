"""Homework 4 Question 1    Developed by JC     02.06.25

This application collects two inputs, score and wheather the grading system is pass/fail or grade basis.
On a grade basis, score >= 80 is an A, while score < 80 is a B.
On a pass/fail basis, score >= 40 is a pass, whereas <40 is a fail.
Next the counts of As, Bs, passes, or fails need to be updated depending on the grade that the score received. 
The total number of inputs need to be updateed as well. 
Then the user prints the score and the grade to end the submit function.
For the summary function, it displays the total number of inputs, the counts of all the grades, and both average scores for the pass.fail basis and the grade basis respectively.
There are two seperate functions to calcualte the average score, one for the grade basis and one for pass/fail.
The reset function clears exsisting values in the event that the user wants to clear all stored data.
The main is written in a way where the user decides wheather they want to submit another score input, get a summary for average score, reset all values, or exit the program 

inputs: score (int), grade_basis (int)
outputs: 
    submit: grade (string), score (int)
    summary: num_imputs (int), count_a (int), count_b (int), count_p (int), count_f (int), average_scoreg (float), average_scorepf (float)
"""
#globals 
total_scoreg = 0 #the total scores on a grade basis, for average score calculation 
total_scorepf = 0 #the total scores on a pass/fail basis, for average score calculation
count_a = 0 #the number of As there were, used for summary function 
count_b = 0 #the number of Bs there were, used for summary function
count_p = 0 #the number of passes there were, used for summary function
count_f = 0 #the number of fails there were, used for summary function

#functions
def compute_grade(sco):
    if sco >= 80:
        grade = 'A'
    else:
        grade = 'B'
    
    return grade

def compute_grade_pf(sco):
    if sco >= 40:
        grade = 'Pass'
    else:
        grade = 'Fail'
        
    return grade 


def submit():
    global total_scoreg, total_scorepf, count_a, count_b, count_p, count_f
    #inputs 
    score = int(input('Enter score\n>>'))
    is_grade_basis = int(input('Enter 1 for grade basis, 0 for pass/fail\n>>'))
    
    #computations
    #1 if grade basis:
        #compute grade based on grade basis system
    # else:
        #compute grade based on pass/fail
    if is_grade_basis:  #same as is_grade_basis == 1 
        grade = compute_grade(score)
        total_scoreg += score
    else:
        grade = compute_grade_pf(score)
        total_scorepf += score
    #2 calculate the average score, which happens in summary 
    
    #3 update the number of inputs 
    if grade == 'A':
        count_a += 1 
    elif grade == 'B':
        count_b += 1 
    elif grade == 'Pass':
        count_p += 1
    else:
        count_f += 1 


    


    #output
    print(f'Score: {score:d}')
    print(f'Grade: {grade:s}')
#end submit 


def compute_average_scoreg():
    global total_scoreg, total_scorepf, count_a, count_b, count_p, count_f
    
    num_inputsg = count_a + count_b
    if num_inputsg > 0:
        avg = total_scoreg / num_inputsg
    else:
        avg = None    
    
    return avg

def compute_average_scorepf():
    global total_scoreg, total_scorepf, count_a, count_b, count_p, count_f
 
    num_inputspf = count_p + count_f
    if num_inputspf > 0:
        avg = total_scorepf / num_inputspf
    else:
        avg = None

    return avg

def summary():
    global total_scoreg, total_scorepf, count_a, count_b, count_p, count_f
    
    average_scoreg = compute_average_scoreg()

    average_scorepf = compute_average_scorepf()

    num_inputs = count_a + count_b + count_p + count_f

    if average_scoreg is not None:
        print(f'Average Score is {average_scoreg:.2f}')
    else:
        print(f'No data for average score.')

    if average_scorepf is not None:
        print(f'Average Score is {average_scorepf:.2f}')
    else:
        print(f'No data for average score.')

    print(f'Number of As: {count_a:d}')
    print(f'Number of Bs: {count_b:d}')
    print(f'Number of Pass: {count_p:d}')
    print(f'Number of Fail: {count_f:d}')
    print(f'Number of inputs: {num_inputs:d}')


def reset():
    global total_scoreg, total_scorepf, num_inputs, num_inputsg, num_inputspf, count_a, count_b, count_p, count_f

    total_scoreg = 0 
    total_scorepf = 0 
    # num_inputs = 0 
    # num_inputsg = 0 
    # num_inputspf = 0 
    # count_a = 0 
    # count_b = 0 
    # count_p = 0 
    # count_f = 0 


#main
quit = False
while not quit: #quit == False: #infinite loop with an exit #repeated 'if' is 'while' 
    print('1.Submit 2.Summary 3.Reset 4.Exit')
    print('Enter 1,2,3, or 4 >>')
    choice = int(input('Choice >>'))
    if choice == 1: 
        submit()
    elif choice == 2:
        summary()
    elif choice == 3:
        reset()
        print('Ready for a new batch...')
    elif choice == 4:
        quit = True 
    else:
        print('Invalid choice!')

print('Goodbye!')




#main
# summary()
# submit()
# submit()
# submit()
# summary()