
person=("Mehedi","Hasan","Ratul",29,3.54)

print(person[2])

fName=person[0]
mName=person[1]
lName=person[2]
age=person[3]
cgpa=person[4]

print(f"Your CGPA is:{cgpa}")

#searching in tuple
print('Mehedi' in person)

#joining tuples
fruits=("Mango","orange","banana")

new_tuple=person+fruits
print(new_tuple)

