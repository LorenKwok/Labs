#30 Days of Python
#Day 5 - Lists

#Exercises: Level 1
#1. Declare an empty list

empty_list = list()
print(len(empty_list))

#2. Declare a list with more than 5 items

list = ['Thor', 'Steve', 'Tony', 'Bruce', 'Natasha']
print(len(list))

#3. Find the length of your list

print('Avengers:', list)
print('Number of Avengers:', len(list))

#4. Get the first item, the middle item and the last item of the list
print(list[0],list[2],list[4])

#5.Declare a list called mixed_data_types, 
# put your(name, age, height, marital status, address)

mixed_data_types = ['Loren', 31, '178cm', 'single', 'address']

#6. Declare a list variable named it_companies and assign initial values 
# Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

#7. Print the list using print()
print(it_companies)

#8. Print the number of companies in the list
print(len(it_companies))

#9. Print the first, middle and last company
print(it_companies[0],it_companies[3],it_companies[6])

#10. Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print(it_companies) 

#11. Add an IT company to it_companies
it_companies.insert(2,'Cisco')
print(it_companies)

#12. Insert an IT company in the middle of the companies list
it_companies.insert(4,'CrowdStrike')
print(it_companies)

#13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = 'META'
print(it_companies)

#14. Join the it_companies with a string '#;  '
print("#;  ".join(it_companies))

#15. Check if a certain company exists in the it_companies list.
print('Apple' in it_companies) #True

#16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

#17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

#18. Slice out the first 3 companies from the list
it_companies_copy = it_companies.copy() #So that I will retain a full list for next questions
del it_companies_copy[0:3]
print(it_companies_copy)


#19. Slice out the last 3 companies from the list
it_companies_copy = it_companies.copy()
del it_companies_copy[-3:]
print(it_companies_copy)

#20. Slice out the middle IT company or companies from the list
it_companies_copy = it_companies.copy()
del it_companies_copy[2:5]
print(it_companies_copy)

#21. Remove the first IT company from the list
it_companies_copy = it_companies.copy()
del it_companies_copy[0]
print(it_companies_copy)

#22. Remove the middle IT company or companies from the list
it_companies_copy = it_companies.copy()
del it_companies_copy[4]
print(it_companies_copy)

#23. Remove the last IT company from the list
it_companies_copy = it_companies.copy()
del it_companies_copy[-1]
print(it_companies_copy)

#24. Remove all IT companies from the list
it_companies_copy = it_companies.copy()
it_companies_copy.clear()
print(it_companies_copy)

#25. Destroy the IT companies list
it_companies_copy = it_companies.copy()
del it_companies_copy
try:
    print(it_companies_copy)
except NameError:
    print('countries is not defined') #Using try/except to tell Python to determine if there is an error. I am using this method to continue running the subsequent code.

#26. Join the following lists:
#front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#back_end = ['Node','Express', 'MongoDB']

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
code_base = front_end+back_end
print(code_base)

#27.After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = code_base.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

#Exercises: Level 2
#1. The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print('Min age:', ages[0],)
print('Max age:', ages[-1])

#Add the min age and the max age again to the list
ages.insert(0,19)
ages.insert(-1,26)
print(ages)

#Find the median age (one middle item or two middle items divided by two)
median_age = ages[5]/2
print('The median age is:', median_age)

#Find the average age (sum of all items divided by their number)
ages_sum = sum(ages)
ages_average = ages_sum/(len(ages))
print('The average of all ages is:', ages_average)

#Find the range of the ages (max minus min)
print('The range of all ages is :', ages[-1] - ages[0])

#Compare the value of (min - average) and (max - average), use abs() method
abs((ages[0]-ages_average)-(ages[-1]-ages_average))

#1. Find the middle country(ies) in the countries list https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py
from countries import countries #importing the list from the countries.py instead of typing it all here
print(len(countries)) #determine if the number of countries is even or odd to see if there are multiple middle countries. Since it is not an odd number, only one middle country
print('Middle country:', countries[(len(countries)//2)]) #if it was an even number, would need to find countries[lens(countries)//2] and countries[lens(countries)//2-1] for both middle countries

#2. Divide the countries list into two equal lists if it is even if not one more country for the first half.
countries_firsthalf = countries[0:len(countries)//2]
print(countries_firsthalf)
countries_secondhalf = countries[len(countries)//2+1:]
print(countries_secondhalf) 

#3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country,*scandic_countries = countries
print(first_country, second_country, third_country, scandic_countries)