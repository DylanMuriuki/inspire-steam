# Name : Dylan Muriuki
# Date : 19/02/2026
# Program to show objects in python 

class Human:
    # First we define the attributes of a human
    type = "Mammal"
    legs = 2
    brain = True
    warm_blooded = True
    city = "Nairobi"

    # We then create a constructor for this class/object
    # The constructor will be used to create copies of this object
    def __init__(self, name, age):
        self.human_name = name
        self.human_age = age

    def tell_story(self):
        print(f"Hello I am {self.human_name} and here is a story")
        print("The blacker the berry the sweeter the juice")

# create the humans
Dylan = Human("Dylan", 17)
Vinicky = Human("Vinicky", 30)

#Let the humans created do things
Dylan.tell_story()
print("Dylan's age is", Dylan.human_age)

# Modify one of the objects without modifying other objects
Vinicky.city = "Kiambu"
print("Vinicky's location", Vinicky.city)
print("Dylan's location", Dylan.city)