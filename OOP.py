# Object Oriented Programming (OOP)

print(type(None)) # <class 'NoneType'>
print(type(True)) # <class 'bool'>
print(type(5)) # <class 'int'>
print(type(5.5)) # <class 'float'>
print(type("Hi")) # <class 'str'>
print(type([])) # <class 'list'>
print(type(())) # <class 'tuple'>
print(type({})) # <class 'dict'>

# Everything is an Object in Python because everything is based on the class keyword
# We can use different methods on our objects we can access with .method
# OOP is a way for us to structure our code that easier to maintain and write
# With OOP, we can break up our code into small pieces
# These small pieces or objects can be used in other code
# Can create our own classes using the class keyword with camel case instead

# private variables - just add an underscore
# Example - _name = "Myname"
# An underscore means do not touch it or modify this variation
# The double underscore have special meaning and means do not touch or modify this

class BigObject: # class
    pass
obj1 = BigObject()  # instanciate creating a new object

print(type(obj1))

class PlayerCharacter:
    membership = True # Class Object Attribute. Same for all objects
    def __init__(self, name="anomymous", age=0):  # Usually see this at the top when creating a class
        if (age > 18):
            self.name = name  # self refers to player1 or what is left of the dot
            self.age = age

    def shout(self):
        print(f"My name is {self.name}")

    # decorator - Don't need to instanciate the class
    # can instanciate in the return still if you want
    @classmethod
    def adding_things(cls, num1, num2): # standard is to use cls
        return cls("Teddy", num1 + num2)

    @staticmethod # Do not have access to cls
    def adding_things2(num1, num2):
        return num1 + num2

player1 = PlayerCharacter("Cindy", 44)
player2 = PlayerCharacter("Tom", 21)
player2.attack = 50
print(player1)  # <__main__.PlayerCharacter object at 0x7f784c26c1c0>
print(player1.name)  # Cindy
print(player1.age)  # Cindy
print(player2.name)  # Tom
print(player1.name)  # Cindy
print(player2.attack)  # 50
help(player1) # Gives the entire blueprint of that object
help(list) # prints the blueprint
print(player2.membership) # True
print(player1.shout())
print(player2.shout())

print(player1.adding_things(2,3)) # <__main__.PlayerCharacter object at 0x7f48ba4da970>

player3 = PlayerCharacter.adding_things(2,3)
print(player3) # <__main__.PlayerCharacter object at 0x7fdd76704970>

# Abstraction
print(player2.shout())
print((1,2,3,1).count(1))
print(len((1,2,3,1)))

# Inheritance
class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("Logged in")

class Wizard(User): # Pass in the parent class for inheritance
    def __init__(self, name, power):
        # super().__init__() # Do not need self when using super()
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with the power of {self.power}")

class Archer(User): # Pass in the parent class for inheritance
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f"{self.arrows} remaining")

    def run(self):
        print("Runs fast")

# Multiple inheritance - Be cautious as this adds complexity
class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

hb1 = HybridBorg("Borg", 100, 150)
print(hb1.attack())

wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 100)
print(wizard1)
print(wizard1.sign_in()) # Inherited from User class
wizard1.attack()  # Attacking with the power of 50
#archer1.attack()  # Attacking with arrows: arrows left-100

# isinstance(instance, Class)
print(isinstance(wizard1, Wizard))  # True
print(isinstance(wizard1, User))  # True

# Polymorphism
# Above we have attack which is shared but each one does something different
# The object calling attack will cause attack to print different output
print(wizard1.attack())

#def player_attack(char):
#    char.attack()

# Same function gives a different output
# player_attack(wizard1)
# player_attack(archer1)

# Once again, two different output calling the same method
#for char in [wizard1, archer1]:
#   char.attack()


wizard2 = Wizard("Elminster", 60)
print(wizard2)

# Introspection
print(dir(wizard1)) # gives all methods and attributes the method has access to

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age

# dunder methods
action_figure = Toy("Red", 0)
print(action_figure.__str__())
print(str(action_figure))

# Method Resolution Order - MRO
# Rule that Python follows which method to run when there aremore than one
class A:
    num = 10
class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass

#       A
#     /   \
#     B   C
#      \ /
#       D

print(D.num)  # 1  MRO = D > B > C > A
print(D.mro())  # prints the order or MRO of that class











