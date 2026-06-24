#30 Days of Python
#Day 3 - Operators

integer = 31 #1. Declare age as integer variable
height = 5.8 #2. Declare height as a float variable
complex = 1+1j #3. Declare a variable that store a complex number

#4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Enter base:"))
height = float(input("Enter height:"))
area = (0.5)*base*height
print("The area of the triangle is:", area)

#5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = float(input("Enter side a:"))
side_b = float(input("Enter side b:"))
side_c = float(input("Enter side c:"))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is:", perimeter)

#6.Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length =  float(input("Enter length of the rectangle:"))
width =  float(input("Enter width of the rectangle:"))
area = (length)*(width)
perimeter = 2*(length+width)
print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)

#7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input("Enter the radius of the circle:"))
area = 3.14*radius*radius
circumference = 2*3.14*radius
print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference)

#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope_q8 = 2
x_intercept = 1
y_intercept = -2

print("The slope is:", slope_q8)
print("The x-intercept is:", x_intercept)
print("The y-intercept is:", y_intercept)

#9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, x2, y1, y2 = 2, 6, 2, 10
slope_q9 = (y2-y1)/(x2-x1)
print("The slope is:", slope_q9)
euclidean_distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
print("The Euclidean distance between point (2, 2) and point (6,10) is:", euclidean_distance)

#10. Compare the slopes in tasks 8 and 9.
print("The slope in task 8 is:", slope_q8, ".", "The slop in task 9 is:", slope_q9, ".", "The slope in task 8 minus the slope in task 9 is:", slope_q8-slope_q9, ".")

#11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

x = float(input("Enter a value for x:"))
y = x**2 + (6*x) + 9
print("You entered the value of x:", x)
print("The value of y is:", y) #The value of y is 0 when x = -3

#12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') > len('dragon')) #Will print as False since both are the same length

#13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in ('python' and 'dragon')) #Prints True since 'on' is found in both

#14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence
print('jargon' in 'I hope this course is not full of jargon') #Prints True since 'jargon' is in the sentence

#15. There is no 'on' in both dragon and python
print('on' not in ('dragon' and 'python')) #Prints False since 'on' is found in both

#16. Find the length of the text python and convert the value to float and convert it to string
len_python = len('python')
len_python = float(len_python)
print(type(len_python))
len_python = str(len_python)
print(type(len_python))

#17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input("Enter a number:"))
print("The number is even:",number % 2 == 0)

#18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
value = 2.7
value = int(value)
print(type(value))
print(7//3 == value) #Should return true since 7//3 is 2 and int(2.7) is also 2

#19. Check if type of '10' is equal to type of 10
print(type('10') == type(10)) #Should return false since '10' is a string and 10 is an integer

#20. Check if int('9.8') is equal to 10
print(int('9.8') == 10) #Returns an error on purpose since '9.8' is a string and cannot be converted to an integer

#21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = input("Enter hours:")
rate_per_hour = input("Enter rate per hours:")
print("Your weekly earning is:", float(hours)*float(rate_per_hour)) #In the example provided, hours are 40 and rate per hour is 28. The weekly earning should be 1120

#22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
year = input("Enter the number of years you have lived:")
seconds = int(year)*365*24*60*60
print("You have lived for:", seconds, "seconds", ".")

#23. Write a Python script that displays the following table
#1 1 1 1 1
#2 1 2 4 8
#3 1 3 9 27
#4 1 4 16 64
#5 1 5 25 125

print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)