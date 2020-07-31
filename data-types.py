type(99.9)
type("False")
type(False)
type('0')
type(0)
type(True)
type('True')
type([{}])
type({'a':[]})

# A term or phrase typed into a search box? str
# If a user is logged in? bool
# A discount amount to apply to a user's shopping cart? float
# Whether or not a coupon code is valid? bool
# An email address typed into a registration form? str
# The price of a product? float
# A Matrix? list
# The email addresses collected from a registration form? dict
# Information about applicants to Codeup's data science program? dict

'1' + 2
6 % 4
type(6 % 4)
type(type(6 % 4))
'3 + 4 is ' + 3 + 4
0 < 0
'False' == False
True == 'True'
5 >= -5
!False or False
True or "42"
!True && !False
6 % 5
5 < 4 and 1 == 1
'codeup' == 'codeup' and 'codeup' == 'Codeup'
4 >= 0 and 1 !== '1'
6 % 3 == 0
5 % 2 != 0
[1] + 2
[1] + [2]
[1] * 2
[1] * [2]
[] + [] == []
{} + {}

# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?
tlm_rental_len = 3
bb_rental_len = 5
h_rental_len = 1
price_pmpd = 3
total_rental_payment = tlm_rental_len * price_pmpd + bb_rental_len * price_pmpd + h_rental_len * price_pmpd

print(total_rental_payment)
# total__rental_payment = 27

# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
google_pph = 400
amazon_pph = 380
facebook_pph = 350

facebook_hours = 10
google_hours = 6
amazon_hours = 4

total_contractor_payment = google_pph * google_hours + amazon_pph * amazon_hours + facebook_pph * facebook_hours

print(total_contractor_payment)
# total_contractor_payment = 7420

# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
class_full = False
class_schedule_conflict = False

can_be_enrolled = not class_full and not class_schedule_conflict

print(can_be_enrolled)

# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.
num_items_more_than_2 = False
premium_member = True 
offer_not_expired = False 

offer_applied = (num_items_more_than_2 or premium_member) and not offer_not_expired

print(offer_applied)

# Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'
# Create a variable that holds a boolean value for each of the following conditions:

# the password must be at least 5 characters
password_at_least_5 = len(password) >= 5
print(password_at_least_5)

# the username must be no more than 20 characters
username_length_no_more_than_20 = len(username) <= 20
print(username_length_no_more_than_20)

# the password must not be the same as the username
password_username_different = username != password
print(password_username_different)

# bonus neither the username or password can start or end with whitespace
whitespace = (password[0] == ' ') or (password[-1] == ' ') or (username[0] == ' ') or (username[-1] == ' ')

# the previous solution will only detect a single whitespace. We can use the strip() function to detect multiple whitespaces (although the previous solution will still work even in the case of multiple whitespaces)

whitespace_check = (password == password.strip()) or (username == username.strip())

# if we want to be extra about it, we can create a function that passes in arguments
def is_there_whitespace(username, password):
    username_stripped = username.strip()
    password_stripped = password.strip()
    if username != username_stripped:
        return True
    elif password != password_stripped:
        return True
    else:
        return False

print(is_there_whitespace(username, password))

# 17 LIST COMPREHENSION PROBLEMS IN PYTHON

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]

uppercased_fruits = [fruit.upper() for fruit in fruits]

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

capitalized_fruits = [fruit.title() for fruit in fruits]

capitalized_fruits_v2 = [fruit.capitalize() for fruit in fruits]

# Exercise 2b - capitalize only the 3rd character in each fruit
[fruit[0:2] + fruit[2].capitalize() + fruit[3:] for fruit in fruits]

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.

# This first solution is not a list comprehension, but helped me to wrap my head around what the list comprehension would need to ultimately look like
# Working through the problem. This next bit of code is not list comprehension. 
fruits_with_more_than_two_vowels_not_list_comprehension = []
for fruit in fruits:
    vowel_count = 0
    for letter in fruit:
        if letter in ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']:
            vowel_count += 1
    if vowel_count > 2:
        fruits_with_more_than_two_vowels_not_list_comprehension.append(fruit)

# This next attempt accurately picks fruits that have two or more vowels but duplicates those fruits in the final list with the number of duplicates based on the length of the fruit string.  
fruits_with_more_than_two_vowels_lc = [fruit for fruit in fruits for letter in fruit if (fruit.count('a') + fruit.count('A') + fruit.count('e') + fruit.count('E') + fruit.count('i') + fruit.count('I') + fruit.count('o') + fruit.count('O') + fruit.count('U') + fruit.count('u')) > 1]

# This is the working solution
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if fruit.count('a') + fruit.count('A') + fruit.count('e') + fruit.count('E') + fruit.count('i') + fruit.count('I') + fruit.count('o') + fruit.count('O') + fruit.count('U') + fruit.count('u') > 2]

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

fruits_with_only_two_vowels = [fruit for fruit in fruits if fruit.count('a') + fruit.count('A') + fruit.count('e') + fruit.count('E') + fruit.count('i') + fruit.count('I') + fruit.count('o') + fruit.count('O') + fruit.count('U') + fruit.count('u') == 2]

