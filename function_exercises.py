#!/usr/bin/env python
# coding: utf-8

# Create a file named function_exercises.py for this exercise. After creating each function specified below, write the necessary code in order to test your function.
# 
# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# 
# anything that is not a valid python identifier should be removed
# 
# leading and trailing whitespace should be removed
# 
# everything should be lowercase
# 
# spaces should be replaced with underscores
# 
# for example:
# Name will become name
# 
# First Name will become first_name
# 
# % Completed will become completed
# 
# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# 
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# 
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
# 
# Bonus
# 
# 1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.
# 2. Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# 
# col_index('A') returns 1          |
# col_index('B') returns 2          |
# col_index('AA') returns 27

# ### Question 1
# Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise

# In[150]:


def is_two(x):
    if x == 2 or x == '2':
        return True
    return False

#Testing the function
print(is_two(2))
print(is_two('2'))
print(is_two(1))
print(is_two('beans'))


# ### Question 2
# Define a function named is_vowel. It should return True if the passed string  is a vowel, False otherwise.

# In[151]:


def is_vowel(string):
    if str(string).lower() in ['a', 'e', 'i', 'o', 'u']:
        return True
    return False

#Testing the function
print(is_vowel('A'))
print(is_vowel(1))
print(is_vowel('beans'))
print(is_vowel('m'))


# ### Question 3
# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[39]:


def is_consonant(string):
    if is_vowel(str(string)) or len(str(string)) > 1 or str(string).isdigit():
        return False
    return True

# Testing the function
print(is_consonant("X"))
print(is_consonant('beans'))
print(is_consonant(1))
print(is_consonant('e'))


# ### Question 4
# Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[152]:


def capitalize_first_letter_if_consonant(word):
    if str(word).isdigit():
        return (word)
    elif is_consonant(word[0]):
            return (word[0].upper() + word[1:])
    else:
        return (word)
        
# Testing the function
print(capitalize_first_letter_if_consonant('queen'))
print(capitalize_first_letter_if_consonant('apple'))
print(capitalize_first_letter_if_consonant(123))


# ### Question 5
# Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[74]:


def calculate_tip(bill, tip = 0):
    if tip > 1:
        return "Cannot tip over 100%"
    elif tip < 0:
        return "Cannot tip a negative amount"
    else:
        tip_amount = round((bill * (1 + tip) - bill), 2)
        return tip_amount
    
# Testing the function
print(calculate_tip(50))
print(calculate_tip(50, .2345673))
print(calculate_tip(50, 1.2))
print(calculate_tip(50, -0.2))


# ### Question 6
# Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[153]:


def apply_discount(price, discount):
    if discount > 100:
        return 0
    elif discount < 0:
        return price
    else:
        discount_amount = price * discount / 100
        return price - discount_amount
    
# Testing the function
print(apply_discount(100, 20))
print(apply_discount(100, 100))
print(apply_discount(100, 200))
print(apply_discount(100, -5))


# ### Question 7
# Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[154]:


def handle_commas(string):
    no_commas = ''
    for letter in string:
        if letter != ',':
            no_commas += letter
    return no_commas

# Testing the function
print(handle_commas('1,000,000'))
print(handle_commas('1,,,,,0'))


# ### Question 8
# Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[87]:


def get_letter_grade(num):
    if num >= 90:
        return 'A'
    elif num >= 80:
        return 'B'
    elif num >= 70:
        return 'C'
    elif num >= 60:
        return 'D'
    else:
        return 'F'

# Testing the function
print(get_letter_grade(27))
print(get_letter_grade(-30))
print(get_letter_grade(130))
print(get_letter_grade(77))


# ### Question 9
# Define a function named remove_vowels that accepts a string and returns string with all the vowels removed.

# In[90]:


def remove_vowels(string):
    no_vowels = ''
    for letter in string:
        if not is_vowel(letter) or letter.isdigit():
            no_vowels += letter
    return no_vowels

# Testing the function
print(remove_vowels("Concatenation"))
print(remove_vowels("There were 300 sailors on that ship."))


# ### Question 10
# Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# - anything that is not a valid python identifier should be removed
# - leading and trailing whitespace should be removed
# - everything should be lowercase
# - spaces should be replaced with underscores
# 
# For example:
# - Name will become name
# - First Name will become first_name
# - % Completed will become completed

