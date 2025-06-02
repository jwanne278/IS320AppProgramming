oopexample.py

class Pet:
    pet_count = 0
    def __init__(self,species,name):    #the 'constructor'
        self.species = species
        self.name = name

        Pet.pet_count += 1

    #end init

    def __str__(self):
        return f'''
        Hello, I am {self.name:s}, a {self.species:s}.
        '''
    #end str

    def __repr__(self):     #supports print. customize to change print always returns string 
        return self.name
    #end repr    ---> optional function

    def display(self):
        return f'|{self.name:<10s}|{self.species:^10s}|'
    #end display
    def speak(self):
        if self.species == 'Dog':
            return 'BowWow'
        if self.species == 'Cat':
            return 'Meow'
    #end speak

    #class method
    @classmethod
    def display_count(cls):
        return f'The number of pets is: {cls.pet_count:d}'
    

#end class

#main
#---1----
pet1 = Pet('Dog', 'Tiger')  #make an object (a pet)
pet2 = Pet('Cat', 'Princess')   #a 'constructor' - function that makes the object 

print('What is the type of pet1 variable?')
print(type(pet1))

print('What is the type of a number 10.5, and a string "Blue">')
print(type(10.5))
print(type('Blue'))
print()
print('When you add a class, you are adding your own type to the language.')
print('The variable is said to be an object, defined by the class.')

print('In python types are classes')
print('and all variables are objects.')

print()

#end 1-----

#---2

print('printing each pet, with simple print, which uses __str__')
print(pet1)    #__str__
print(pet2)
print(1000)

"""

print('printing pet1, explicitly using __str__')
print(pet1.__str__())

print('printing pet1, using str(pet1)')
print(str(pet1))

print('All three use the same method, __str__()')
"""
#----end 2


#-----3
"""
print('Now we store the pet objects in a list')
pets = []
pets.append(pet1)
pets.append(pet2)

print('printing entire list of pets, using repr')
print(pets)   #repr
"""



#-----4
"""
print('Display all pets, using default __str__')
print('Using for pet in pets:')
for pet in pets:
    print(pet)
print()
print('Display all pets, using custom display function')
print('Using for pet in pets:')
for pet in pets:
    print(pet.display())
print()
"""

#----5
"""
print('Making all pets speak, using speak()')
for pet in pets:
    print(pet.speak())
print()
"""

#----6
"""
print('The count, from class variable pet count')
print(Pet.pet_count)
print()
print('The count, using class method display_count ')
print(Pet.display_count())
"""


'''
terminology:
init - constructor, 'constructs' an object
class - blueprint to make objects, like types.
a pet is of type Pet.
a pet is an object of Pet class.

in python, types (int, float..) are classes
And a class you add, is like a type you add.
Pet is a new type of your own.
pet1 is a variable of that type.

pet1 variable contains attributes - name, species
and methods - speak, display, init, str

method - a function inside a class.
rule - must have self as first parameter.

every pet has a name, and a species.
every pet gets a copy of all the methods.

pet_count belongs to the class Pet.
every pet does not get a pet_count.

self.name  - name belongs to self.   
self -> this object

Pet.pet_count   pet_count belongs to the class, not to each pet object.

__init__   the __xx__ notation indicates it is a built-in method.
by defining it, you are customizing the built-in method.

principles we follow
- we are not printing or doing inputs from within the class
- the list holding the pets is outside the class
- all computations and variables related to the class will be inside class.
'''

    
