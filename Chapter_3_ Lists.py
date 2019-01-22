#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 3.1
# Names: Store the names of a few of your friends in a list called names. Print
# each person’s name by accessing each element in the list, one at a time.

names = ["alex", "beth", "cathy", "dan"]
print("Names present in the list are: ")
print(names[0] + ", " + names[1] + ", " + names[2] + " and " + names[3])


# In[3]:


# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each message
# should be the same, but each message should be personalized with the
# person’s name.

print("Hello " + names[0].title())
print("Hello " + names[1].title())
print("Hello " + names[2].title())
print("Hello " + names[3].title())


# In[10]:


# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.

guest_list = ["arya", "sansa", "bran", "oberyn"]
print(guest_list[0].title() + ", you are invited to dinner at my place!")
print(guest_list[1].title() + ", you are invited to dinner at my place!")
print(guest_list[2].title() + ", you are invited to dinner at my place!")
print(guest_list[3].title() + ", you are invited to dinner at my place!")


# In[16]:


# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print statement at the
# end of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still
# in your list.

guest_list = ["arya", "sansa", "bran", "oberyn"]
print(guest_list[0].title() + ", you are invited to dinner at my place!")
print(guest_list[1].title() + ", you are invited to dinner at my place!")
print(guest_list[2].title() + ", you are invited to dinner at my place!")
print(guest_list[3].title() + ", you are invited to dinner at my place!")

print("\n")
print(guest_list[3].title() + " cannot make it to the dinner!")

guest_list[3] = "Jon Snow" #modified the guest list
print("\n")

print("Printing second set of invitations: ")
print("\n")

print(guest_list[0].title() + ", you are invited to dinner at my place!")
print(guest_list[1].title() + ", you are invited to dinner at my place!")
print(guest_list[2].title() + ", you are invited to dinner at my place!")
print(guest_list[3].title() + ", you are invited to dinner at my place!")


# In[22]:


# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

guest_list = ["arya", "sansa", "bran", "oberyn"]
print(guest_list[0].title() + ", you are invited to dinner at my place!")
print(guest_list[1].title() + ", you are invited to dinner at my place!")
print(guest_list[2].title() + ", you are invited to dinner at my place!")
print(guest_list[3].title() + ", you are invited to dinner at my place!")

print("\n")
print("Guys, I got a bigger dinner table for us; so inviting more guests :)")
print("\n")

guest_list.insert(0, "brienne")
guest_list.insert(3, "tyrion")
guest_list.append("melisandre")

print("Printing a new set of invitations: ")
print("\n")

print(guest_list[0].title() + ", you are invited to dinner at my place!")
print(guest_list[1].title() + ", you are invited to dinner at my place!")
print(guest_list[2].title() + ", you are invited to dinner at my place!")
print(guest_list[3].title() + ", you are invited to dinner at my place!")
print(guest_list[4].title() + ", you are invited to dinner at my place!")
print(guest_list[5].title() + ", you are invited to dinner at my place!")
print(guest_list[6].title() + ", you are invited to dinner at my place!")


# In[23]:


# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

print("Hey guys, looks like the dinner table won't arrive in time for dinner. So there's space for only 2 more guests")
print("\n")

print("Sorry " + guest_list.pop().title() + ", I can't invite you to dinner :( ")
print("Sorry " + guest_list.pop().title() + ", I can't invite you to dinner :( ")
print("Sorry " + guest_list.pop().title() + ", I can't invite you to dinner :( ")
print("Sorry " + guest_list.pop().title() + ", I can't invite you to dinner :( ")
print("Sorry " + guest_list.pop().title() + ", I can't invite you to dinner :( ")

print("\n")

print(guest_list[0].title() + ", you are invited to dinner at my place!")
print(guest_list[1].title() + ", you are invited to dinner at my place!")

del guest_list[0]
del guest_list[0]

print("\n" + "emptied guest_list:")
print(guest_list)


# In[33]:


# 3-8. Seeing the World: Think of at least five places in the world you’d like to
# visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modifying the
# actual list.
# • Show that your list is still in its original order by printing it.
# • Use sorted() to print your list in reverse alphabetical order without changing
# the order of the original list.
# • Show that your list is still in its original order by printing it again.
# • Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
# • Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
# • Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.

location_list = ["croatia", "germany", "australia", "kerala", "kashmir", "paris"]
print(location_list) #original list

print("\n")

print(sorted(location_list)) #sort w/o modifying
print(location_list)
print("\n")

print(sorted(location_list, reverse = True)) #sort w/o modifying
print(location_list)
print("\n")

location_list.reverse()
print(location_list)
print("\n")

location_list.reverse()
print(location_list)
print("\n")

location_list.sort()
print(location_list)
print("\n")

location_list.sort(reverse=True)
print(location_list)

