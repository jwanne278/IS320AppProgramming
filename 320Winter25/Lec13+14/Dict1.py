"""Dictionary App 1 

"""
student1 = { 'Name':'Alex', 'Score':90, 'Grade':'A'}    #a digest of attributes

#major is IS
student1['Major'] = 'IS'    #Insert: dict[key] = value
name = student1['Name'] #key gets you the value     value = dict[key] 
score = student1['Score']
grade = student1['Grade']
major = student1['Major']
print(name, score, grade, major)
print(student1)
#print(student1)

student2 = {}   #initialize an empty dictionary
name = 'Ben'
score = 70
grade = 'B'
major = 'Accounting'

student2['Name'] = name
student2['Score'] = score
student2['Grade'] = grade
student2['Major'] = major
print(student2)

print(f"{student2['Name']:s}, {student2['Score']:d}, {student2['Grade']:s}, {student2['Major']:s}")     #remember to use the double quote of the single quote doesnt work


students = { 101: 'Alex', 102: 'Ben'}
print(students)
for key in students:
    value = students[key]
    print(key, value)

for sid in students:
    name = students[sid]
    print(sid, name)

all_students = {}   
all_students[101] = student1
all_students[102] = student2
print(all_students)

for sid in all_students:
    student_details = all_students[sid]
    name = student_details['Name']
    score = student_details['Score']
    grade = student_details['Grade']
    major = student_details['Major']
    print(sid, name, score, grade, major)

