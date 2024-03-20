

#. Names: Store the names of a few of your friends in a list called names. Print each
#person’s name by accessing each element in the list, one at a time.


names = ['Justine','Jessica', 'Florence','Elga','Reine','Carine-rose']

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print (names[-1])

#  Greetings: Start with the list you used , but instead of just printing
#each person’s name, print a message to them. The text of each message should be the same,
#but each message should be personalized with the person’s name.


messages = f"hello my friend {names[0]}, how are you doing?"

print( messages)

messages = f"hello my friend {names[1]}, how are you doing?"
print( messages)

messages = f"hello my friend {names[2]}, how are you doing?"
print( messages)

messages = f"hello my friend {names[3]}, how are you doing?"
print( messages)

messages = f"hello my friend {names[4]}, how are you doing?"
print( messages)

messages = f"hello my friend {names[5]}, how are you doing?"
print( messages)


#Your Own List: Think of your favorite mode of transportation, such as a motorcycle
#or a car, and make a list that stores several examples. Use your list to print a series of
#statements about these items, such as “I would like to own a Honda motorcycle.”


cars = ['Bmw','Audi','Peugeot','Toyota','Mercedes']

statement = f"i would like to own a {cars[0]} car."

print (statement)

statement = f"i would like to own a {cars[1]} car."

print (statement)
statement = f"i would like to own a {cars[2]} car."

print (statement)
statement = f"i would like to own a {cars[3]} car."

print (statement)
statement = f"i would like to own a {cars[4]} car."

print (statement)
