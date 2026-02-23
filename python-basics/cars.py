# Name : Dylan Muriuki
# Date : 23/02/2026
#Program to show classes in python

class Car():
    #attributes of the car
    def __init__(self,model,make,colour,year):

    self.model = model
    self.make = make        
    self.colour = colour
    self.year = year

    #print car details
    def print_details(self,model,make,colour,year):
        print(f"{make} {model} of {colour} colour was manufactured in the year 2001")

#Instantiate a class object

my_car = Car("Azenza","Mazda","Red","2022")
dads_car = Car("Landcruiser","Toyota","Black","2025")

my_car.print_details("Azenza","Mazda","Red","2022")