# In[156]:


def normalize_name(string):
    normalized_string = ''
    stripped_string = string.strip()
    if stripped_string[0].isdigit():
        stripped_string = '_' + stripped_string
    for letter in stripped_string:
        if (letter.isalpha() or letter == '_') and not letter == ' ':
            normalized_string += letter.lower()
        elif letter.isdigit():
            normalized_string += letter
        elif letter == ' ':
            normalized_string += '_'
    return normalized_string

# Testing the function
print(normalize_name(" 3 A#ples . in a pod324"))
print(normalize_name("First Name"))
print(normalize_name("% Completed"))

# Note: This function can also be created more simply by using .isidentifier()


# ### Question 11
# Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# In[104]:


def cumulative_sum(lst_num):
    cumul_sum_lst = []
    for i in range(len(lst_num)):
        cumul_sum_lst.append(sum(lst_num[:i + 1]))
    return cumul_sum_lst

# Testing the function
print(cumulative_sum([1, 2, 3, 4]))
print(cumulative_sum([1, 1, 1]))
print(cumulative_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))


# ### Bonus Question 1
# Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format.

# In[172]:


def twelveto24(time):
    try:
        hour = ''
        minute = ''
        colon_position = time.rindex(':')
        formatted_time = ''
        if time[-2:] == 'am':
            hour = int(time[:colon_position])
            if int(hour) <= 11:
                formatted_time = time[:-2]
                return formatted_time
            else:
                hour = '00'
                minute = time[colon_position + 1:-2]
                formatted_time = hour + ':' + minute
                return formatted_time
        elif time[-2:] == 'pm':
            hour = int(time[:colon_position]) + 12
            minute = time[colon_position + 1:-2]
            formatted_time = str(hour) + ':' + minute
            return formatted_time
        else:
            return "Please input the time in the correct format."
    except ValueError:
        return 'Please input the time in the correct format.'
    
# Testing the function
print(twelveto24('10:45am'))
print(twelveto24('4:30pm'))
print(twelveto24('beans'))
print(twelveto24('6:30pm'))
print(twelveto24('12:15am'))
print(twelveto24('11:59pm'))


# Bonus write a function that does the opposite.

# In[182]:


def twelvefrom24(time24):
    
    colon_position = time24.rindex(':')
    hour = time24[:colon_position]
    minute = time24[colon_position + 1:]
    formatted_time = ''
    if int(hour) == 0:
        hour = '12'
        formatted_time = hour + ':' + minute + 'am'
        return formatted_time
    elif int(hour) < 12:
        formatted_time = time24 + 'am'
        return formatted_time
    elif int(hour) == 12:
        formatted_time = time24 + 'pm'
        return formatted_time
#    elif int(hour) > 12:
    else:
        hour = int(hour) - 12
        formatted_time = str(hour) + ':' + minute + 'pm'
        return formatted_time
    
# Testing the Function    
print(twelvefrom24('8:30'))
print(twelvefrom24('12:17'))
print(twelvefrom24('00:47'))
print(twelvefrom24('13:12'))
print(twelvefrom24('23:59'))
print(twelvefrom24('1:22'))


# #### Bonus Question 2
# Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# - col_index('A') returns 1
# - col_index('B') returns 2
# - col_index('AA') returns 27

