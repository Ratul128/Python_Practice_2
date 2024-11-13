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

print(person["age"])
print(person["skills"])
print(person["skills"][0])
print(person["hobby"][1])

print(person["full_address"]["street"])

print(person["full_address"]["old house"]["old house no"])