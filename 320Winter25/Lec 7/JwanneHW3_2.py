""" Homework 3 Question 2   Developed by JC     01.30.25

Problem 4
 An application that uses the number of hours worked in a week by an employee to compute and display the gross pay, the taxes and the net pay. Net pay is gross pay less taxes. 
There is a single input, hours, and three outputs: gross pay , tax and net pay. The hours input may be treated as integer or as float.

Use the following rules:

Basic pay rate = 10$ per hour
Overtime rate (overtime is defined as hours in excess of 40 hours) = 1.25 times the regular hourly rate
Tax rate  : 15% of the first 200$
          	20% of the next 200$
          	25% of the rest
             (this is a tiered rate system, with tax computed as the sum of components, the formula changing for each tier). It is best to do the tax calculation within the if statement here, as the calculations are different for the three branches of the if.

testing: Use enough inputs to check for overtime, as well as each individual tax tier.

#Test data
#These are just showing the values; they are not formatted.
#hours -> gross tax net
#20 -> 200 30 170
#30 -> 300 50 250
#40 -> 400 70 330
#50 -> 525 101.25 423.75

comments:
The comments below are in response to questions anticipated. Information above is sufficient to complete this app; please read comments below before contacting me with questions.

Hint: Before you do any coding, solve the problem by hand. For this, first use the input value 50 and calculate the gross pay including overtime, and the total tax for it. You should write down each component of tax separately. Repeat for more inputs. Then look through the calculations you wrote down, and think how you can represent that logic in a program, so that it will work for ANY input.

Hint 2: If you are not able to figure out the logic for the if statement: First, write a working program for the input 20 (hours worked). Then, figure out what needs to be added to that code, or what changes need to be done, to make it give you the right result for 40. Repeat for 50. By then, you would have the complete program. And in writing these programs, pay attention to the fact that you need to figure out gross pay correctly, and then figure out the correct tax, which is a sum of different parts.

What the lines in bold above imply :
The problem can be divided into two steps:  compute the gross pay,  and compute the tax.  The first needs hours, and the second needs gross pay, as input.  There is no need for the computations to overlap.
The tax is a ‘sum of different parts’:  Unlike previous tax problems, there is no simple tax computation formula here.  Under each tier, the tax computation is different.   So,  there is no need to try to separate Finding Rate, and Computing Tax.  Under each possibility of the if statement, compute the corresponding tax directly.

  When you do the tax computation, it would be  good to have the if statement reflect the tax rule as closely as possible. (so that a casual reader can infer the tax rule by reading your if statement, and does not have to reverse-engineer your code to figure out the tax rule. This guideline applies to the gross pay computation as well. It would be best to have the if statement clearly reflect the rule used for computing gross pay)

 In this problem, your variable choices can lead to different kinds of code:
Minimal number of variables, with some of them being reused, but leading to additional steps, and less readability
Using variables for every numeric value, tending towards less readability and clutter
Using a mix of variables and numbers
The best approach here is to write out the computations in a way that a third party can read your code and directly see the rules for gross pay and tax computation, without having to revisit the problem description or reverse engineering.

If you use numbers directly in your code, do note that  300 * 0.15 is more readable than just typing in 45, leaving the reader to wonder where that number came from.



Documentation
This app computes the net_pay per week based on the amount of hours worked per week.
The input is the hours_worked.
The hours_worked will determines the pay rate, which affects gross pay.
If you work <= 40 hours you get paid $10/ hour.
If you work > 40 hours you get paid $12.5/ hour.
After you are given gross_pay, a function is created to select the corresponding tax_rate.
If your gross_pay is <= $200, then multiply corresponding tax_rate of 0.15 by gross_pay.
If your gross_pay is <= $400, then multiply corresponding tax_rate of 0.2 by gross_pay.
If your gross_pay is > $400, then multiply corresponding tax_rate of 0.25 by gross_pay.
The answer gives you tax.
Third step in computation section states to get net_pay, take gross_pay less taxes.
Outputs are gross pay, tax, and net pay.


inputs: hours_worked (int), 
output: gross_pay (float), tax (float), net_pay (float)
"""

#functions 
def compute_tax(pay):
    if pay <= 200.0:
        rate = 0.15
        tax = rate * pay
    elif pay <= 400.0:
        rate = 0.2
        tax = (0.15 * 200.0) + (pay - 200.0) * 0.20
    else:
        rate = 0.25
        tax = (0.15 * 200.0) + (200.0 * 0.2) + (pay - 400.0) * 0.25
    
    return tax 


#main
#initializations 
basic_pay_rate = 10.0   #per hour
overtime_pay_rate = 12.5 #per hour

#inputs 
hours_worked = int(input(f'How many hours did you work?\n>>'))

#computations
#1 first, we find gross pay, but we must include the fact that poeple earn overtime pay_rate if they exceed 40 hours 
if hours_worked <= 40:
    gross_pay = hours_worked * basic_pay_rate  #per hour 
else:
    gross_pay = hours_worked * overtime_pay_rate

#2 solve tax using the tax bracket
#out: tax   in: gross_pay (float)
tax = compute_tax(gross_pay)

#3 net pay 
net_pay = gross_pay - tax

#output
print(f'Gross pay is {gross_pay:.2f}')
print(f'Tax is {tax:.2f}')
print(f'Net pay is {net_pay:.2f}')