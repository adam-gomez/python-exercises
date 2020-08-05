#!/usr/bin/env python
# coding: utf-8

# ### Import and test 3 of the functions from your functions exercise file.
# 
# Import each function in a different way:
# 
# - Import the module and refer to the function with the `.` syntax

# In[1]:


import function_exercises as fe


# In[2]:


print(fe.is_two(2))


# - Use `from` to import the function directly

# In[3]:


from function_exercises import is_vowel


# In[4]:


print(is_vowel('u'))


# - Use `from` and give the function a different name

# In[5]:


from function_exercises import capitalize_first_letter_if_consonant as cap


# In[6]:


print(cap('maple'))


# ### For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.
# 1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

# In[7]:


import itertools as it


# In[8]:


print(list(it.product('abc', '123')))
print(f"There are {len(list(it.product('abc', '123')))} different ways to combine the letters \"abc\" with the numbers 1, 2, and 3.")


# 2. How many different ways can you combine two of the letters from "abcd"?

# In[9]:


print(list(it.combinations('abcd', 2)))
len_abcd_comb_2 = len(list(it.combinations('abcd', 2)))
print(f'There are {len_abcd_comb_2} different ways you can combine two of the letters from "abcd".')


# ## Reading the Data from profiles.json
# 
# Save [this](https://gist.githubusercontent.com/ryanorsinger/f77e5ec94dbe14e21771/raw/d4a1f916723ca69ac99fdcab48746c6682bf4530/profiles.json) file as `profiles.json` inside of your exercises directory. Use the load function from the json module to open this file, it will produce a list of dictionaries. 

# In[10]:


import json #bringing in the json functions to this file


# In[11]:


with open('./profiles.json') as access_profiles_json: 
    read_profiles_content = json.load(access_profiles_json)
#using json functions, we can load the file as an object in Python (read_profiles_content)


# In[12]:


print(read_profiles_content) #Lets look at this object


# In[13]:


print(type(read_profiles_content)) 
#This object is a list of nested dictionaries, where each dictionary contains information about a user


# With this in mind, lets look at a single user

# In[14]:


print(read_profiles_content[0])


# This is a bit tough to read. Lets find out what the keys are.

# In[15]:


print(read_profiles_content[0].keys())
# The keys are: _id, index, guid, isActive, balance, picture, age, eyeColor, name, gender, company, email, 
# phone,address, about, registered, latitude, longitude, tags, friends, greeting, favoriteFruit


# Let's get a cleaner view of each of the users

# In[16]:


for user in read_profiles_content:
    print(user)
    print('\n')


# Using this data, write some code that calculates and outputs the following information:
# - Total number of users

# In[17]:


num_users = len(read_profiles_content)
print(f'The total number of users is {num_users}')


# - Number of active users

# In[18]:


# Lets access the isActive key and see what is contained
# A simple way to do this is to create a variable that stores the value called from 
# the list element using its key ('isActive')

is_active_access = user['isActive']
print(is_active_access)

# Notice that while it does print the value, it only prints the very last value in the list
# Python looks at all the info, and only returns the last matching key


# In[19]:


#If we look at the type of the object that we pulled, we can see that its a bool
print(type(is_active_access))


# In[20]:


# To get the number of active users, lets create a list of dictionaries where isActive == True
# Then we can check the length of this list
active_users_list = [user for user in read_profiles_content if user['isActive'] == True]
print(f"The number of active users is {len(active_users_list)}.")


# - Number of inactive users

# In[21]:


# To get the number of inactive users, lets create a list of dictionaries where isActive == False
# Then we can check the length of this list

inactive_users_list = [user for user in read_profiles_content if user['isActive'] == False]
print(f"The number of inactive users is {len(inactive_users_list)}.")

# Since isActive can only be True or False, we also could have concluded this by subtracting
# the number of active users from the total number of users 


# - Grand total of balances for all users

# In[22]:


# Each user has a balance. Lets look at what the value for key 'balance' is
balance_access = user['balance']
print(balance_access)

# Let's also look at its type
print(type(balance_access))


# In[23]:


# Because the value for 'balance' is a string, we will need to collect a list of these balances to convert to float
list_of_balances = [user['balance'] for user in read_profiles_content]
print(list_of_balances)

# We can see that each element of this list is a single value
# Lets make sure that every user had a balance
print(f"The number of users with balances is: {len(list_of_balances)}")


# In[24]:


# Now that we have these balances, we need to clean these strings and convert them to float values
# Lets create an empty list to store our balances with the '$' and ',' characters removed
cleaned_list_of_balances = []
# Lets iterate through our list_of_balances, remove those characters, and append them to our empty list
for balance in list_of_balances:
    balance = balance.replace("$", "")
    balance = balance.replace(",", "")
    cleaned_list_of_balances.append(float(balance))

# Let's look at this list
print(cleaned_list_of_balances)


# In[25]:


# Now lets get the total balance by summing these float values
total_user_balances = 0
for balance in cleaned_list_of_balances:
    total_user_balances += balance

print(f"The total sum of balances is: ${total_user_balances}")


# - Average balance per user

# In[26]:


# Lets divide the total sum of balances by the number of balances
average_user_balance = total_user_balances / len(cleaned_list_of_balances)
average_user_balance = round(average_user_balance, 2) # Lets round this float value to 2 decimal places, since it represents a monetary value
print(f"The average user balance is: ${average_user_balance}")


# - User with the lowest balance

# In[27]:


# For this we can create a dictionary that stores the user's id with their balance
# We will need to zip together a list of users and a list of balances
# We already have a great list of balances (cleaned_list_of_balances), so lets get a list of users

id_list = [user['_id'] for user in read_profiles_content]

