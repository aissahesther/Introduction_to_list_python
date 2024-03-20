
#exemple of a list that contains a few kinds of bicycles

bicycles = ['trek','cannondale','redline','specialized']

print (bicycles)

#pulling out the first bicycle in the list bicycles

print (bicycles[0])

#format the first element by using the title() method


print (bicycles[0].title())

#display the last item in the list

print (bicycles[-1].upper())


#composing a message using the first item


message = f" My first bicycle was a {bicycles[0].title()}"

print(message)