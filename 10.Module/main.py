
#import my_module

#option_1
import my_module
full_name_new=my_module.generate_fullname("Ratul","Hasan")
print(full_name_new)

#option_2
import my_module as FullName
full_name_new=FullName.generate_fullname("Ratul","Hasan")
print(full_name_new)

#option_3
from my_module import generate_fullname,summation
full_name_new=generate_fullname("Ratul","Hasan")
print(full_name_new)

sum_result=summation(20,30)
print(sum_result)