# print(id_list)
# Well print(id_list) is difficult to read, but each of these id's are probably unique. 
# At least they are more likely to be unique than a list of names
# Lets check if the ids are unique

_id_flag = 0 # Setting a boolean flag
  
# using set() + len() 
# to check all unique list elements 
_id_flag = len(set(id_list)) == len(id_list) 
  
# printing result

if(_id_flag) : 
    print ("id_list contains all unique elements") 
else :  
    print ("id_list does not contain all unique elements")

# Lets check if the names are unique. We will start with creating a list of names

name_list = [user['name'] for user in read_profiles_content]

# print(name_list)
# The output of printing the name_list is much easier to read, but we need to check if these are all unique names
# Now lets check if they are unique

name_flag = 0 # Setting a boolean flag

# using set() + len() 
# to check all unique list elements 
name_flag = len(set(name_list)) == len(name_list) 

# printing result

if(name_flag) : 
    print ("name_list contains all unique elements") 
else :  
    print ("name_list does not contain all unique elements")


# In[28]:


# Our name_list is easier to read than our id_list. So for the purpose of this exercise, we will use the users names
# Lets create a dictionary that maps the names to the balance values

name_balance_dict = dict(zip(name_list, cleaned_list_of_balances))
# We now have our dictionary of names and balances
# print(name_balance_dict)

user_lowest_balance = min(name_balance_dict, key = name_balance_dict.get)
# This will use min()
# min has 3 parameters (iterable, iterable*, key, default) there can be multiple iterables passed to min
# in this case, our iterable is the dictionary name_balance_dict
# our key is name_balance_dict.get
# min is going to sort the values and return the first value that is sorted
# key = name_balance_dict.get means that the list will be sorted by the values
# and what is being returned is 'name_balance_dict' which defaults to returning a key
# so we will return the key that has the smallest value
print(f'The user with the lowest balance is: {user_lowest_balance}')
print(f'{user_lowest_balance} has a balance of: ${name_balance_dict[user_lowest_balance]}')


# - User with the highest balance

# In[29]:


# We already have a great list of names and balances
# We can repeat the same method using max() instead of min()

user_highest_balance = max(name_balance_dict, key = name_balance_dict.get)

print(f'The user with the highest balance is: {user_highest_balance}')
print(f'{user_highest_balance} has a balance of: ${name_balance_dict[user_highest_balance]}')


# - Most common favorite fruit

# In[30]:


# We need to create a list of all of the favorite fruits held in the dataset

fav_fruit_list = [user['favoriteFruit'] for user in read_profiles_content]
print(fav_fruit_list)
print(f'There are {len(fav_fruit_list)} favorite fruits in the data.') 

# We can see that there were no null values and each user has one favorite fruit


# In[31]:


# We see that there are three unique fruits in the data
print(set(fav_fruit_list))


# In[32]:


# We can create a dictionary that shows the number of counts for each fruit
unique_fruits = set(fav_fruit_list) # this creates the set of unique fruits which we will compare our fav_fruit_list to

# This is an empty dictionary that we will add key,value pairs to where the key is the fruit name and the value is the count of that fruit
fruit_count = {} 

# This iterates through the unique fruits set. At each fruit in that set, it creates a dictionary key = fruit
# It them maps the value to that key to be equal to the count of matching fruit strings in the total list (fav_fruit_list)
for fruit in unique_fruits:
    fruit_count[fruit] = fav_fruit_list.count(fruit) 

print(fruit_count)


# In[33]:


# Now we can use the max function on our fruit_count dictionary to sort the values and return the key paired to the highest value

most_common_fruit = max(fruit_count, key = fruit_count.get)
print(f'The most common fruit is {most_common_fruit}.')
print(f'There are {fruit_count[most_common_fruit]} users who have {most_common_fruit} as their favorite fruit.')


# - Least common favorite fruit

# In[34]:


# We can use the min function on our fruit_count dictionary to return the least common fruit

least_common_fruit = min(fruit_count, key = fruit_count.get)
print(f'The least common fruit is {least_common_fruit}.')
print(f'There are {fruit_count[least_common_fruit]} users who have {least_common_fruit} as their favorite fruit.')


# - Total number of unread messages for all users

# In[35]:


# Lets look at type for the value of the key unread messages
# Uh oh! There is no key directly mapped to the number of unread messages
# Hidden in the greeting is the number of unread messages. Let's look at that value type. 
print(type(user['greeting']))


# In[36]:


# Its a string. Let's look at an example
greeting_access = user['greeting']
print(greeting_access)


# In[37]:


# The greeting string contains a combination of characters. 
# Thankfully, the number of unread messages is represented by digits
# We can generate a list of these greeting strings, and in each string clean away everything but the digits

list_of_greetings = [user['greeting'] for user in read_profiles_content]
print(list_of_greetings)

# Now that we have created our list, lets clean each element by iterating through each string and only appending
# digits to a new list. 

list_unread_digits = [] # This will store our strings cleaned of everything but digits

for message in list_of_greetings: #We will iterate through every greeting in our list of greetings
    digit_string = '' # We create an empty string that will eventually only hold the digits from our greeting
    for character in message: #We iterate through every character in the message
        if character.isdigit(): #If the character is a numeric character
            digit_string += character # The character is added to our digit_string
    list_unread_digits.append(digit_string) #Once we have iterated through a message, we append that digit_string to our list
    
print(list_unread_digits) # We see that we now have a list of strings only containing the number of unread messages for each user


# In[38]:


# Finally, we can convert the elements of the list_unread_digits to integer values and sum them up

total_unread_messages = 0 # This will store our growing number of unread messages as we iterate through our list_unread_digits

for number in list_unread_digits:
    total_unread_messages += int(number)

print(f'The total number of unread messages is: {total_unread_messages}')

