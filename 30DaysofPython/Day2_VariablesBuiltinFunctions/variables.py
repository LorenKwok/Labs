#30 Days of Python# 
#Day 2 - Variables, Builtin Functions#

#Exercises: Level 1

first_name = 'Loren'
last_name = 'Kwok'
full_name = 'Loren Kwok'
country = 'Canada'
city = 'Vancouver'
age = 31
year = 2026
is_married = False
is_true = True
is_light_on = True

print (first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on)

character_name, superhero_name, movie, studio, owner = 'Steve Rogers', 'Captain America', 'Avengers', 'Marvel', 'Disney'

print (character_name, superhero_name, movie, studio, owner)

#Exercises: Level 2

print(type(first_name), type(last_name), type(full_name), type(country), type(city), type(age), type(year), type(is_married), type(is_true), type(is_light_on)) #Check data type of all variables
print(type(character_name), type(superhero_name), type(movie), type(studio), type(owner))

print(len(first_name)) #Check name of first name

print(len(first_name) - len(last_name)) #Compare length of first name and last name

num_one, num_two = 5, 4 #Declare 5 as num_one and 4 as num_two
print(num_one, num_two)

total = num_one + num_two #Add num_one and num_two and assign value to a variable total
print(total)

diff = num_two - num_one #Subtract num_two from num_one and assign value to a variable diff
print(diff)

product = num_two*num_one #Multiply num_two and num_one and assign value to a variable product
print(product)

division = num_two/num_one #Divide num_two by num_one and assign value to a variable division
print(division)

remainder = num_two%num_one #Use modulus division to find num_two divided by num_one and and assign value to a variable remainder
print(remainder)

exponent = num_one**num_two #Calculate num_one to the power of num_two and assign value to a variable exponent
print(exponent)

floor_division = num_two//num_one #Find floor division of num_two by num_one and assign value to a variable floor_division
print(floor_division)

#The radius of a circle is 30 meters
#Calculate the area of a cricle and assign the value to a variable name of area_of_circle
area_of_circle = 3.14*30**2
print(area_of_circle)

user_firstname = input("What is your first name?")
user_lastname = input("What is your last name?")
user_country = input("What is your country?")
user_age = input("What is your age?")
print(user_firstname, user_lastname, user_country, user_age)

help('keywords')
