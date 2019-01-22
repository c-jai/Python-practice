#!/usr/bin/env python
# coding: utf-8

# In[7]:


# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

number = input("Enter a number: ")

if(int(number) % 10 == 0):
    print("The number you have entered is a multiple of 10")
else:
    print("The number is not a multiple of 10")
        


# In[10]:


topping = ""
topping_list = []
while(topping != "end"):
    topping = input("Enter a topping (or type end if no more toppings to be added): ")
    if topping != "end":
        topping_list.append(topping)

print("\nWe'll add these toppings to your pizza: ")
for topping in topping_list:
    print(topping)
    


# In[14]:


# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.

end_loop = "no"

while end_loop == "no":
    print("Check out the cost for your ticket")
    age = int(input("Enter your age: "))
    if age < 3:
        print("You get a free ticket!")
    elif age >= 3 and age <= 12:
        print("Your ticket costs $10")
    else:
        print("Your ticket costs $15")
    end_loop = input("Type yes to quit/ no to continue: ")


# In[17]:


# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
# sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.

sandwich_orders = ["tuna", "BLT", "avocado", "coleslaw", "ham"]
finished_orders = []

i = 0
while sandwich_orders:
    print("I made you a " + sandwich_orders[i] + " sandwich.")
    finished_orders.append(sandwich_orders[i])
    del sandwich_orders[i]
    ++i


# In[19]:


# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

sandwich_orders = ["tuna", "pastrami", "BLT", "avocado", "pastrami", "coleslaw", "ham", "pastrami"]
finished_orders = []

print("The Deli has run out of pastrami sandwiches!\n")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
i = 0
while sandwich_orders:
    print("I made you a " + sandwich_orders[i] + " sandwich.")
    finished_orders.append(sandwich_orders[i])
    del sandwich_orders[i]
    ++i


# In[ ]:




