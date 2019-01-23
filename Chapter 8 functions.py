#!/usr/bin/env python
# coding: utf-8

# In[34]:


# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.

def favorite_book(title):
    print("One of my favorite books is " + title)

favorite_book("Pride & Prejudice")


# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.

def make_shirt(size, message_text):
    print("Shirt of size " + size + " and text message '" + message_text + "' is now ready!")

#using positional argument:
make_shirt("small", "Born Free")

#using keyword argument:
make_shirt(message_text = "Do or Die", size = "small")


# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.

def modified_make_shirt(size = "large", message_text = "I love Python"):
    print("Shirt of size " + size + " and text message '" + message_text + "' is now ready!")

#calling without passing arguments:
modified_make_shirt()

#medium shirt with defautlt message
modified_make_shirt("medium")

#shirt of no default size and default message
modified_make_shirt("small", "Merry Christmas")


# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value
# that’s returned.

def city_country(city, country):
    result_string = city.title() + ", " + country.title()
    return result_string

print(city_country("pune", "india"))

# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Add an optional parameter to make_album() that allows you to store the
# number of tracks on an album. If the calling line includes a value for the number
# of tracks, add that value to the album’s dictionary. Make at least one new
# function call that includes the number of tracks on an album.

#num_of_tracks is an optional parameter
def make_album(artist_name, album_title, num_of_tracks = None):
    
    album = {}
    album["artist_name"] = artist_name.title()
    album["album_title"] = album_title.title()
    if num_of_tracks:
        album["num_of_tracks"] = num_of_tracks
    return album

print(make_album("Ed Sheeren", "Divide"))
print(make_album("Taylor Swift", "Reputation", 6))


# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.

quit = ""

while quit != "q":
    artist_name = input("Enter artist's name ")
    album_title = input("Enter album's title ")
    
    print(make_album(artist_name, album_title))
    
    quit = input("enter 'q' if you want to quit OR 'c' if you want to continue ")
    

# 8-9. Magicians: Make a list of magician’s names. Pass the list to a function
# called show_magicians(), which prints the name of each magician in the list.

def show_magicians(magicians_list):
    for magician in magicians_list:
        print(magician)

magicians = ["amy", "brian", "cathy", "debra", "joey"]
show_magicians(magicians)

# 8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians by adding
# the phrase the Great to each magician’s name. Call show_magicians() to
# see that the list has actually been modified.

def make_great(magicians_list):
    i = 0
    while i < len(magicians_list):
        magicians_list[i] = "The Great " + magicians_list[i].title()
        
        i += 1

make_great(magicians)
show_magicians(magicians)

# 8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
# function make_great() with a copy of the list of magicians’ names. Because the
# original list will be unchanged, return the new list and store it in a separate list.
# Call show_magicians() with each list to show that you have one list of the original
# names and one list with the Great added to each magician’s name.

def make_great(magicians_list):
    i = 0
    while i < len(magicians_list):
        magicians_list[i] = "The Great " + magicians_list[i].title()
        
        i += 1
    return magicians_list

magicians = ["amy", "brian", "cathy", "debra", "joey"]

print(make_great(magicians[:]))
show_magicians(magicians)


# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sandwich
# that is being ordered. Call the function three times, using a different number
# of arguments each time.

def order_sandwich(*ingredients):
    print("You ordered a sandwich that has:")
    
    for item in ingredients:
        print(item)
    
order_sandwich("paneer", "cheese", "mayo", "mushrooms")
order_sandwich("bacon", "lettuce", "tomato")
order_sandwich("cheese")

# 8-14. Cars: Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name. It
# should then accept an arbitrary number of keyword arguments. Call the function
# with the required information and two other name-value pairs, such as a
# color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was
# stored correctly.

def make_car(*args, **kwargs):
    car_info = {}
    car_info["manufacturer"] = args[0]
    car_info["model"] = args[1]
    
    for key, val in kwargs.items():
        car_info[key] = val
    
    return car_info

print(make_car('subaru', 'outback', color='blue', tow_package=True))

