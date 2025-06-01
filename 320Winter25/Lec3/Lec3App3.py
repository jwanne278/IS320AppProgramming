""" Home Activity Lecture 3 App 3   Developed by JC     01.15.25

User enters number of books ordered.
Price per book:
10$ 0-10 books (including 10)
9$ 11-100 books
8$ above 100 books
Display order price.

inputs: books_ordered (int)     
outputs: order_price
"""

#Initializations 
#price_book depends on how many books_ordered
#therefore, price_book will have a different equation depending on the amount of books_ordered
#books_ordered (float)

#Inputs 
books_ordered = int(input('How many books did you order?\n>>'))

#Computations
#Once the user enters how many books they ordered, /
#there needs to be a correlary equation. 
#10$ 0-10 books (including 10)
#9$ 11-100 books
#8$ above 100 books
if books_ordered > 100:
    price_book = 8.0

elif books_ordered <= 10:
    price_book = 10.0

else:
    price_book = 9.0

#end if
order_price = books_ordered * price_book

#Output
print(f'The order price for your book(s) is {order_price:.2f}$')