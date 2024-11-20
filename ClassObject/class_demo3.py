
class Person:
    def __init__(self,name,age,city):
        self.Full_name=name
        self.my_age=age
        self.my_city=city
        self.skills=[]

    def person_info(self):
        return f"Name:{self.Full_name} \nAge:{self.my_age} \nCity:{self.my_city}"

    def add_skills(self,abc):
        self.skills.append(abc)


my_obj=Person("Ratul",29,"Kishoreganj")
print(my_obj.person_info())

my_obj.add_skills("Python")
my_obj.add_skills("Java")
my_obj.add_skills("C++")
print(my_obj.skills)
