# 类 class1
class Dog:
    """A simple attempt to simulate a dog"""

    def __init__(self, name, age):
        """Initialize properties name and age"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog crouching when command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over when commanded."""
        print(self.name.title() + " rolled over!")


my_dog = Dog("da1", 3)
print("My dog's name is " + my_dog.name.title() + ".")
# My dog's name is Da1.
print("My dog is " + str(my_dog.age) + " years old.")
# My dog is 3 years old.
my_dog.sit()  # Da1 is now sitting.
my_dog.roll_over()  # Da1 rolled over!
