#30 Days of Python
#Day 4 - Strings

#1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string = ['Thirty','Days','Of','Python']
string_concat = ' '.join(string)
print(string_concat)

#2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string = ['Coding', 'For' , 'All']
string_concat = ' '.join(string)
print(string_concat)

#3. Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding for All'

#4. Print the variable company using print().
print(company)

#5. Print the length of the company string using len() method and print().
print(len(company))

#6. Change all the characters to uppercase letters using upper() method.
print(company.upper())

#7. Change all the characters to lowercase letters using lower() method.
print(company.lower())

#8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print('Coding For All'.capitalize())
print('Coding For All'.title())
print('Coding For All'.swapcase())

#9. Cut(slice) out the first word of Coding For All string.
print('Coding For All'[6:])
print('Coding For All'.strip('Coding'))

#10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print('Coding For All'.find('Coding'))
print('Coding For All'.index('Coding'))
print('Coding For All'.rindex('Coding'))

#11.Replace the word coding in the string 'Coding For All' to Python.
print('Coding For All'.replace('Coding','Python'))

#12. Change "Python for Everyone" to "Python for All" using the replace method or other methods.
print('Python For Everyone'.replace('Python For Everyone', 'Python for All'))

#13. Split the string 'Coding For All' using space as the separator (split()) .
print('Coding For All'.split())

#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
tech_comp = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(tech_comp.split(','))

#15. What is the character at index 0 in the string Coding For All.
print('Coding For All'[0])

#16. What is the last index of the string Coding For All.
print('Coding For All'[-1])

#17. What character is at index 10 in "Coding For All" string.
print('Coding For All'[10])

#18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
string_split = 'Python For Everyone'.split()
string_acronym = string_split[0][0] + string_split[1][0] + string_split[2][0]
print(string_acronym)

#19. Create an acronym or an abbreviation for the name 'Coding For All'.
string_split = 'Coding For All'.split()
string_acronym = string_split[0][0] + string_split[1][0] + string_split[2][0]
print(string_acronym)

#20. Use index to determine the position of the first occurrence of C in Coding For All.
print('Coding For All'.index('C'))

#21. Use index to determine the position of the first occurrence of F in Coding For All.
print('Coding For All'.index('F'))

#22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print('Coding For All'.rfind('l'))

#23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
#'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
print(sentence.find('because'))

#24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 
#'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))

#25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence[0:30] + sentence[54:])

sentence = 'You cannot end a sentence with because because because is a conjunction'
because_last_position = sentence.rindex('because')
because_last_letter_index = len('because')+because_last_position
print(sentence[0:30] + sentence[because_last_letter_index:])

#26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

#27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction' (Repeating question from question 25 for some reason)
sentence = 'You cannot end a sentence with because because because is a conjunction'
because_first_position = sentence.index('because')
because_last_position = sentence.rindex('because')
because_last_letter_index = len('because')+because_last_position
print(sentence[0:because_first_position] + sentence[because_last_letter_index+1:])

#28. Does 'Coding For All' start with a substring Coding?
print('Coding For All'.startswith('Coding')) #True

#29. Does 'Coding For All' end with a substring coding?
print('Coding For All'.endswith('coding')) #False

#30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
sentence = '   Coding For All      '
print(sentence.strip('      '))

sentence = '   Coding For All      '
start = sentence.index('Coding')
end = sentence.index('All') + 3
print(sentence[start:end])

#31. Which one of the following variables return True when we use the method isidentifier():
print('30DaysOfPython'.isidentifier()) #False
print('thirty_days_of_python'.isidentifier()) #True

#32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(python_libraries))

#33. Use the new line escape sequence to separate the following sentences.
#I am enjoying this challenge.
#I just wonder what is next.

print('I am enjoying this challenge.\nI just wonder what is next.')

#34. Use a tab escape sequence to write the following lines
#Name      Age     Country   City
#Asabeneh  250     Finland   Helsinki

print('Name \t\t Age \t Country \t City \nAsabeneh \t 250 \t Finland \t Helsinki') #Have to do an extra \t between Name and Age for alignment

#35. Use the string formatting method to display the following:
#radius = 10
#area = 3.14 * radius ** 2
#The area of a circle with radius 10 is 314 meters square.

radius = 10
area = 3.14 * radius ** 2
print('radius = {}'.format(radius))
print('3.14 * radius ** 2')
print('The area of a circle with radius {} is {} meters square.'.format(radius, area))

#36. Make the following using string formatting methods:
#8 + 6 = 14
#8 - 6 = 2
#8 * 6 = 48
#8 / 6 = 1.33
#8 % 6 = 2
#8 // 6 = 1
#8 ** 6 = 262144

a = 8
b = 6
print('%s + %s = %s'%(a,b, a+b))
print('%s - %s = %s'%(a,b, a-b))
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b}')
print('{} % {} = {}'.format(a,b,a%b))
print('{} // {} = {}'.format(a,b,a//b))
print(f'{a} ** {b} = {a**b}')