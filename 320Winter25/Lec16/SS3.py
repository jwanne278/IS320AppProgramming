"""Self Study 3: Task 1        Developed by JC      3.12.24

This program inputs name, income, and marriage status.
It validates that the income > 0 and a number. 
It validates that the marriage status is either or or 0 and is an integer.
Then, it prints both income and marriage status. 
"""

#TASK
def is_valid_income(income):
  return income >= 0 
  

def is_valid_marriage(marriage_status):
  return 0 <= marriage_status <= 1 



while True:
    try:
      input_list = input('Enter name, income, and marriage status(1/0)>> ').split()
      assert len(input_list) == 3
      name = input_list[0]
      income = input_list[1]
      marriage_status = input_list[2]
    
      while True:
          try:
              income = float(income)
              assert is_valid_income(income)
              print(income)
              break
          except AssertionError:
              print('Income must be above 0')
              income = float(input('Enter income above 0 >>'))
       
     

      while True:
          try: 
              marriage_status = int(marriage_status)
              assert is_valid_marriage(marriage_status) 
              print(marriage_status)
              break
          except ValueError:
              print('marriage status must be an integer!')
              marriage_status = int(input('Enter marriage status (whole number 0 or 1) >>'))
          except AssertionError:
              print('marriage status must be either 1 or 0!')
              marriage_status = int(input('Enter marriage status (whole number 0 or 1) >>'))
      break
    
    except AssertionError:
        print('You must type three inputs')