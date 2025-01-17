guests = ['Danilo', 'Julia', 'Theo']

# Initial invitations
for guest in guests:
    print(f"{guest.title()}, please come to dinner.")

# Danilo can't make it; replacing with Lorrie
print(f"\nSorry, {guests[1].title()} can't make it to dinner.")
guests[1] = 'Lorrie'

# New invitations
for guest in guests:
    print(f"{guest.title()}, please come to dinner.")