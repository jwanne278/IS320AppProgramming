"""Exam 1 B     Developed by JC     02.13.25


in: test_score (int), hw_score (int)
out: grade (string), scaled_score (float)


compute_grade function 

"""
#globals
scaled_total_score = 0.0    #used to calculate average score in the summary function
total_count = 0             #used to calculate average score in the summary function
total_count_a = 0           #used to keep track of poeple who got grade A
total_count_b = 0           #used to keep track of poeple who got grade B
total_count_c = 0           #used to keep track of poeple who got grade C

#functions
def compute_grade(scaled_score, hw_total, test_total, test_sco, hw_sco):
    global scaled_total_score, total_count, total_count_a

    scaled_score = (hw_total + test_total) / 100
    
    if scaled_score > 80.0:
        grade = 'A'
        total_count_a += 1
    elif scaled_score > 60.0:
        if test_sco == 50.0:
            grade = 'A'
            total_count_a += 1
        else: 
            grade = 'B'
            total_count_b += 1                      
    else:
        if hw_sco == 50.0:
            grade = 'B'
            total_count_b += 1
        else:
            grade = 'C'
            total_count_c += 1
            
    return grade, scaled_score

def submit():
    global scaled_total_score, total_count, total_count_a
    #inputs
    test_score = int(input('Enter test score >> '))
    if test_score > 50: 
        print(f'You entered {test_score:.2f}. Please enter a value between 0 and 50.')
        return
    hw_score = int(input('Enter hw score >> '))

    #Computations
    homework_total = (hw_score) / 70
    test_total = (test_score) / 50


    #then multiply homework_total by the scaled percetnage which is 60 
    hw_total_scaled = homework_total * 60
    #do the same for test_total by the scaled percetnage which is 40
    test_total_scaled = test_total * 40

    #Add both scaled homework and scaled test scores up 
    grade, scaled_total_score = compute_grade(scaled_total_score, hw_total_scaled, test_total_scaled, test_score, hw_score)
    
    #outputs
    print(f'Your grade is {grade:s}')
    print(f'Your scaled score is: {scaled_total_score:.2f}')

def compute_avg_score():
    global scaled_total_score, total_count, total_count_a
    
    if total_count > 0:
        average_score = scaled_total_score / total_count
    else:
        average_score = None

    return average_score


def summary():
    global scaled_total_score, total_count, total_count_a
    
    average_score = compute_avg_score() 

    if average_score is not None:
        print('Average Score: {average_score:.2f}')
    else:
        print(f'No data for average score')

    
     
def reset():
    global scaled_total_score, total_count, total_count_a

    scaled_total_score = 0.0
    total_count = 0
    total_count_a = 0

    
#main
quit = False
while not quit:
  print('1.Submit 2.Summary 3.Reset. 4.Exit')
  print('Choose 1,2,3 or 4')
  choice = int(input('>>'))
  if choice == 1:
      submit()
  elif choice == 2:
      summary()
  elif choice == 3:
      reset()
      print('Ready for new series..')
  elif choice == 4:
      quit = True
  else:
      print('Invalid choice! Choose 1,2,3 or 4')
print('Bye!')

