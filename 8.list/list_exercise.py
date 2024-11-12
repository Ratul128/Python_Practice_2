
'''user=[]

for i in range(5):
    user_name=input("Enter the name:")
    user.append(user_name)

print(user)'''

country=[]
for i in range(5):
    index_number = int ( input ( "Enter index number between 0 to 4:" ) )
    cName=input("Enter country name:")
    country.insert(index_number, cName)
print(country)
