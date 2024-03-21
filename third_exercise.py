
#_____Seeing the World: Think of at least five places in the world you’d like to visit.

#Store the locations in a list. Make sure the list is not in alphabetical order.

places_to_visit = ['seoul','tokyo','paris','dubai','maldive']

#Print your list in its original order.

print (places_to_visit)

#Use sorted() to print your list in alphabetical order without modifying the actual list.

print(sorted(places_to_visit))

#Show that your list is still in its original order by printing it.

print(places_to_visit)

#Use sorted() to print your list in reverse alphabetical order without changing the order of the original list

sorted_list = sorted(places_to_visit)


print(sorted_list)
sorted_list.reverse()

print(sorted_list)

#Show that your list is still in its original order by printing it again.

print(places_to_visit)

#Use reverse() to change the order of your list. Print the list to show that its order has changed.

places_to_visit.reverse()

print(places_to_visit)


#Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

places_to_visit.reverse()

print(places_to_visit)

#Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

places_to_visit.sort()

print(places_to_visit)

#Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed

places_to_visit.sort(reverse=True)

print(places_to_visit)


#_________Dinner Guests:use len() to print a message indicating the number of people you are inviting to dinner.

guest_list = ['Emma','Lelen','Nadege','Pelagie']

print(f" the number of people i'm inviting to dinner is {len(guest_list)}")


