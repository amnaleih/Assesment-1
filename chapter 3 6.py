# Invite some people to dinner.
guests = ['Danilo', 'Julia', 'Theo']

name = guests[0].title()
print(name + ", please come to the dinner.")

name = guests[1].title()
print(name + ", please come to the dinner.")

name = guests[2].title()
print(name + ", please come to the dinner.")

name = guests[1].title()
print("\nSorry, " + name + " can't make it to dinner.")

# Denise can't make it! Let's invite Mary instead.
del(guests[1])
guests.insert(1, 'Alexa Smith')

# Print the invitations again.
name = guests[0].title()
print("\n" + name + ", please come to the dinner.")

name = guests[1].title()
print(name + ", please come to the dinner.")

name = guests[2].title()
print(name + ", please come to the dinner.")

# We got a bigger table, so let's add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(0, 'Maria Laurier ')
guests.insert(2, 'Bella Madden')
guests.append('Lizette Hansley')

name = guests[0].title()
print(name + ", please come to the dinner.")

name = guests[1].title()
print(name + ", please come to the dinner.")

name = guests[2].title()
print(name + ", please come to the dinner.")

name = guests[3].title()
print(name + ", please come to the dinner.")

name = guests[4].title()
print(name + ", please come to the dinner.")

name = guests[5].title()
print(name + ", please come to the dinner.")

# Oh no, the table won't arrive on time!
print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

# There should be two people left. Let's invite them.
name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

# Empty out the list.
del(guests[0])
del(guests[0])

# Prove the list is empty.
print(guests)