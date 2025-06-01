"""Homework 1 Question 1: App Calorie Calculator   Developed by JC 01.14.25

Q1: Your program calculates the calorie content of a food item,
based on the user specifying the amount (by weight, in grams) of protein,
carb and fat in the food item. Prompt the user to enter the weight of each
of the above, one by one. Compute calorie content using this rule: Each
gram of fat is nine calories, and each gram of protein or carb is four 
calories. Display protein (grams), carb (grams), fat (grams), total 
calories.

input: protein_weight (float)   carb_weight (float)     fat_weight (float)  
output: calorie content (protein, carbs, fat)
"""

#initializations
protein_weight = 4
carb_weight = 4
fat_weight = 9

#inputs
food_item = input('What food item are you logging today? \n>>')
protein_grams = float(input('How many grams of protein are in the/ food item? \n>>'))
carb_grams = float(input('How many grams of carbs are in the food item? \n>>'))
fat_grams = float(input('How many grams of fat are in the food item? \n>>'))

#computations
calorie_protein = protein_grams * protein_weight
calorie_carb = carb_grams * carb_weight
calorie_fat = fat_grams * fat_weight
total_calories = calorie_protein + calorie_carb + calorie_fat

#outputs
print(f'Hello,\nThe total amount of calories in your {food_item:s} is {total_calories:.2f}\nThe amount of protein calories in your {food_item:s} is {calorie_protein:.2f}\nThe amount of carb calories in your {food_item:s} is {calorie_carb:.2f}\nThe amount of fat calories in your {food_item:s} is {calorie_fat:.2f}')
# print(f'')

# print(f'The amount of carb calories in your {food_item:s} is {calorie_carb:.2f}')
# print(f'The amount of fat calories in your {food_item:s} is {calorie_fat:.2f}')