# #### Step One: Understanding How Spreadsheets Give Columns Their Name / Step Two: Developing A Mathematical Formula
# In both Google Sheets and Excel, the first column is given the header 'A'. As each new column is added to the right, the headers cycle through the alphabet in a predictable pattern. After, 'A', the next 25 columns are given the headers 'B' through 'Z' alphabetically. 
# 
# Immediately after column 'Z', the very next column is given the header 'AA'. The next 25 columns are given the headers 'AB' through 'AZ' alphabetically. The very next column is given the header 'BA'. We can see a pattern developing. Every 26 columns, the leftmost letter is advanced to the next alphabetic letter. 
# 
# Once we reach 'ZZ', the next column is 'AAA'. 
# 
# Each individual letter in the column header string represents a numerical value. Lets examine this in detail:
# - After 'Z' (Column 26) the next column is 'AA' (Column 27). Or in other words, column 'Z' (26 from 'Z') and column 'AA' (26 from the leftmost 'A' and 1 from the rightmost 'A' = 27)
# - After 'AZ' (26 from 'A' and 26 from 'Z' = 52), the next column is 'BA' (52 from 'B' and 1 from 'A')
# - After 'BZ' (52 from 'B' and 26 from 'Z' = 78), the next column is 'CA' (78 from 'C' and 1 from 'A')
# - After 'ZZ' (676 from 'Z' and 26 from 'Z' = 702), the next column is 'AAA' (702 from 'AA' and 1 from 'A')
# 
# Let's breakdown 'AAA' further:
# - The rightmost 'A' is equal to a numeric value based on its letter (A-Z:1-26). In this case its worth 1.
# - The middle 'A' is equal to 26 * the value of its letter. In this case, 26 * 1 = 26. 
# - The leftmost 'A' is equal to 26 * 26 * the value of its letter. In this case, 26 * 26 * 1 = 676.
# - If we sum the three values up (676 + 26 + 1), we have the column value 703, exactly one more than 'ZZ'. 
# 
# In summary:
# - the rightmost position of any string holds the smallest value. In a sense, it represents the most current cycling through the alphabet. Its value will be equal to A-Z:1-26
# - Moving left, the next position will increase by one letter for every cycle through the alphabet (26 columns).
# - Moving left again, the next position will increase by one letter for every full cycle of the alphabet that the position immediately to the right has gone through. 
# - Putting this in a formula, we see that for n moves to the left from the rightmost letter, the letter in that position has a value of 26 ^ n * A-Z:1-26. 
# 
# As an extended example, column 'AAAA' would equal (reading from the right to left):
# - 26 ^ 0 * 1 = 1 * 1 = 1
# - 26 ^ 1 * 1 = 26 * 1 = 26
# - 26 ^ 2 * 1 = 676 * 1 = 676
# - 26 ^ 3 * 1 = 17576 * 1 = 17576
# - TOTAL = 1 + 26 + 676 + 17576 = 18279

# #### Step Three: Developing a Method to Iterate Through the Header String from Right to Left
# While there are several great methods for iterating through a string from right to left, by using the range function, we can generate a variable "i" that can be simultaneously used as an index and as a mathematical value to represent the increasing value of n from the previous discussion. 
# 
# But how can we iterate from the right to the left? 
# 
# Range takes has three parameters: range(start, end, step)
# 
# We know where to start. The rightmost element of the string, which is at index -1. Therefore range(-1, end, step)
# 
# We know where to end. The leftmost element of the string. But if the string is of varying lengths, how do we determine that? We can use the length function. For example, if we are working with string 'AAA', the len(string) will be 3. That means that we want to end our iteration at index -3. 
# 
# So for 'AAA' should we enter range(-1, -len(string), step)? No. This would tell the iteration to stop BEFORE it reached the leftmost A (string[-3]). So we need it to have an ending value of one further. So the correct code is range(-1, -(len(string) + 1), step). 
# 
# Now how should we move in each step of the range. Well, we are starting at -1 and moving to a more negative value, so our step needs to be -1. The final range for our iteration is range(-1, -(len(string) + 1), -1)

# In[184]:


# Testing our backwards iteration. These will produce the indices that we will feed into our iteration

test_len = 'A'
print(list(range(-1, -(len(test_len) + 1), -1)))
test_len = 'AA'
print(list(range(-1, -(len(test_len) + 1), -1)))
test_len = 'AAA'
print(list(range(-1, -(len(test_len) + 1), -1)))

# Hashtag success


# #### Step Four: Using the Indices From range(-1, -(len(string)+1), -1)  to Develop Our Mathematical Formula
# Let's create a dictionary that maps the letter values to numerical values: 
# letter_to_num = {A:1, B:2, ... , Z:26}
# 
# We know that each letter in the string has a value equal to the following formula:
# 
# Value = letter_to_num['?'] * 26 ^ n, where n is the number of steps to the left of the rightmost element in the string
# 
# Lets use the index numbers we developed from our range to generate n at each position in the string. In the rightmost position, we are 0 steps to the left of the rightmost element. So n needs to equal zero. We have an index value of -1. So if we make n = -(-1 + 1), then n = 0. 
# 
# With this in mind, we can update our formula for the value at any given position to be:
# 
# Value = letter_to_num['?'] * 26 ** -(-index + 1)

