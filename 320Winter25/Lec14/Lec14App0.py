"""Lecture 14 Application 0
breif look at lists


"""
#list identifying a poisition
numbers = [20, 88, 90, 100]
print(numbers)
for number in numbers:
    print(number)

#indexing starts at 0
#indexing by itself is identifying a key from a list '2'
print(numbers[2])
print(numbers[0])

sentence = 'the cat sat in a hat'
words = sentence.split()
print(words)

#find the 4th word
print(words[3])
print(words[0])

line_in = input('Enter name and score >> ')
print(line_in)  # 'Adam 100'
list_in = line_in.split()
print(list_in)
name = list_in[0]
score = int(list_in[1])

print(name, score)
