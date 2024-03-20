
#Modifying element in a list

motocycles = ['honda','yamaha', 'suzuki']

print (motocycles)


motocycles[0]= 'ducati'

print (motocycles)

# Adding elements to a list

#1- Appending elements in the end of a list

motocycles.append('honda')

print(motocycles)

#2 inserting elements into the list

motocycles.insert(1, "dubai")

print (motocycles)

# Removing element from a list 

#using del statement

del motocycles[0]

print (motocycles)


#using pop() method

popped_motocycle = motocycles.pop()

print(motocycles)

print (popped_motocycle)


#popping items from any Position in a list


first_owned = motocycles.pop(0)


print(f"The first motorcycle i own was a {first_owned.title()}.")


#removing an item by Value

motocycles.remove('yamaha')

print(motocycles)

