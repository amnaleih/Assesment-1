# Make an complete list of pets that will be stored.
pets = []

# Make a list of individual pets, and the store each one of them in the list.
pet = {
    'animal type': 'axolotl',
    'name': 'Alfie',
    'owner': 'Luella',
    'weight': '80 grams',
    'eats': 'Bloodoworms and Brine Shrimp',
    'height': '4 cm',
}
pets.append(pet)

pet = {
    'animal type': 'capybara',
    'name': 'Jelly',
    'owner': 'Julie',
    'weight': '35 kg',
    'height': '61 cm',
    'eats': 'grass',
}
pets.append(pet)

pet = {
    'animal type': 'rabbit',
    'name': 'Ivy',
    'owner': 'Jasmine',
    'weight': '37',
    'height': '12 inches',
    'eats': 'lettuce',
}
pets.append(pet)

pet = {
    'animal type': 'Dog',
    'name': 'Mitzy',
    'owner': 'Julia',
    'weight': '10 kg',
    'height': '38 cm',
    'eats': 'chicken breast',
}
pets.append(pet)

# Arrange the information of each pet. 
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")