# 类 class1
class Dog:
    """A simple attempt to simulate a dog"""

    def __init__(self, name, age):
        """Initialize properties name and age"""
        self.name = name
        self.age = age
        self.character = "cute"

    def sit(self):
        """Simulate a dog crouching when command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over when commanded."""
        print(self.name.title() + " rolled over!")

    def update_character(self, char1):
        """Sets the character to the specified value"""
        self.character = char1


my_dog = Dog("da1", 3)
my_dog2 = Dog("da2", 2)
print("My dog's name is " + my_dog.name.title() + ".")
# My dog's name is Da1.
print("My dog is " + str(my_dog.age) + " years old.")
# My dog is 3 years old.
my_dog.sit()  # Da1 is now sitting.
my_dog.roll_over()  # Da1 rolled over!

print(my_dog.character)  # cute
my_dog.character = "cute2"
print(my_dog.character)  # cute2
my_dog.update_character("cute_update")
print(my_dog.character)  # cute_update


class Characteristics:
    """A simple attempt to simulate the characteristics of a dog."""

    def __init__(self, character5="cute5"):
        """Initialize dog attributes"""
        self.character5 = character5

    def describe_character5(self):
        print("This dog has " + str(self.character5) + " characteristics")


class BorderCollieDog(Dog):
    """What makes this Class unique"""

    def __init__(self, name, age):
        """Initialize a property of the superclass"""
        super().__init__(name, age)
        self.intelligence_quotient = "high"
        self.characteristics = Characteristics()

    def describe_iq(self):
        """Print a message describing the Border Collie IQ"""
        print("this dog has " + self.intelligence_quotient + " IQ!")

    def sit(self):
        """Simulate a Border Collie crouching when command."""
        print(self.name.title() + " now sits perfectly.")


my_bc = BorderCollieDog("bc1", "1")
print(my_bc.name)  # bc1
my_bc.describe_iq()  # this dog has high IQ!
my_bc.sit()  # Bc1 now sits perfectly.

# This dog has cute5 characteristics
my_bc.characteristics.describe_character5()

# 假设有个模块是dog.py，其中包含Dog类 等等，可以这样导入类：
# Let's say we have a module called dog.py that contains the Dog class etc.
# We can import the class like this:
# from dog import Dog, Dog1, Dog2
# from dog import *
# import dog
# my_new_dog = Dog("new1", 1)
