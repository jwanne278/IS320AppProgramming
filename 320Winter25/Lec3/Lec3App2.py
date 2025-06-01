"""Lec3App2.py  Developed by JC     01.14.25.

User enters score (integer in range 0..100)
letter grade A,B or C is computed and displayed.
80-100 A    >=80
60-79 B    >= 60    
0-59 C
input: score :int
output: letter_grade : stre     (other languages have 'char' for character)
"""

score = int(input('Enter score (0...100) >>'))

if score >=80:   #score > 79
    letter_grade = 'A'
elif score >= 60:   # we know the score < 80        else if becoems 'elif'
    letter_grade = 'B'
else:    #we know the score < 60
    letter_grade = 'C'


print(score, letter_grade)  #make this print infomrative, and formatted
#int    d
#str    s
#float  f


# see an error like 'Invalid Syntax?'
#look in your terminal. Is there a >>>?
#type exit()    at the >>> and hit Enter or clear. 
