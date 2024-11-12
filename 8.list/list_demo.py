fruits=['orange','banana','apple']
cities=['Dhaka','Chattogram','Rajshahi','Sylhet']
country=['Bangladesh','Australia','India','USA', 'Pakistan','UK','Canada']

'''print(country[0])
first_country=country[0]
print(first_country)

#slicing country
poweful=country[0:4]
print(poweful)

abc=country[3:]
print(abc)

#changing items
country[4]='France'
print(country)'''

#checking is there any item present or not
print('UK' in country)

#adding any item with the list
country.append('Srilanka')
print(country)

#removing item
country.remove('Pakistan')
print(country)

#insert in specific condition
country.insert(4,'Pakistan')
print(country)

#remove last item
country.pop()
print(country)

#count the list items
print(len(country))

#sort the list item
country.sort()
print(country)

#reverse the list
country.reverse()
print(country)

#clear all items
country.clear()
print(country)
