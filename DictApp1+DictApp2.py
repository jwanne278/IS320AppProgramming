"""Lect13DictionaryApp1 + Lec 14 DictApp2 + Lec15App0

This program is a full-featured student record system that allows users to input, search, display, 
and persist student data (name, score, grade) using a global dictionary, with support for file I/O, 
grading logic, summaries, and robust user validation.

NEW:    submit:     inputs read as a single line
        search:     empty check, search by id, including checking if the id is present
        summary:    single avg function, running for loop, no new globals
        display:    captions/titles, id
        submit:     validations
        search:     search by name (non-key attribute)


Dictionaries - Template for full app. Lecture after Midterm.
submit: user inputs: name(str) score(int)
outputs: id(int), name(str), score(int), grade(str)
grade A for > 80 else B
summary: average score, and count of A grades
display: shows all students (id,name,score,grade), nicely presented
search: displays student details for the id entered by user

reset: gets ready for a new series of inputs. does not reset id.

Recommended: include comments like below in your documentaion 
data: stored as a global dictionary - students 
key: student id starting at 1001
value: a dictionary of attributes name, score, grade, student_details
{
1001: {'Name': 'Alex', 'Score':90, 'Grade': 'A'},
1002: {'Name': 'Ben', 'Score':80, 'Grade': 'B'},
}
insert:     students[s_id] = student_details
retreive:   student_details = students[sid]
student_details example {'Name': 'Alex', 'Score':90, 'Grade':'A'}

"""
#globals
students = {}   #a global dictionary
s_id = 1000     #

#functions
def compute_grade(score):
    grade = 'A' if score > 80 else 'B'

    return grade

def process_line(line_in, sep):
    global students, s_id

    list_in = line_in.split(sep)
    name = list_in[0]
    is_graded = int(list_in[1])
    score = int(list_in[2])
    
    
    #validations
    #is_graded must be 1 or 0 
    while is_graded not in {1,0}:  # [1,0] (1,0) {1,0}     a 'set'
        print(f'You entered {is_graded:d} for grade status. Please use 1 or 0')
        is_graded = int(input('Enter 1 or 0 for grade status >> '))

    #score must be in range 0 to 100, inclusive.
    while score < 0 or score > 100:
        print(f'You entered {score:d} for score.')
        score = int(input('Please enter a score in the range 0..100>> '))

    #computations
    grade = compute_grade(score)
    #initialize a dictionary for the student.
    student_details = {}
    #insert attributes
    student_details['Name'] = name
    student_details['Score'] = score
    student_details['Grade'] = grade 

    #insert student_details into the glboal dictionary, students.
    s_id += 1 
    students[s_id] = student_details

    
def submit():
    global students, s_id 

    #inputs
    # name = input('Name?')
    # score = int(input('Score? '))
    line_in = input('Enter name, graded(1/0) and score >> ')
    
    #process the line, to add an entry in the global students.
    process_line(line_in, ',')
    

    #outputs: suggested: make a function to do the steps below 
    student_details = students[s_id]
    name = student_details['Name']
    score = student_details['Score']
    grade = student_details['Grade']
    print(s_id, name, score, grade)  #DIY print nicely


def load():
    """read data from a text file with comma separated values: name, graded(1/0), score.
    fill students dictionary with matching data.
    """

    #1. prepare a text file, preferably in vs code. Adam,1,80
    #2. open the file for reading,
    #3. for each line in the file: 
    #4.     process the line.
#vs code: settings: search for Execute in File Dir
#vs code: file:open new text file. save as: inputs.txt (choose any name.)
    with open('inputs.txt', 'r') as loadfile:
        #super interesting.
        for line in loadfile:
            process_line(line, ',')


def save():
    """save the contnets of the global dictionary to a comma seperated text file.
    each line: 1001,Adam,1,100,A
    """
    global students
    #initialize an empty master string 
    #for each key in the dictionary:
    #   get matching student details,
    #   get attributes from the  details dictionary (name etc)
    #   compose a line (a string) combining the attributes,
    #   append the line to the master string
    # after the loop,
    #open a text file for writing,
    # and write the master string to it. 

    out_data = ''   #the string that will be written to the file. 
    for sid in students:
        student_details = students[sid]
        name = student_details['Name']
        score = student_details['Score']
        grade = student_details['Grade']
        line_out = f'{sid:d},{name:s},{score:d},{grade:s}'
        out_data += line_out + '\n'
    #end loop
    # print(out_data)
    with open('outputs.txt', 'w') as savefile:
        savefile.write(out_data.rstrip('\n'))


