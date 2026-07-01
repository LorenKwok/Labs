#30 Days of Python
#Day 6 - Tuples

#Exercises: Level 1
#1. Create an empty tuple
tpl = ()
print(tpl)

#2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('King', 'Edwin') 
sisters = ('Karen', 'Sharon')

#3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

#4. How many siblings do you have?
print('Number of siblings:', len(siblings))

#5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('Johnny', 'Emily')
family_members = siblings + parents
print(family_members)

siblings = list(siblings) #Another method which turns the siblings tuple into a list first then add indexes in, and turn it back into a tuple after
family_members = siblings + ['Johnny'] + ['Emily']
family_members = tuple(family_members)
print(family_members)

#Exercises: Level 2
#1. Unpack siblings and parents from family_members
siblings = family_members[0:4]
parents = family_members[-2:]
print(siblings)
print(parents)

#2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'watermelon')
vegetables = ('corn', 'lettuce', 'spinach')
animal_products = ('beef', 'chicken', 'pork')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

#3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_tp = list(food_stuff_tp)

#4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(len(food_stuff_tp)) #9 which is an odd number
middle_food_stuff = food_stuff_tp[len(food_stuff_tp)//2]
print(middle_food_stuff)

#5. Slice out the first three items and the last three items from food_stuff_lt list
first_three_food = food_stuff_tp[0:3]
last_three_food = food_stuff_tp[-3:]
print(first_three_food)
print(last_three_food)

#6. Delete the food_stuff_tp tuple completely
del food_stuff_tp

try:
    print(food_stuff_tp)
except NameError:
    print('Variable does not exist')
    
#7. Check if an item exists in tuple:
#Check if 'Estonia' is a nordic country
#Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)