"""Homework 4 Question 2      Developed by JC   02.07.25

This application computes the amount of tax that poeple have to pay.
Your maritial status, income, and number of exepmtions, will determine how much money you get subtracted from your taxable income.
It will also determine how much tax you ultimately have to pay. 
Income --> marital status --> number of exemptions --> taxable income --> tax rate --> tax 

inputs: is_married (int), income (float), num_exemptions (int)
output: tax(float)

"""
#globals
married_taxpayers = 0   #used to keep track of married tax_payers in higher tax_bracket for the summary function
single_taxpayers = 0    #used to keep track of single tax_payers in higher tax_bracket for the summary function 
total_tax = 0.0         #used to keep track of total tax, used to compute average tax in the sumamry functiin 
inputs_m = 0            #total married taxpayers, used to calculate num_inputs for the sumamry function  
inputs_s = 0            #total single taxpayers, used to calculate num_inputs for the sumamry function 

#functions
#1
def compute_taxable_income(inc,exemptions,married):
      global married_taxpayers, single_taxpayers, total_tax, inputs_m, inputs_s 

      if married:
            inputs_m += 1
            exemption_rate = 500.0
            inc = inc - (exemptions * exemption_rate) 
      else:
            inputs_s += 1
            exemption_rate = 375.0
            inc = inc - (exemptions * exemption_rate)

      return inc 

#2
def compute_tax_rate(taxab, married):
      global married_taxpayers, single_taxpayers, total_tax, inputs_m, inputs_s 

      if married:
            if taxab > 150000.0:
                  married_taxpayers += 1 
                  rate = 0.3
            else:
                  rate = 0.2
      else:
            if taxab > 100000.0:
                  single_taxpayers += 1
                  rate = 0.18
            else:
                  rate = 0.15
      
      return rate 


def submit():
      global married_taxpayers, single_taxpayers, total_tax, inputs_m, inputs_s
      #inputs 
      is_married = int(input('If you are married enter 1, single enter 0\n>>'))
      income = float(input('Enter income\n>>'))
      num_exemptions = int(input(f'How many exemptions are you claiming?\n>>'))

      #computations
      #1 Take the income and subtract out the exemptions to find taxable income.
      # take the number of exeptions 
      taxable_income = compute_taxable_income(income, num_exemptions, is_married)
      #2 Based on the taxable income, the program determines what the tax rate will be.
      #function
      tax_rate = compute_tax_rate(taxable_income, is_married)
      
      #3 Find the amount of tax by multiplying the remaining taxable income after exemptions by tax rate.
      tax = taxable_income * tax_rate 
      total_tax += tax
      #4 find the number of single and married tax payers in higher tax bracket 
 

      #outputs
      # if is_married:
      #       inputs_m += 1 
      #       print(f'Married')
      # else:
      #       inputs_s += 1  
      #       print(f'Single')

      # print(f'Income: {income:.2f}')
      # print(f'{num_exemptions:d} exemptions')
      print(f'Tax is {tax:.2f}')


def compute_average_tax(): 
      global married_taxpayers, single_taxpayers, total_tax, inputs_m, inputs_s
      
      num_inputs = inputs_m + inputs_s
      if num_inputs > 0:
            avg = total_tax / num_inputs
      else:
            avg = None
      
      return avg 

def summary():
      global married_taxpayers, single_taxpayers, total_tax, inputs_m, inputs_s

      average_tax = compute_average_tax()

      if average_tax is not None:
          print(f'Average Tax is {average_tax:.2f}')
      else: 
          print(f'No data for Average Tax')

      print(f'Married Taxpayers in higher tax bracket: {inputs_m:d}')
      print(f'Single Taxpayers in higher tax bracket: {inputs_s:d}')

def reset():
      global married_taxpayers, single_taxpayers, total_tax, inputs_m, inputs_s

      married_taxpayers = 0   
      single_taxpayers = 0     
      total_tax = 0.0          
      inputs_m = 0              
      inputs_s = 0            


#main
quit = False
while not quit: #quit == False: #infinite loop with an exit #repeated 'if' is 'while' 
    print('1.Submit 2.Summary 3.Reset 4.Exit')
    print('Enter 1,2,3, or 4 >>')
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