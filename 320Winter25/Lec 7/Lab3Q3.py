"""Lab 3 Problem 3    Developed by JC     01.29.25

This app computes the number of points a user has after reading a certain amount of books.
There is a teired system to denote how many points each book read gets.
If user reads <= 3 books, that equates to 10 points/book.
If user reads <= 6 books, the first 3 books are worth 10 points each, and the rest are 15 points each. 
If user reads > 7 books, the first 3 books are worth 10 points each, the next 3 are worth 15 points each, then every other book is worth 20 points each. 
With these denotations, we can obtain the number of points.
Lastly, we output the member name and the number of points. 

inputs: name (str), num_books (int)
output: name (str), points (float)
"""

#functions 
def compute_points(books):
    if books <= 3:
        points = books * 10
    elif books <= 6:
        points = (3 * 10) + (books - 3) * 15
    else:
        points = (3 * 10) + (6 * 15) + (books - 6) * 20

    return points 

#main 
#inputs
name = input('Member Name >> ')
num_books = int(input('How many books did you read? >> '))

#calculations
#we need to figure out how many points someone gets for reading x amount of books 
#there is a teired point system based on amount of books read 
#out: points (float)     in: num_books
points = compute_points(num_books)

#output
print(f'{name:s} has earned {points:.2f} points')