# Nathan Barton
# 1 October, 2024
# If Else Starter


# Task 2

color = input('Type in any color:')
if color == 'green':
    print('Congradulations! you just earned 5 points!!')
else:
    print('Congradulations! You just earned 10 points!!')


# Task 3
    
first_name = input('Please enter your first name here: ')
if len(first_name) <= 5:
    print('You\'re name is too short.')
else:
    print('You\'re name is very long.')


# Task 4
# Create a Python list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']
    
letter = input('Enter any letter in the alphabet: ').lower()

# Check to see if what the user typed in was a vowel or not
if letter in vowels:
    print('The letter you entered was a vowel!')
else:
    print('The letter you entered was a consonant!')


# Task 5

num1 = int(input('Please enter any integer: '))
num2 = int(input('Please enter another integer: '))

div = num1%num2
if div == 0:
    print('The numbers you entered are divisible by one another.')
else:
    print('The numbers you entered are not divisble by one another.')