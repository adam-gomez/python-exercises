#!/usr/bin/env python
# coding: utf-8

# # Control Structure Exercises

# ### Conditional Basics

# In[52]:


# prompt the user for a day of the week, print out whether the day is Monday or not
input_day_of_the_week = input("What day of the week is it? ")
if input_day_of_the_week.upper() == 'MONDAY':
    print('Today is Monday')
else:
    print('Today is not Monday')


# In[43]:


# prompt the user for a day of the week, print out whether the day is a weekday or a weekend
input_weekday_weekend = input("What day of the week is it? ")
if input_weekday_weekend.upper() in ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY']:
    print('Today is a weekday')
elif input_weekday_weekend.upper() in ['SATURDAY', 'SUNDAY']:
    print('Today is a weekend')
else:
    print('That is not a valid day of the week')


# In[6]:


# create variables and make up values for
# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
num_hours_worked = 53.2
hourly_rate = 122
if num_hours_worked <= 40:
    print("The week's paycheck will be $" + str(num_hours_worked * hourly_rate)) 
else:
    print("The week's paycheck will be $" + str((40 * hourly_rate) + ((num_hours_worked - 40) * hourly_rate * 1.5))) 


# ### Loop Basics

# #### While

# In[9]:


# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.
int_var = 5
while int_var <= 15:
    print(int_var)
    int_var += 1


# In[11]:


# Create a while loop that will count by 2's starting with 0 and ending at 100. 
# Follow each number with a new line.
new_int = 0
while new_int <= 100:
    print(new_int)
    new_int += 2


# In[12]:


# Alter your loop to count backwards by 5's from 100 to -10.
also_int = 100
while also_int >= -10:
    print(also_int)
    also_int -= 5


# In[13]:


# Create a while loop that starts at 2, and displays the number squared on each line 
# while the number is less than 1,000,000.
squared_int = 2
while squared_int < 1_000_000:
    print(squared_int)
    squared_int **= 2


# In[14]:


# Write a loop that uses print to create the output shown below (each number on its own line)
# 100 95 90 85 80 75 70 65 60 55 50 45 40 35 30 25 20 15 10 5
start_at_100 = 100
while start_at_100 > 0:
    print(start_at_100)
    start_at_100 -= 5


# #### For Loops

# In[53]:


# Write some code that prompts the user for a number, 
# then shows a multiplication table up through 10 for that number
user_num = input("Give me an integer: ")
if user_num.isdigit():
    for num in list(range(1,11)):
        product = num * int(user_num)
        print(str(user_num) + " x " + str(num) + " = " + str(product))
else:
    print("You did not enter an integer.")


# In[33]:


# Create a for loop that uses print to create the output shown below.
# 1
# 22
# 333
# ...
# 999999999
for i in range(1,10):
    print(str(i)*i)


# #### Break and continue

# In[45]:


# Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
while True:

    start_odd = input("Please input an odd number between 1 and 50 (inclusive): ")
    
    if not start_odd.isdigit():
        print("\nPlease input a positive integer value without decimals. ")
        continue

    if int(start_odd) < 1 or int(start_odd) > 50:
        print("\nYou have entered a number outside of the specified range. Please try again. ")
        continue
        
    if int(start_odd) % 2 != 1:
        print("\nYou have failed to enter an odd number. Please try again. ")
        continue
        
    else:
        break
        
print(f"\nNumber to skip is: {start_odd}\n")

for num in range(1, 51):
    if num == int(start_odd):
        print(f"Yikes! Skipping number: {start_odd}")
        continue
    if num % 2 == 1:
        print(f"Here is an odd number: {num}")


# In[1]:


# This is an alternative solution that uses try and except
while True:
    
    try:
        start_odd = int(input("Please input an odd number between 1 and 50 (inclusive): "))
    except ValueError:
        print("\nSorry I didn't understand that. Please no strings or decimals. Try again. ")
        continue

    if int(start_odd) < 1 or int(start_odd) > 50:
        print("\nYou have entered a number outside of the specified range. Please try again. ")
        continue
        
    if int(start_odd) % 2 != 1:
        print("\nYou have failed to enter an odd number. Please try again. ")
        continue 
        
    else:
        break
        
print(f"\nNumber to skip is: {start_odd}]\n")

for num in range(1, 51):
    if num == int(start_odd):
        print(f"Yikes! Skipping number: {start_odd}")
        continue
    if num % 2 == 1:
        print(f"Here is an odd number: {num}")


# In[54]:


# The input function can be used to prompt for input and use that input in your python code.
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
while True:
    count_to_num = input("Please enter a positive integer without decimal places: ")
    
    if not int(count_to_num.isdigit()):
        print("Sorry! That was not a positive integer without decimal places. Please try again.  ")
        continue
    if int(count_to_num) < 0:
        print("Please enter a positive number. ")
        continue
    else:
        break

