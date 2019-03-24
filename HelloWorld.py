from typing import List

print("Hello World!")

# string format function

name = 'Bartek'
machine = 'Mac'

print("Hello {0} !. I`m {1}".format(name, machine))

print(f"Nice to meet you {name}, I`m {machine} :)")

''' ########## statements ########## '''

if name.isdigit():
    print("No!")
else:
    print("Yes")

''' ############ lists ############# '''

students = ['Anna', 'Maria', 'Wesolowska']

print(students)
print(students[0] == 'Anna')

students[2] = 'Jola'  # replacing elements
print(students)

students.append("Tola")  # adding elements
print(students)

len(students)  # number of elements
