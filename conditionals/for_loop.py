
def dhaka():
    print("Dhaka112")
    for i in range(5):
        print(i)

#print 1 to 10
def func_1():
    for i in range ( 1 , 11 , 2 ) :
        print ( i )

def func_2():
    number = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
    for i in number :
        print(f"Iteration: {i}")

def func_3():
    language = "English"
    for i in language :
        print ( i )

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
def all_keys(dic):
    for i in dic:
        print(i)

#for all values
def all_values(dic):
    for j in person.values ( ) :
        print ( j )


#for all keys and values
def all_key_and_values(dic):
    for key , value in person.items ( ) :
        print ( f"{key} : {value}" )


def specific_keys(dic):
    for key in person :
        if key == "name" :
            print ( key )


#for specific key and value
def key_value_of_dictionary(dic):
    for key , value in dic.items ( ) :
        if key == "name" :
            print ( key , value )


#create a list with all keys
def create_key_list_from_dic(dictionary):
    list = []
    for key in dictionary:
        list.append ( key )
    print ( f"Kye List is:{list}" )


#create a list with all the values
def create_Valu_list_from_dictionary(dictionary):
    value_list = []
    for value in dictionary.values ():
        value_list.append (value)
    print ( f"Value List is:{value_list}" )

#dhaka()
#func_1()
#func_2()
#func_3()
#all_keys(person)
#all_values(person)
#all_key_and_values(person)
#specific_keys(person)
key_value_of_dictionary(person)
create_key_list_from_dic(person)
create_Valu_list_from_dictionary(person)