# Exercise 5 - make a list that contains each fruit with more than 5 characters

fruits_with_more_than_5_characters = [fruit for fruit in fruits if len(fruit) > 5]

# Exercise 6 - make a list that contains each fruit with exactly 5 characters

fruits_with_exactly_5_characters = [fruit for fruit in fruits if len(fruit) == 5]

# Exercise 7 - Make a list that contains fruits that have less than 5 characters

fruits_with_less_than_5_characters = [fruit for fruit in fruits if len(fruit) < 5]

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

number_of_characters_in_each_fruit_in_fruits = [len(fruit) for fruit in fruits]

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

fruits_with_letter_a = [fruit for fruit in fruits if fruit.count('a') > 0]

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

odd_numbers = [number for number in numbers if number % 2 == 1]

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

positive_numbers = [number for number in numbers if number > 0]

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

negative_numbers = [number for number in numbers if number <0]

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals

numbers_with_2_or_more_numerals = [number for number in numbers if (number >= 10 or number <= -10)]
print(numbers_with_2_or_more_numerals)

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

numbers_squared = [number ** 2 for number in numbers]

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

odd_negative_numbers = [number for number in numbers if number % 2 == 1 and number < 0]

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 

numbers_plus_5 = [number + 5 for number in numbers]

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.

total = 0
total += 5
total -= 2
total *= 2
print(total)

def prime_number_detector(num):
    if num > 1:
        if num == 2:
            return True
        for i in range(2, num):
            if (num % i) == 0:
                return False 
        else: 
            return True
    else: 
        return False
        
primes = [number for number in numbers if prime_number_detector(number) == True]
print(primes)

students = [{"id": "100001", "student": "Ada Lovelace", "coffee_preference": "light", "course": "web development", "grades": [70, 91, 82, 71], "pets": [{"species": "horse", "age": 8}]},{"id": "100002", "student": "Thomas Bayes", "coffee_preference": "medium", "course": "data science", "grades": [75, 73, 86, 100], "pets": []}, {"id": "100003", "student": "Marie Curie", "coffee_preference": "light", "course": "web development", "grades": [70, 89, 69, 65], "pets": [{"species": "cat", "age": 0}]}, {"id": "100004", "student": "Grace Hopper", "coffee_preference": "dark", "course": "data science", "grades": [73, 66, 83, 92], "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}]}, {"id": "100005", "student": "Alan Turing", "coffee_preference": "dark", "course": "web development", "grades": [78, 98, 85, 65], "pets": [{"species": "horse", "age": 6}, {"species": "horse", "age": 7}, {"species": "dog", "age": 5}]}, {"id": "100006", "student": "Rosalind Franklin", "coffee_preference": "dark", "course": "data science", "grades": [76, 70, 96, 81], "pets": []}, {"id": "100007", "student": "Elizabeth Blackwell", "coffee_preference": "dark", "course": "web development", "grades": [69, 94, 89, 86],"pets": [{"species": "cat", "age": 10}]}, {"id": "100008","student": "Rene Descartes","coffee_preference": "medium","course": "data science","grades": [87, 79, 90, 99],"pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}]},{"id": "100009","student": "Ahmed Zewail","coffee_preference": "medium","course": "data science","grades": [74, 99, 93, 89],"pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}]},{"id": "100010","student": "Chien-Shiung Wu","coffee_preference": "medium","course": "web development","grades": [82, 92, 91, 65],"pets": [{"species": "cat", "age": 8}]},{"id": "100011","student": "William Sanford Nye","coffee_preference": "dark","course": "data science","grades": [70, 92, 65, 99],"pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}]},{"id": "100012","student": "Carl Sagan","coffee_preference": "medium","course": "data science","grades": [100, 86, 91, 87],"pets": [{"species": "cat", "age": 10}]},{"id": "100013","student": "Jane Goodall","coffee_preference": "light","course": "web development","grades": [80, 70, 68, 98],"pets": [{"species": "horse", "age": 4}]},{"id": "100014","student": "Richard Feynman","coffee_preference": "medium","course": "web development","grades": [73, 99, 86, 98],"pets": [{"species": "dog", "age": 6}]}]

# How many students are there?
print(len(students))
# How many students prefer light coffee? For each type of coffee roast?
light_coffee_count = 0
for 
# How many types of each pet are there?
# How many grades does each student have? Do they all have the same number of grades?
# What is each student's grade average?
# How many pets does each student have?
# How many students are in web development? data science?
# What is the average number of pets for students in web development?
# What is the average pet age for students in data science?
# What is most frequent coffee preference for data science students?
# What is the least frequent coffee preference for web development students?
# What is the average grade for students with at least 2 pets?
# How many students have 3 pets?
# What is the average grade for students with 0 pets?
# What is the average grade for web development students? data science students?
# What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
# What is the average number of pets for medium coffee drinkers?
# What is the most common type of pet for web development students?
# What is the average name length?
# What is the highest pet age for light coffee drinkers?