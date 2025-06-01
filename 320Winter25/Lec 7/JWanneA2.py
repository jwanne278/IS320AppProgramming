"""A2   Develooped by JC     01.28.25

User enters the input:   weight in pounds 

Your program finds the shipping rate -  orders with weights at or above 10 pounds are charged at 20 cents per pound; otherwise, the order is charged at 15 cents per pound.  (These are flat rates that apply for the entire weight, there is no addition involved).

And then your program uses the rate found to compute the shipping cost, based on the weight.

Each calculation (finding the shipping rate, and computing the shipping cost) should be implemented using functions. (so, two functions required)

Your main program reads user input, calls each function one after the other, and then prints the shipping cost.

Documentation:  your name at the top is sufficient.   

Suppose there is a second input - express or standard shipping (let us say that is supplied as 1 for express and 0 for standard).  This affects the shipping rate calculation(Don't worry about how).   What change will be required in the function call for shipping rate, and what change will be required in the def line (the header) for the shipping rate function?  (Write your brief response as a comment in your code; a few words is sufficient.  Ignore what changes need to happen inside the if statement for shipping rate)

(Keep your function definitions separate from the main (i.e. do not place def.. lines within the main).  And do not define one function inside another.)

inputs: weight (float)
output: shipping_cost (float)

"""

#functions
#If there was an express vs. standard option...
#For the same reason, the function definition line would have to be changed so that 'if' statments now indicate wheather express or stnadard shipping is used. 
#The new 'if' statement will now choose rate based on two arguments: standard vs express (0 or 1) and weight
def find_shipping_rate(wt):     
    if wt >= 10.0:
        rate = 0.2
    else:
        rate = 0.15

    return rate 


def compute_shipping_cost(wt,rate):
    shipping_cost = wt * rate

    return shipping_cost
    

#main
#input
weight = float(input('Enter weight'))

#computations
#1 find shipping rate   out: shipping_rate (float)  in: weight (float)
shipping_rate = find_shipping_rate(weight)

#If there was a express and a standard option...
#The function call would have to include anohter input within the parenthesis, perhaps it would look like "shipping_rate = find_shipping_rate(weight, express_charge)"

#2 compute the shipping cost    out: shipping_cost (float)  in: weight, shipping_rate (float)
shipping_cost = compute_shipping_cost(weight, shipping_rate)

#Output
print(f'Weight of the order is {weight:.2f}')
print(f'Shipping Cost is {shipping_cost:.2f}')