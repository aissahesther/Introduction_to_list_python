
#Guest List: If you could invite anyone, living or deceased, to dinner, who would you
#invite? Make a list that includes at least three people you’d like to invite to dinner. Then
#use your list to print a message to each person, inviting them to dinne

guest_list = ["Lelen","Nadège","Pélagie","Emma","Gracia"]

message = f"Hello {guest_list[0]},i want to invite you to dinner this monday."

print (message)

message = f"Hello {guest_list[1]},i want to invite you to dinner this monday."

print (message)


message = f"Hello {guest_list[2]},i want to invite you to dinner this monday."

print (message)


message = f"Hello {guest_list[3]},i want to invite you to dinner this monday."

print (message)


message = f"Hello {guest_list[4]},i want to invite you to dinner this monday."

print (message)


# changing Guest List


#Add a print() call at the end of your program stating the name of the guest who can’t make it.
guest_pop = guest_list.pop(4)

print(f"{guest_pop} will unfortunately no longer be part of tomorrow's dinner ")


# Modify your list, replacing the name of the guest who can’t
# make it with the name of the new person you are inviting.

print(guest_list)

guest_list.append("Donné")

print(guest_list)




message = f"Hello {guest_list[0]},i want to invite you to dinner this monday."

print (message)

message = f"Hello {guest_list[1]},i want to invite you to dinner this monday."

print (message)


message = f"Hello {guest_list[2]},i want to invite you to dinner this monday."

print (message)


message = f"Hello {guest_list[3]},i want to invite you to dinner this monday."

print (message)


message = f"Hello {guest_list[4]},i want to invite you to dinner this monday."

print (message)


# More Guests

print(f"I found a bigger table")

#Use insert() to add one new guest to the beginning of your list.


guest_list.insert(0,'Maman')

print(guest_list)

#Use insert() to add one new guest to the middle of your list.

guest_list.insert(3,'Papa')

print(guest_list)

#Use append() to add one new guest to the end of your list

guest_list.append("Shayiah")

print(guest_list)

#Print a new set of invitation messages, one for each person in your list.


message = f"Hello {guest_list[0]},i want to invite you to dinner this monday."

print (message)

message = f"Hello {guest_list[1]},i want to invite you to dinner this monday."

print (message)


message = f"Hello {guest_list[2]},i want to invite you to dinner this monday."

print (message)


message = f"Hello {guest_list[3]},i want to invite you to dinner this monday."

print (message)


message = f"Hello {guest_list[4]},i want to invite you to dinner this monday."

print (message)


message = f"Hello {guest_list[5]},i want to invite you to dinner this monday."

print (message)

message = f"Hello {guest_list[6]},i want to invite you to dinner this monday."

print (message)


message = f"Hello {guest_list[-1]},i want to invite you to dinner this monday."

print (message)


#shrinking Guest List

# You just found out that your new dinner table won’t arrive in
#time for the dinner, and you have space for only two guests.



print(f"for sad reasons I can only invite 2 people ")


guest_pop = guest_list.pop()

print(f"Hello {guest_pop}, i'm sorrt but i can't invite you to dinner")

guest_pop = guest_list.pop()

print(f"Hello {guest_pop}, i'm sorrt but i can't invite you to dinner")
guest_pop = guest_list.pop()

print(f"Hello {guest_pop}, i'm sorrt but i can't invite you to dinner")

guest_pop = guest_list.pop()

print(f"Hello {guest_pop}, i'm sorrt but i can't invite you to dinner")
guest_pop = guest_list.pop()

print(f"Hello {guest_pop}, i'm sorrt but i can't invite you to dinner")

guest_pop = guest_list.pop()

print(f"Hello {guest_pop}, i'm sorrt but i can't invite you to dinner")



#Print a message to each of the two people still on your list,
#letting them know they’re still invited


message = f"Hello {guest_list[0]}, you're still invited to dinner this monday."

print (message)

message = f"Hello {guest_list[1]}, you're still invited to dinner this monday."

print (message)

#removing the last 2 names from the list

del guest_list[0]
print(guest_list)
del guest_list[0]

print(guest_list)