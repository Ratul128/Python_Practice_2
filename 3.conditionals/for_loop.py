
'''def dhaka():
    print("Dhaka112")

for i in range(5):
    print(i)
    dhaka()'''

#print 1 to 10

'''for i in range(1,11,2):
    print(i)'''


'''number=[1,2,3,4,5,6,7,8,9]

for i in number:
    print(f"Iteration: {i}")'''

'''language="English"

for i in language:
    print(i)'''

#print dictionary using loop
person={
    "name":"Ratul",
    "age": 29,
    "city":"Dhaka",
    "skills":["python","java","C#"],
    "full_address":
        {
            "street":"123, main road",
            "house":"123/ad",
            "old house":{
                "old house no":"1/12, 455 dhaka",
                "old house color": "black"
            }
        },
    "hobby": ("travel","guitar play","photography")
}

#for all key
'''for i in person:
    print(i)

#for all values
for j in person.values():
    print(j)

#for all keys and values
for key,value in person.items():
    print(f"{key} : {value}")

for key in person:
    if key=="name":
        print(key)

#for specific key and value
for key,value in person.items():
    if key=="name":
        print(key,value)

#create a list with all keys
list=[]
for key in person:
    list.append(key)
print(f"List is:{list}")'''

#create a list with all the values
value_list=[]
for value in person.values():
    value_list.append(value)
print(f"Value is:{value_list}")