if int(num) > 0:
    for i in range (0, int(count_to_num) + 1, 1):
        print(f"Counting to {count_to_num}: {i}")


# In[24]:


# Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the user entered down to 1.
while True:
    count_down_from_num = input("Please enter a positive integer without decimal places: ")
    
    if not int(count_down_from_num.isdigit()):
        print("Sorry! That was not a positive integer without decimal places. Please try again.  ")
        continue
    if int(count_to_num) < 0:
        print("Please enter a positive number. ")
        continue
    else:
        break

if int(num) > 0:
    for i in range (int(count_down_from_num), 0, -1):
        print(f"Counting to 1 from {count_down_from_num}: {i}")


# ## FizzBuzz

# In[25]:


# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(1, 101, 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# ## Display a table of powers.

# In[50]:


# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

while True:    
    table_target = int(input("What number would you like to go up to? "))
    if table_target > 0:
        print("\nHere is your table!\n")
        print("number | squared | cubed")
        print("------ | ------- | -----")
        number_lst = []
        for i in list(range(1, table_target + 1, 1)):
            number_lst.append(i)
        for n in range(0, len(number_lst), 1):
            print(f"{number_lst[n]}      | {number_lst[n]**2}       | {number_lst[n]**3}")
    user_continue = input("Would you like to create another table? (y/n): ")
    if user_continue == "y":
        continue
    if user_continue == "n":
        print("\nThank you! Stay classy!")
        break
    else:
        print("\nI didn't understand you. Goodbye!")
        break
# Program can be improved by having the continue question prompt the user again if they do not enter exactly 'y' or 'n'
# BONUS
# Research python's format string specifiers to align the table
# Solution Provided Below in following cells


# In[36]:


# Messing around with alignment code
left_aligned = 'number'
left_divider = "|"
center = 'squared'
right_divider = "|"
right_aligned = 'cubed'
print(f"{left_aligned:<7}|{center:^11}|{right_aligned:>6}")
# after the : < means align on the left of the area that is # width
# after the : ^ means align in the center of the area that is # width
# after the : > means align on the right of the area that is # width
# using format, you will need to have each of the text areas defined by a variable


# In[51]:


# FORMATTING STRING POSITIONS
# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

while True:    
    table_target = int(input("What number would you like to go up to? "))
    if table_target > 0:
        print("\nHere is your table!\n")
        print("number | squared | cubed")
        print("------ | ------- | -----")
        number_lst = []
        for i in list(range(1, table_target + 1, 1)):
            number_lst.append(i)
        for n in range(0, len(number_lst), 1):
            normal = number_lst[n]
            squared = number_lst[n] ** 2
            cubed = number_lst[n] ** 3
            print(f"{normal:<7}| {squared:<8}| {cubed:<5}")
    user_continue = input("\nWould you like to create another table? (y/n): ")
    if user_continue == "y":
        continue
    if user_continue == "n":
        print("\nThank you! Stay classy!")
        break
    else:
        print("\nI didn't understand you. Goodbye!")
        break


# In[56]:


# Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0
# BONUS: Edit your grade ranges to include plusses and minuses
# A+	97–100%
# A	93–96%
# A−	90–92%
# B+	87–89%
# B	83–86%
# B−	80–82%
# C+	77–79%
# C	73–76%
# C-	70–72%
# D+	67–69%
# D	63–66%
# D-	60–62%
# F	0–59%

print("Welcome to the wonderous wonderful grade converter!\n")
print("This AMAZING program will convert your numerical grades into letter grades.")

while True:
    num_grade = float(input("\nPlease enter a numerical grade from 0 to 100: "))
    if num_grade >= 97:
        print("\nYour letter grade is: A+")
    elif num_grade >= 93:
        print("\nYour letter grade is: A")
    elif num_grade >= 88:
        print("\nYour letter grade is: A-")
    elif num_grade >= 86:
        print("\nYour letter grade is: B+")
    elif num_grade >= 83:
        print("\nYour letter grade is: B")
    elif num_grade >= 80:
        print("\nYour letter grade is: B-")
    elif num_grade >= 76:
        print("\nYour letter grade is: C+")
    elif num_grade >= 71:
        print("\nYour letter grade is: C")
    elif num_grade >= 67:
        print("\nYour letter grade is: C-")
    elif num_grade >= 65:
        print("\nYour letter grade is: D+")
    elif num_grade >= 62:
        print("\nYour letter grade is: D")
    elif num_grade >= 60:
        print("\nYour letter grade is: D-")
    elif num_grade >= 0:
        print("\nYour letter grade is: F")
    else:
        print("I award you no points, and may God have mercy on your soul.")
    user_continue = input("\nWould you like to enter another grade? (y/n): ")
    if user_continue == 'y':
        continue
    if user_continue == 'n':
        print("\nThank you for using grade converter!")
        break
    else:
        print("\nI didn't understand that. Goodbye!")