# #### Step Five: Putting it All Together

# In[193]:


def col_index(col_name): # The name of our function is col_index() and the parameter will be called col_name
    letter_to_num = {
                    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
                    'H': 8, 'I': 9, 'J':10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
                    'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
                    'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
                     } # Here we create a dictionary that maps our letters to values
    col_value = 0 # This is going to store the the total numerical value of the entire string
    for index in range(-1, -(len(col_name)+1), -1): 
    # We are developing our indices (index) that we will iterate through, starting at -1 and going more negative
        col_value += letter_to_num[(col_name[index])] * (26 ** -(index + 1))
        # To get the final value, we need to find the equivalent value for our letter at our current index
        # col_name[index] is our key for our letter_to_num dictionary
        # letter_to_num[(col_name[index])] will return our numeric value for that letter
        # The rest of the formula will modify that initial value based on its position in the string
        
# Lets walk through the example string 'CMS':
        
# FIRST ITERATION '__S'
# The very first check is on col_name[-1], the rightmost position. It will take the value of that letter
# by referencing the dictionary letter_to_num (S = 19)
# Then it will multiply that value by (26 ** -(-1 + 1)) (notice how this is 26 ** 0) What is 26 ** 0? 1
# So 19 * 1 = 19
# It will add the calculated total via += to col_value (col_value is now 19)

# SECOND ITERATION '_M_'
# The next check is on col_name[-2], the second to last position. It will take the value of that letter
# by referencing the dictionary letter_to_num (M = 13)
# Then it will multiply that value by (26 ** -(-2 + 1)) (notice how this is 26 ** 1) What is 26 ** 1? 26
# So 13 * 26 = 338
# It will add the calculated total to col_value (col_value is now 357)

# THIRD ITERATION 'C__'
# The next check is on col_name[-3], the final position to check. It will take the value of that letter
# by referencing the dictionary letter_to_num (C = 3)
# Then it will multiply that value by (26 ** -(-3 + 1)) (notice how this is 26 ** 2) What is 26 ** 2? 676
# So 3 * 676 = 2028
# it will then add that to col_value (col_value is now 2385)
        
# NO MORE ITERATIONS
# We have reached our target in our range (-(len(col_name) + 1)) or -(3 + 1) == -4. 
# Remember that the end value in a range is not inclusive
# By setting -4 as our end value, our last iteration was at -3. 

# Our col_value now contains the sum of the individual positional values (2385). Let's return it. 
    return col_value

# Testing the function
print(col_index('A')) # prints 1
print(col_index('B')) # prints 2
print(col_index('AA')) # prints 27
print(col_index('CMS')) # prints 2385
print(col_index('AAAA')) # prints 18279


# Bonus 2 Final Code Without Comments

# In[192]:


def col_index(col_name):
    letter_to_num = {
                    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
                    'H': 8, 'I': 9, 'J':10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
                    'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
                    'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
                     }
    col_value = 0
    for index in range(-1, -(len(col_name)+1), -1):
        col_value += letter_to_num[(col_name[index])] * (26 ** -(index + 1))
    return col_value

print(col_index('CMS'))


# In[194]:


# Previous attempt - FAILURE due to misunderstanding how spreadsheets create column headers
# def col_index(col_name):
#     letter_to_num = {
#                     'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
#                     'H': 8, 'I': 9, 'J':10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
#                     'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
#                     'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
#                     }
#     col_value = 0
#     col_length = len(col_name)
#     for letter in col_name:
#         col_value += letter_to_num[letter]
#     col_value = col_value + 25 * (col_length - 1)
#     return col_value

# Testing the function
# print(col_index('A'))
# print(col_index('B'))
# print(col_index('AA'))
# print(col_index('AAB')) #FAILED
# print(col_index('AAD')) #FAILED
# print(col_index('AAAM')) #FAILED


# In[ ]:




