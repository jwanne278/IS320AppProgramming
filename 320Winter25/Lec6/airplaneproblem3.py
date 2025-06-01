"""Lab 2 Airplane Problem 3     Developed by JC     01.27.25

This app computes the total weekly pay for a salesman.
We know that salesmen earn base_salary $250/ week, just for working so we factor that in to the equation.
Next, we cacluate wheather our salesperson earns comission.
If the saleseperson, did over $1000 in sales, then they would earn 15% of their sales value as long as it is at or above $1000
If sales >= $1000, total_salary = base_salary + commission
If sales < $1000, total_salary = base_salary 
The output of the app shows commission amount and total_salary if sales >= $1000.
But, only shows total_salary if sales < $1000

Inputs: weekly_sales (float)
Outputs: comission (float), total_pay (float)
"""

#Initializations
base_salary = 250.0

#Inputs
weekly_sales = float(input('Enter weekly sales\n>>'))

#Computations
if weekly_sales >= 1000:
    commission = .15 * weekly_sales
else:
    commission = 0.0

total_pay = base_salary + commission

#Outputs
if weekly_sales >= 1000:
    print(f'The total commission amount is {commission:.2f}$')
    print(f'The total pay is {total_pay:.2f}$')
else:
    print(f'The total pay is {total_pay:.2f}$')