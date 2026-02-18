#Name:Dylan Muriuki
#Date:18/02/2026
#Program to show lists in python

#Lists of friends
friends=["Bob","Joel","Rachael","Monica","Angela","Phoebe","Ross"]

print(friends)

friends.sort() #sort function
print(friends)

friends.reverse() #reverse function
print(friends)

friends.append("Jack") #append function adds
print(friends)

new_friends=["Tracy","James","Faith","Don","Augustine","Wendy"]
print(len(new_friends))

#New list of students
students = friends + new_friends
print(students)
students.pop() #Pop function removes the last item
print(students)

students.insert(5,"Jenny") #Insert function
students.insert(9,"Vallary")
print(students)

students.extend("Dan")#Extend function
print(students)

students.remove("Ross") #Remove function
print(students)

new_students=students.copy() #Copy function
print(new_students)