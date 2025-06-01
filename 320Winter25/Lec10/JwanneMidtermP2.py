"""Midterm B Redo      Developed by JC   02.13.25

Your program is computing taxes and average taxes using the main above.   
Variables such as being married, amount of income, and child credits determine amount of tax.


inputs: is_married (int), income (float), count_child_credits (int)
output: tax(float)
"""

#globals
married_taxpayers = 0   #used to keep track of married tax_payers in higher tax_bracket for the summary function
single_taxpayers = 0    #used to keep track of single tax_payers in higher tax_bracket for the summary function 
total_tax = 0.0         #used to keep track of total tax, used to compute average tax in the sumamry functiin 
inputs_m = 0            #total married taxpayers, used to calculate num_inputs for the sumamry function  
inputs_s = 0            #total single taxpayers, used to calculate num_inputs for the sumamry function 
total_tax_s = 0.0       #total tax of single taxpayers, used to cacluate average tax, just for single taxpayers for the summary 

#functions
def compute_tax(married, inc):
      global married_taxpayers, single_taxpayers, total_tax, inputs_m, inputs_s, total_tax_s

      if married:
            inputs_m += 1
            if inc >= 50000.0: 
                  tax_rate = 0.1 
            else:
                 tax_rate = 0.08  
      else:
            inputs_s += 1 
            if inc > 70000.0:
                 tax_rate = 0.07
            else:
                 tax_rate = 0.05
                  
            total_tax_s += inc * tax_rate
      
      tax = tax_rate * inc
      tax_rate = tax_rate * 100
      
      return tax, tax_rate, total_tax_s 


def compute_child_credit(married, credits):
      global married_taxpayers, single_taxpayers, total_tax, inputs_m, inputs_s, total_tax_s
      if married:
            tax_credit = 1500.0
            amount = credits * tax_credit
      else:
            tax_credit = 2000.0
            amount = credits * tax_credit
            total_tax_s -= amount  

      return amount, total_tax_s


def submit():
      global married_taxpayers, single_taxpayers, total_tax, inputs_m, inputs_s, total_tax_s
      #inputs 
      income = float(input('Enter income >'))
      is_married = int(input('If you are married enter 1, single enter 0 >'))
      if is_married != 0:
            if is_married != 1:
                 print(f'You entered a value {is_married}. Please enter a value of either 0 or 1.')
                 
                 return 
                
      
      count_child_credits = int(input(f'Number of child credits claimed >'))

      #computations
      #1
      tax, tax_rate, total_tax_s = compute_tax(is_married, income)
      
      #2
      child_credit_amount, total_tax_s = compute_child_credit(is_married, count_child_credits)
      
      #3
      tax -= child_credit_amount
      if tax < 0.0:
           tax = 0.0
      
      #4 
      total_tax += tax 
      
      #outputs
      print(f'Tax:\t\t{tax:.2f}')
      print(f'Tax Rate:\t{tax_rate:.2f}')
      print(f'Child Credit:\t{child_credit_amount:.2f}')


def compute_average_tax(): 
      global married_taxpayers, single_taxpayers, total_tax, inputs_m, inputs_s, total_tax_s
      
      num_inputs = inputs_m + inputs_s
      if num_inputs > 0:
            avg = total_tax / num_inputs
      else:
            avg = None
      
      if inputs_s > 0:
           average_tax_s = total_tax_s / inputs_s
      else:
           average_tax_s = None


      return avg, average_tax_s


def summary():
      global married_taxpayers, single_taxpayers, total_tax, inputs_m, inputs_s, total_tax_s

      average_tax, average_tax_s = compute_average_tax()

      if average_tax is not None:
          print(f'Average Tax is {average_tax:.2f}')
      else: 
          print(f'No data for Average Tax')


      if average_tax_s is not None:
           print(f'Average Tax for Unmarried {average_tax_s:.2f}')
      else:
           print(f'No data for Average Tax of Unmarried Taxpayers')

      print(f'Married Taxpayer Count: {inputs_m:d}')


def reset():
      global married_taxpayers, single_taxpayers, total_tax, inputs_m, inputs_s, total_tax_s

      married_taxpayers = 0   
      single_taxpayers = 0     
      total_tax = 0.0          
      inputs_m = 0              
      inputs_s = 0 
      total_tax_s = 0.0           


#main
quit = False
while not quit: #quit == False: #infinite loop with an exit #repeated 'if' is 'while' 
    print('1.Submit 2.Summary 3.Reset 4.Exit')
    print('Enter 1,2,3, or 4')
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