#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 4-2. Animals: Think of at least three different animals that have a common characteristic.
# Store the names of these animals in a list, and then use a for loop to
# print out the name of each animal.
# • Modify your program to print a statement about each animal, such as
# A dog would make a great pet.
# • Add a line at the end of your program stating what these animals have in
# common. You could print a sentence such as Any of these animals would
# make a great pet!

animals = ["cat", "dog", "hamster"]

for animal in animals:
    print(animal + " will make a great pet!")


# In[2]:


# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive.

for num in range(1,21):
    print(num)


# In[8]:


# 4-5. Make a list of the numbers from one to 20, and then use min() and max() to make sure your list actually starts at one and
# ends at 20. Also, use the sum() function to see how quickly Python can
# add numbers.

numbers = [num for num in range(1,21)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))


# In[9]:


# 4-6. Odd Numbers: Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number.

odd_numbers = [num for num in range(1,21,2)]

for num in odd_numbers:
    print(num)


# In[12]:


# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.

multiples_of_three = [num for num in range(3, 31, 3)]
#alternate list comprehension:
#multiples_of_three = [num for num in range(3, 31) if num % 3 == 0]


for num in multiples_of_three:
    print(num)


# In[13]:


# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.

cubes = [value**3 for value in range(1,11)]

for num in cubes:
    print(num)


# In[22]:


# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# • Print the message, The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
# • Print the message, Three items from the middle of the list are:. Use a slice
# to print three items from the middle of the list.
# • Print the message, The last three items in the list are:. Use a slice to print
# the last three items in the list.

numbers = [num for num in range(1,11)]
print(numbers[:3])
print(numbers[3:6])
print(numbers[-3:])


# In[24]:


# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message, My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message,
# My friend’s favorite pizzas are:, and then use a for loop to print the second
# list. Make sure each new pizza is stored in the appropriate list.

pizzas = ["hawaiin", "margherita", "veggie"]
friend_pizzas = pizzas[:]

pizzas.append("pepperoni")
friend_pizzas.append("chicken tikka")

print("my favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)
print("\n")

print("my friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)


# In[29]:


# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
# • Use a for loop to print each food the restaurant offers.
# • Try to modify one of the items, and make sure that Python rejects the
# change.
# • The restaurant changes its menu, replacing two of the items with different
# foods. Add a block of code that rewrites the tuple, and then use a for
# loop to print each of the items on the revised menu.

buffet_menu = ("soup", "salad", "appetisers", "entrees", "dessert")

for item in buffet_menu:
    print(item)
    
#buffet_menu[0] = "bread" : causes error

#modifying the menu
buffet_menu = ["noodles", "stews", "cocktails", "sides", "appetisers"]

for item in buffet_menu:
    print(item)

