#!/usr/bin/env python
# coding: utf-8

# In[8]:


# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.

person = {"first_name" : "neeraj", "last_name" : "kulkarni", "age" : "30", "city" : "pune"}

for key, value in person.items():
    print(key + ", " + value)
    
for key in person.keys():
    print(key)

for value in set(person.values()): #unique values
    print(value)


# In[14]:


# 6-6. Polling: Use the code in favorite_languages.py (page 104).
# • Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

fav_languages = {'jen': 'python', 'sarah': '', 'edward': 'ruby', 'phil': 'python',}

for key, val in fav_languages.items():
    if val:
        print("Thanks for responding " + key.title() + ".")
    else:
        print("Please record your response, " + key.title() + ".")


# In[15]:


# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.

person_1 = {"first_name" : "neeraj", "last_name" : "kulkarni", "age" : "30", "city" : "pune"}
person_2 = {"first_name" : "jai", "last_name" : "kulkarni", "age" : "26", "city" : "pune"}
person_3 = {"first_name" : "suchitra", "last_name" : "joshi", "age" : "35", "city" : "vadodara"}

persons = [person_1, person_2, person_3]

for person in persons:
    print("\n")
    for key, val in person.items():
        print(key + " : " + val)


# In[19]:


# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.

favorite_numbers = {"jai" : [1,23,4], "neeraj" : [76,9, 87], "isha" : [22, 13,4], "riya" : [6,2,1,1,3,45]}

for name, nums in favorite_numbers.items():
    print(name + "'s favorite numbers are:")
    for num in nums:
        print(num)
    print("\n")


# In[22]:


# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information
# you have stored about it.

cities = {"jaipur" : {"country" : "india", "approx_population" : "1000", "fact" : "pink city"}, 
          "pune" : {"country" : "india", "approx_population" : "4567", "fact" : "students' paradise"}, 
          "delhi" : {"country" : "india", "approx_population" : "678999", "fact" : "capital city"}}

for city_name, info in cities.items():
    print(city_name.title() + "'s info:")
    for key, val in info.items():
        print(key + " : " + val)
    print("\n")
    
    

