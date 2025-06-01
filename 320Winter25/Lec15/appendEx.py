numbers = [10,40,60]
x = 77
numbers.append(x)   #add new numbers to a dictionary

count = 0
sum = 0

for number in numbers:
    count += 1 
    sum += number 
    print(number)

avg = sum / count
print(count, avg)
#empty check: if not numbers: 
#emptying out: numbers.clear()

