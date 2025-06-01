"""Task 1: Self Study Functions     Devloped by JC      01.28.25

"""

#1
def sum_series(first,last, number_of_elements):
  sum = (first + last) / 2 * number_of_elements #count of numbers in the series
  
  return sum
#for example: The series 5,6,7 has first = 5, last = 7, number_of_elements = 3
#and the sum is then: 12 / 2 * 3 = 18

#I want to find the sum of numbers 1,2,....98,99,100.  The function above has the correct computation for it.
#Make the code below work, so that I get 5050 as result displayed
#

my_sum = sum_series(1,100,100)
print(my_sum)


#2
def compute_square(num):
  area = num * num   #'pass' is used to make an empty function
  
  return area 
  #replace it with code to make the function call below work.


my_square = compute_square(10)
print(my_square)


#3
#define your function here
def compute_product(num1, num2):
  product = num1 * num2

  return product


my_product = compute_product(7,3)
print(my_product)



#4
#tax rate is 10% for income below 100,000, and
#15% otherwise.
#define your function here to make the call below work.
def compute_tax_rate(income):
  if income < 100000:
    tax_rate = 0.10
  else:
    tax_rate = 0.15

  return tax_rate

income = float(input('Enter income >>'))
tax_rate = compute_tax_rate(income)
tax = income * tax_rate
print(tax)


#5
#letter grade is A for score above 70, B otherwise.
#assume score will always be
#in the range 0..100
#define your function here.
def find_grade(score):
  if score >70:
    grade = 'A'
  else:
    grade = 'B'

  return grade


score = int(input('Enter your score >>'))
#add your function call here so that the print below works.
grade = find_grade(score)
print(grade)


#6
#user enters: prot_gms, carb_gms, fat_gms display: total calories.
#protein - 4 cal per gm
#carbs - 4 cal per gm
#fat - 9 cal per gm
def compute_calories(prot_gms, carb_gms, fat_gms):
  total_calories = prot_gms * 4 + carb_gms * 4 + fat_gms * 9

  return total_calories

total_calories= compute_calories(10,10,10)
print(total_calories)

#write a function to compute calories. Takes three weights as inputs, output is the total calories.
#write code to read the three inputs, call the function, and to display the total calories.


#7 Bonus Problem 
#In this problem, you choose which functions to make, and call them.

#Each book costs 15$.
#Each order is taxed at 7%.
#For 0-10 books ordered, shipping is charged at 10 cents per book.
#11-20 books, 15 cents per book.
#beyond that, 20 cents per book.
#shipping cost is the selected shipping rate * number of books
#example 15 books: shipping cost is 15 * 0.15 $.

#your printed results should include:
#order price, tax, shipping rate, shipping cost, billed amount.

#define functions here
#1
def compute_order_price(num_books):
  order_price = num_books * 15

  return order_price

#2
def compute_tax(order_price):
  tax = order_price * 0.07

  return tax

#3
def compute_shipping_rate(num_books):
  if num_books <= 10:
    shipping_rate = 0.10
  elif num_books <= 20:
    shipping_rate = 0.15
  else:
    shipping_rate = 0.20

  return shipping_rate
  
#4
def compute_shipping_cost(num_books):
  if num_books <= 10:
    shipping_cost = num_books * 0.10
  elif num_books <= 20:
    shipping_cost = num_books * 0.15
  else:
    shipping_cost = num_books * 0.20

  return shipping_cost

#Inputs
books = int(input('Enter number of books ordered\n>>'))

#Output
billed_amount = compute_order_price(books) + compute_tax(books) + compute_shipping_cost(books)

#call your functions here, one after the other
#1
order_price = compute_order_price(books)

#2
tax = compute_tax(order_price)

#3
shipping_rate = compute_shipping_rate(books)
#4
shipping_cost = compute_shipping_cost(books)


#print your results here
#1
print(f'Order Price is {order_price:.2f}')

#2
print(f'Tax is {tax:.2f}')

#3
print(f'Shipping Rate is {shipping_rate:.2f}')

#4
print(f'Shipping Cost is {shipping_cost:.2f}')

#5
print(f'Billed Amount is {billed_amount:.2f}')