# Program can be improved by having the continue question prompt the user again if they do not enter exactly 'y' or 'n'


# In[48]:


# Create a list of dictionaries where each dictionary represents a book that you have read. 
# Each dictionary in the list should have the keys title, author, and genre. 
# Loop through the list and print out information about each book.
# Prompt the user to enter a genre, 
# then loop through your books list and print out the titles of all the books in that genre.

books_i_have_read = [{'title': 'The Perfect Close', 'author': 'James Muir', 'genre': 'Business/Economics'},
                     {'title': 'Unscripted', 'author': 'MJ Demarco', 'genre': 'Business/Economics'},
                     {'title': 'Man Up', 'author': 'Bedros Keuilian', 'genre': 'Self Help'},
                     {'title': 'The Introverts Edge', 'author': 'Matthew Pollard', 'genre': 'Business/Economics'},
                     {'title': 'A River In Darkness', 'author': 'Masaji Ishikawa', 'genre': 'Memoir'},
                     {'title': 'Pitch Anything', 'author': 'Oren Klaff', 'genre': 'Business/Economics'},
                     {'title': 'The $100 Startup', 'author': 'Chris Guillebeau', 'genre': 'Business/Economics'},
                     {'title': 'The Dunwich Horror', 'author': 'H P Lovecraft', 'genre': 'Horror'},
                     {'title': 'Dune', 'author': 'Frank Herbert', 'genre': 'Science Fiction'},
                     {'title': 'The Way of Kings', 'author': 'Brandon Sanderson', 'genre': 'Fantasy'},
                     {'title': 'Words of Radiance', 'author': 'Brandon Sanderson', 'genre': 'Fantasy'},
                     {'title': 'The Hobbit', 'author': 'J R R Tolkien', 'genre': 'Fantasy'},
                     {'title': 'The Lazy Dungeon Master', 'author': 'Michael Shea', 'genre': 'Crafts/Hobbies'},
                     {'title': 'Principles', 'author': 'Ray Dalio', 'genre': 'Autobiography'},
                     {'title': 'SPIN Selling', 'author': 'Neil Rackham', 'genre': 'Business/Economics'},
                     {'title': 'Getting Things Done', 'author': 'David Allen', 'genre': 'Self Help'},
                     {'title': 'The Millionaire Mind', 'author': 'Thomas Stanley', 'genre': 'Business/Economics'},
                     {'title': 'Lost Connections', 'author': 'Johann Hari', 'genre': 'Science'},
                     {'title': 'Never Split the Difference', 'author': 'Chris Voss', 'genre': 'Self Help'},
                     {'title': 'The Compound Effect', 'author': 'Darren Hardy', 'genre': 'Self Help'},
                     {'title': 'Way of the Wolf', 'author': 'Jordan Belfort', 'genre': 'Business/Economics'},
                     {'title': 'The Adventures of Huckleberry Finn', 'author': 'Mark Twain', 'genre': 'Adventure'},
                     {'title': 'Treasure Island', 'author': 'Robert Louis Stevenson', 'genre': 'Adventure'},
                     {'title': 'Wuthering Heights', 'author': 'Charlotte Bronte', 'genre': 'Drama'},
                     {'title': 'The Scarlet Letter', 'author': 'Nathaniel Hawthorne', 'genre': 'Drama'},
                     {'title': 'Gulliver\'s Travels', 'author': 'Jonathan Swift', 'genre': 'Adventure'},
                     {'title': 'Frankenstein', 'author': 'Mary Shelley', 'genre': 'Horror'},
                     {'title': 'Oliver Twist', 'author': 'Charles Dickens', 'genre': 'Drama'},
                     {'title': 'Dracula', 'author': 'Bram Stoker', 'genre': 'Horror'},
                     {'title': 'Brave New World', 'author': 'Aldous Huxley', 'genre': 'Science Fiction'},
                     {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'genre': 'Drama'},
                     {'title': 'Animal Farm', 'author': 'George Orwell', 'genre': 'Satire'},
                     {'title': 'The Little Prince', 'author': 'Antoine de Saint Exupery', 'genre': 'Fantasy'},
                     {'title': 'The Grapes of Wrath', 'author': 'John Steinbeck', 'genre': 'Drama'},
                     {'title': 'The Lion, the Witch, and the Wardrobe', 'author': 'C. S. Lewis', 'genre': 'Fantasy'},
                     {'title': 'Lord of the Flies', 'author': 'William Golding', 'genre': 'Drama'},
                     {'title': 'The Trial', 'author': 'Franz Kafka', 'genre': 'Mystery'},
                     {'title': 'All Quiet on the Western Front', 'author': 'Erich Maria Remarch', 'genre': 'Drama'},
                     {'title': '1984', 'author': 'George Orwell', 'genre': 'Science Fiction'},
                     {'title': 'The Jungle', 'author': 'Upton Sinclair', 'genre': 'History'},
                     {'title': 'The Da Vinci Code', 'author': 'Dan Brown', 'genre': 'Suspense'},
                     {'title': 'Charlotte\'s Web', 'author': 'E.B. White', 'genre': 'Children\'s'},
                     {'title': 'The Curious Incident of the Dog in the Nighttime', 'author': 'Mark Haddon', 'genre': 'Mystery'},
                     {'title': 'The Kite Runner', 'author': 'Khaled Hosseini', 'genre': 'Drama'},
                     {'title': 'Beowulf', 'author': 'Unknown', 'genre': 'Fantasy'},
                     {'title': 'Paradise Lost', 'author': 'John Milton', 'genre': 'Fantasy'},
                     {'title': 'Autobiography of a Yogi', 'author': 'Paramahansa Yogananda', 'genre': 'Religion/Spirituality'},
                     {'title': 'Siddharta', 'author': 'Frank Herbert', 'genre': 'Religion/Spirituality'},
                     {'title': 'New Seeds of Contemplation', 'author': 'John Merton', 'genre': 'Religion/Spirituality'},
                     {'title': 'The Man Who Mistook His Wife for a Hat', 'author': 'Oliver Sacks', 'genre': 'Science'},
                     {'title': 'The Lives of a Cell', 'author': 'Lewis Thomas', 'genre': 'Science'},
                     {'title': 'The Disappearing Spoon', 'author': 'Sam Kean', 'genre': 'Science'},
                     {'title': 'Ender\'s Game', 'author': 'Orson Scott Card', 'genre': 'Science Fiction'},
                     {'title': 'The Diary of a Young Girl', 'author': 'Anne Frank', 'genre': 'Diary'},
                     {'title': 'The Prince', 'author': 'Niccolo Machiavelli', 'genre': 'Philosophy'},
                     {'title': 'Confessions', 'author': 'Augustine', 'genre': 'Philosophy'},
                     {'title': 'The Power of Now', 'author': 'Eckhart Tolle', 'genre': 'Religion/Spirituality'},
                     {'title': 'Zen Mind: Beginner\'s Mind', 'author': 'Shunryu Suzuki', 'genre': 'Religion/Spirituality'},
                     {'title': 'The Road Less Traveled', 'author': 'Scott Peck', 'genre': 'Self Help'},
                     {'title': 'Tao Te Ching', 'author': 'Lao Tzu', 'genre': 'Religion/Spirituality'},
                     {'title': 'Black Elk Speaks', 'author': 'Black Elk', 'genre': 'Religion/Spirituality'},
                     {'title': 'Night', 'author': 'Elie Wiesel', 'genre': 'Memoir'},
                     {'title': 'The Candle of Vision', 'author': 'George William Russell', 'genre': 'Religion/Spirituality'},
                     {'title': 'Revelations of Divine Love', 'author': 'Julian of Norwich', 'genre': 'Religion/Spirituality'},
                     {'title': 'How Not to Die', 'author': 'Michael Greger', 'genre': 'Health/Fitness'},
                     {'title': 'Mad Cowboy', 'author': 'Howard Lyman', 'genre': 'Memoir'},]
print("These are some of the books I have read:\n")
for book in books_i_have_read:
    print(book)

print('\nGenres:\nAdventure\nAutobiography\nBusiness/Economics\nCrafts/Hobbies\nChildren\'s\nDiary\nDrama\nFantasy\nHealth/Fitness\nHorror\nMemoir\nMystery\nPhilosophy\nReligion/Spirituality\nSatire\nScience\nScience Fiction\nSelf Help\nSuspense')

genre_list = ['adventure', 'autobiography', 'business/economics', 'crafts/hobbies', 'children\'s', 'diary', 'drama', 'fantasy', 'health/fitness', 'horror', 'memoir', 'mystery', 'philosophy', 'religion/spirituality', 'satire', 'science', 'science fiction', 'self help', 'suspense']
while True:
    requested_genre = input("\nPlease enter a genre: ")
    if requested_genre.lower() not in genre_list:
        print("\nThat was not a valid genre. Please enter a valid genre: ")
        continue
    else:
        break
for book in books_i_have_read:
    if book['genre'].lower() == requested_genre.lower():
        print(book['title'])


# In[ ]:
