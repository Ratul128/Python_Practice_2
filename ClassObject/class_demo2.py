
class Person:
    def __init__(self,name,age,city):
        self.Full_name=name
        self.my_age=age
        self.my_city=city

    def person_info(self):
        return f"Name:{self.Full_name} \nAge:{self.my_age} \nCity:{self.my_city}"

my_obj=Person("Ratul",29,"Kishoreganj")
print(my_obj.person_info())

my_obj2=Person("Mehedi",28,"Dhaka")
print(my_obj2.person_info())

my_obj3=Person("Yakin",25,"Chattogram")
print(my_obj3.person_info())