def display():
    global students
    #if the dict is empty, display a message

    if not students:    #empty check, mandatory 
        print('No data to display')
        return  #exit display function

    # print(students)
    width = 37
    line = '-' * width 
    print(line)
    print(f'|{"ID":^8s}|{"Name":^10s}|{"Score":^7s}|{"Grade":^7s}|')
    print(line)
    for sid in students:
        student_details = students[sid]
        name = student_details['Name']
        score = student_details['Score']
        grade = student_details['Grade'] 
        print(f'|{sid:<8d}|{name:^10s}|{score:>7d}|{grade:^7s}|')     # < left    > right     ^ center 
    print(line)
    
# for a float you could do something like >10.2f for 10 spaces wide, right justify, 2 digits after 
#|    12.50|

#strings - left justified by default 
#numbers - right jsutified by default 
def search():
    global students 

    if not students:    #empty check, mandatory 
        print('No data to search in.')
        return  #exit display function

    #offer the user a menu, to choose search by id, or by name.

    sid = int(input('Enter student id to search for >>'))
    #before you to retreive info matching a key, verify the key is present
    if sid in students:
        student_details = students[sid]
        name = student_details['Name']
        score = student_details['Score']
        grade = student_details['Grade']
        print(sid, name, score, grade)  #DIY print nicely
    else:
        print(f'No student with id {sid:d} in our database')

    #sid search over 

    uname = input('Enter name to search for >>')
    found = False
    for sid in students:
        student_details = students[sid]
        name = student_details['Name']
        if name == uname:
            found = True
            score = student_details['Score']
            grade = student_details['Grade']
            print(sid, name, score, grade)  #DIY print nicely
    #end for loop: we have looked at all the students.
    if not found:
        print(f'No student with name {uname:s}.')



def compute_averages():
    global students

    count = 0
    total_score = 0
    count_A = 0
    total_for_A = 0
    
    for sid in students:
         
        student_details = students[sid]
        # name = student_details['Name']    #comment out the code from the dictionary that is unused for the summary 
        score = student_details['Score']
        grade = student_details['Grade']

        total_score += score
        count += 1
        if grade == 'A':
            count_A += 1 
            total_for_A += score
    #end of for loop
    
    if count > 0:
        avg = total_score / count
        if count_A > 0:
            avg_A = total_for_A / count_A
        else:
            avg_A = None
    else:
        avg = None
        avg_A = None
    #end if 

    return avg, avg_A, count_A

def summary():
    global students
    #display average score, average for A, count of A grades.

    average_score, average_for_A, count_A = compute_averages()
    if average_score is not None:
        print(f'Average score: {average_score:.2f}')    #format, text
        if average_for_A is not None:
            print(f'Average Score "A": {average_for_A:.2f}')
        else:
            print('No data for average score of A')
    else:
        print('No data for average')
        print('No data for average score of A')

    print(f'Count A: {count_A:d}') #format, text 


def reset():
    global students

    students.clear()    #dont forget the parenthesis!
    #note: do not use students = {}    to reset the dictionary.    must use .clear()


#main
#easier verfsion of writing a main 
functions = {
    1: submit,
    2: load,
    3: save,
    4: display,
    5: search,
    6: summary,
    7: reset,

}

# quit = False
# while not quit:
while True:
    print('1.Submit 2.Load 3.Save 4.Display 5.Search 6.Summary 7.Reset 8.Exit')
    choice = int(input('Enter 1, 2, 3, 4, 5, 7 or 8 >>'))
    if choice < 1 or choice > 8:
        print('Invalid choice!')
        continue    #exit the current iteration, continue with the loop from start
    elif choice == 8:
        # quit = True
        break   #exit the loop

    functions[choice]()
    
    
    # if choice == 1:
    #     submit()
    # elif choice == 2:
    #     display()
    # elif choice == 3:
    #     search()
    # elif choice == 4:
    #     summary()
    # elif choice == 5:
    #     reset()
    #     print('Ready for a new series of inputs.')
    # elif choice == 6:
    #     quit = True


"""
Strings, and Things, if empty, are False.

0 is false
{} is False
[] is False
'' is False
None is False

"""
